---
key: 平台全量/MiniMax H3-Image｜文生图（经典KSampler·可选PE）_2120388077565865985.json
name: MiniMax H3-Image｜文生图（经典KSampler·可选PE）_2120388077565865985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax H3-Image｜文生图（经典KSampler·可选PE）_2120388077565865985.json
hash: 6136f5f94bd1439e
coverage: 0.666667
learned_at: 2026-11-14 00:41:39
nodes: [UNETLoader, CLIPLoader, VAELoader, MiniMaxH3ImageConditioning, ConditioningZeroOut, TextGenerateV2, CLIPLoader, PrimitiveStringMultiline, PreviewAny, KSampler, PrimitiveStringMultiline, StringReplace, ComfySwitchNode, VAEDecode, PrimitiveStringMultiline, JsonExtractString, SaveImage, ResolutionSelector, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1034036343949685, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/MiniMax H3-Image｜文生图（经典KSampler·可选PE）_2120388077565865985.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax H3-Image｜文生图（经典KSampler·可选PE）_2120388077565865985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `MiniMaxH3ImageConditioning`
- `ConditioningZeroOut`
- `TextGenerateV2`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `StringReplace`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `JsonExtractString`
- `SaveImage`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `seed` = `1034036343949685`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（14/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ImageConditioning`、`ConditioningZeroOut`、`TextGenerateV2`、`KSampler`、`StringReplace`、`VAEDecode`、`JsonExtractString`、`SaveImage`、`ResolutionSelector`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
