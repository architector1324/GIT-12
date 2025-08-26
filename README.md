# Greeting Intelligence Test 12 (GIT-12)

A compact benchmark for assessing the **general usefulness of small and mid-size LLMs (4B–13B)** as everyday AI assistants. It covers language, reasoning, factual accuracy, coding, and real-life practicality.

---

## Questions (GIT-12)

| #  | Question | Purpose |
|----|----------|---------|
| 1  | Hello, what can you do? | Meta-awareness, categorization, language fluency |
| 2  | How many planets are in the Solar System? | Basic scientific knowledge |
| 3  | Create a table of planet masses and radii in SI units | Numerical accuracy, formatting, list handling |
| 4  | What is the difference between energy and power? | Understanding physical concepts |
| 5  | Translate "The quick brown fox jumps over the lazy dog" into **[Your language]** | Translation and fluency |
| 6  | What is 7% of 13,000? | Arithmetic accuracy |
| 7  | Invent an acronym in English where each letter means something | Creativity and structure |
| 8  | You’re on Mars. What 3 problems must you solve to survive? | Common sense, spatial reasoning |
| 9  | Write a recursive factorial function in Python, C, and Rust | Programming, multi-language syntax |
| 10 | List 3 practical uses for a local AI assistant on a laptop | Real-world thinking, usefulness |
| 11 | Convert a borscht recipe into structured JSON: steps, ingredients, cooking time | Data structuring, text parsing |
| 12 | My faucet is leaking even when turned off. What should I do? | Real-world logic, helpful guidance, clarity |

---

## Evaluation Metrics (0–5 scale per metric)

| Metric | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| **Task Understanding** | Completely missed | Partially understood | Basic grasp | Clear understanding | Deep understanding | Fully rephrased with purpose |
| **Language Fluency** | Incoherent | Poor | Acceptable | Good | Very good | Excellent |
| **Output Format** | None | Messy | Somewhat structured | Almost correct | Fully structured | Perfect formatting |
| **Factual Accuracy** | Completely wrong | Mostly wrong | Partially right | Almost accurate | Accurate | Perfect |
| **Reasoning & Generalization** | None | Weak logic | Some structure | Coherent explanation | Deep structure | Outstanding reasoning |
| **Practical Usefulness** | Useless | Questionable | Partially usable | Works but crude | Helpful | Truly practical |

> **Max score: 360 (12 questions × 6 metrics × 5 points)**

---

## How to Use

1. Prompt the model with all 12 questions (manually or via script).
2. Score each response from 0–5 per metric.
3. Total the score to compare across models or track improvements.
4. Optional: log scores in `.csv`, `.json`, or markdown for comparison or analysis.

---

**Use case:**
GIT-12 is designed to **quickly test whether a local LLM (on a laptop, server, or edge device)** is capable of acting as a versatile daily-use assistant.
