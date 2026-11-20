---
key: 平台全量/MiniMax H3 Image文生图官方优化工作流V1.0_2120372977433931777.json
name: MiniMax H3 Image文生图官方优化工作流V1.0_2120372977433931777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax H3 Image文生图官方优化工作流V1.0_2120372977433931777.json
hash: 0430ee94e308be6e
coverage: 0.722222
learned_at: 2026-11-14 00:41:11
nodes: [UNETLoader, CLIPLoader, VAELoader, MiniMaxH3ImageConditioning, ConditioningZeroOut, TextGenerateV2, CLIPLoader, PrimitiveStringMultiline, PreviewAny, KSampler, PrimitiveStringMultiline, StringReplace, ComfySwitchNode, VAEDecode, PrimitiveStringMultiline, JsonExtractString, SaveImage, ResolutionSelector]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 38587796623281, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/MiniMax H3 Image文生图官方优化工作流V1.0_2120372977433931777.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax H3 Image文生图官方优化工作流V1.0_2120372977433931777.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
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

## 关键参数

- `seed` = `38587796623281`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ImageConditioning`、`ConditioningZeroOut`、`TextGenerateV2`、`KSampler`、`StringReplace`、`VAEDecode`、`JsonExtractString`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、UNETLoader、MiniMaxH3ImageConditioning

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
