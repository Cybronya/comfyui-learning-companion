---
key: 视频生成/图生视频/（自用）Wan2.2 All-in-one V9.2+CineScale图生视频极速版V1_1961655579871789057.json
name: （自用）Wan2.2 All-in-one V9.2+CineScale图生视频极速版V1_1961655579871789057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（自用）Wan2.2 All-in-one V9.2+CineScale图生视频极速版V1_1961655579871789057.json
hash: 25a92e9031455a89
coverage: 1
learned_at: 2026-10-15 22:31:29
nodes: [CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, JWInteger, SaveImage, LoadImage, LoadLatent, VAELoader, VHS_VideoCombine, VAEDecode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, JWInteger, CheckpointLoaderSimple, JWInteger, SaveLatent, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, LoadImage, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 655485123219488, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 All-in-one V9.2+CineScale图生视频极速版V1_1961655579871789057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961655579871789057.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `JWInteger`
- `SaveImage`
- `LoadImage`
- `LoadLatent`
- `VAELoader`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JWInteger`
- `CheckpointLoaderSimple` ★核心
- `JWInteger`
- `SaveLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `655485123219488`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v9.2.safetensors`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`JWInteger`、`SaveImage`、`LoadImage`、`LoadLatent`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`CheckpointLoaderSimple`、`SaveLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
