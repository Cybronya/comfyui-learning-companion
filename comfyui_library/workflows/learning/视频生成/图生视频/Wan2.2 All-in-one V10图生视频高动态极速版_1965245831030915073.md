---
key: 视频生成/图生视频/Wan2.2 All-in-one V10图生视频高动态极速版_1965245831030915073.json
name: Wan2.2 All-in-one V10图生视频高动态极速版_1965245831030915073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 All-in-one V10图生视频高动态极速版_1965245831030915073.json
hash: bbd09f13795720c3
coverage: 1
learned_at: 2026-10-15 22:31:36
nodes: [ModelSamplingSD3, KSampler, WanImageToVideo, CLIPVisionEncode, CLIPVisionLoader, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, CreateVideo, PreViewVideo, JWInteger, JWInteger, LoadImage, CR Prompt Text, VAEDecode, LayerUtility: PurgeVRAM V2, ImageFromBatch+, CheckpointLoaderSimple, wanBlockSwap, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 592728373153415, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2 All-in-one V10图生视频高动态极速版_1965245831030915073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965245831030915073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `KSampler` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CreateVideo`
- `PreViewVideo`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageFromBatch+`
- `CheckpointLoaderSimple` ★核心
- `wanBlockSwap`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `592728373153415`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10.safetensors`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`ModelSamplingSD3`、`KSampler`、`WanImageToVideo`、`CLIPVisionEncode`、`CLIPVisionLoader`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CreateVideo`、`PreViewVideo`、`JWInteger`、`LoadImage`、`CR Prompt Text`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`ImageFromBatch+`、`CheckpointLoaderSimple`、`wanBlockSwap`、`CLIPTextEncode`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CLIPVisionEncode、CLIPVisionLoader、CR Prompt Text

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
