"""Minimal SRT/VTT parsing and word-level timing expansion."""
import re
from dataclasses import dataclass


@dataclass
class Cue:
    start: float
    end: float
    text: str


@dataclass
class Word:
    start: float
    end: float
    text: str


_TIME_RE = re.compile(
    r"(\d+):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d+):(\d{2}):(\d{2})[.,](\d{3})"
)


def _to_seconds(h, m, s, ms) -> float:
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def parse_srt(path: str) -> list[Cue]:
    """Parses a standard .srt (or WebVTT-ish) file into a list of Cues.

    Supports both sentence/phrase-level cues and word-level cues (one word
    per cue), since real-world subtitle exports (YouTube, CapCut, Whisper)
    usually give phrase-level timing.
    """
    raw = open(path, encoding="utf-8").read()
    blocks = re.split(r"\n\s*\n", raw.strip())
    cues: list[Cue] = []
    for block in blocks:
        lines = [line for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        time_line = next((line for line in lines if "-->" in line), None)
        if not time_line:
            continue
        m = _TIME_RE.search(time_line)
        if not m:
            continue
        start = _to_seconds(*m.groups()[0:4])
        end = _to_seconds(*m.groups()[4:8])
        text_lines = lines[lines.index(time_line) + 1 :]
        text = " ".join(text_lines).strip()
        if text:
            cues.append(Cue(start=start, end=end, text=text))
    return cues


def cues_to_words(cues: list[Cue]) -> list[Word]:
    """Expands phrase-level cues into per-word timing.

    Each word's share of the cue's duration is weighted by its character
    length, which is a close-enough approximation of natural speech pacing
    when no true word-level alignment is available.
    """
    words: list[Word] = []
    for cue in cues:
        tokens = cue.text.split()
        if not tokens:
            continue
        if len(tokens) == 1:
            words.append(Word(cue.start, cue.end, tokens[0]))
            continue
        duration = max(cue.end - cue.start, 0.05)
        weights = [len(t) + 1 for t in tokens]
        total_weight = sum(weights)
        t = cue.start
        for token, weight in zip(tokens, weights):
            share = duration * (weight / total_weight)
            words.append(Word(t, t + share, token))
            t += share
    return words


def group_words(words: list[Word], chunk_size: int = 1) -> list[Word]:
    """Regroups words into fixed-size chunks (e.g. 1-2 words per caption)."""
    if chunk_size <= 1:
        return words
    grouped: list[Word] = []
    for i in range(0, len(words), chunk_size):
        chunk = words[i : i + chunk_size]
        grouped.append(
            Word(
                start=chunk[0].start,
                end=chunk[-1].end,
                text=" ".join(w.text for w in chunk),
            )
        )
    return grouped
