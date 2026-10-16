---
key: 视频生成/图生视频/First-LastFrames2Video首尾帧生视频 Minimax H3_2088068432045629441.json
name: First-LastFrames2Video首尾帧生视频 Minimax H3_2088068432045629441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/First-LastFrames2Video首尾帧生视频 Minimax H3_2088068432045629441.json
hash: d1a1d44764b8e89c
coverage: 0.547619
learned_at: 2026-10-16 21:27:28
nodes: [VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, Int, CLIPLoader, Anything Everywhere, ModelAttentionBackend, UNETLoader, SetNode, VAELoader, SetNode, LoraLoaderBypassModelOnly, Anything Everywhere, LayerUtility: PurgeVRAM V2, SetNode, SetNode, SetNode, MiniMaxH3ImageToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, SetNode, KSampler, VAEDecodeAudio, VHS_VideoCombine, ConditioningZeroOut, GetNode, MathExpression|pysssss, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, ImageScale, ImageConcanate, easy showAnything, RH_Captioner, LoadImage, LoadImage, StringFunction|pysssss]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "linear_quadratic", "seed": 233331150297155, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/First-LastFrames2Video首尾帧生视频 Minimax H3_2088068432045629441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/First-LastFrames2Video首尾帧生视频 Minimax H3_2088068432045629441.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（42 个）：
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `Int`
- `CLIPLoader`
- `Anything Everywhere`
- `ModelAttentionBackend`
- `UNETLoader` ★核心
- `SetNode`
- `VAELoader`
- `SetNode`
- `LoraLoaderBypassModelOnly` ★核心
- `Anything Everywhere`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxH3ImageToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `KSampler` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `ConditioningZeroOut`
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `ImageScale`
- `ImageConcanate`
- `easy showAnything`
- `RH_Captioner`
- `LoadImage`
- `LoadImage`
- `StringFunction|pysssss`

## 关键参数

- `seed` = `233331150297155`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`

## 知识

覆盖率 **55%**（23/42）

**有卡**：`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`Int`、`CLIPLoader`、`ModelAttentionBackend`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`LayerUtility: PurgeVRAM V2`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`KSampler`、`VAEDecodeAudio`、`VHS_VideoCombine`、`ConditioningZeroOut`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScale`、`ImageConcanate`、`RH_Captioner`、`LoadImage`、`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、VAEDecodeAudio

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
