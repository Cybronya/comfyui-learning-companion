---
key: 视频生成/图生视频/（自用）Wan2.2 All-in-one V10+CineScale图生视频极速版V1_1962792289108115457.json
name: （自用）Wan2.2 All-in-one V10+CineScale图生视频极速版V1_1962792289108115457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1962792289108115457.json
hash: ed2980604d32d5b4
coverage: 1
learned_at: 2026-10-15 22:31:32
nodes: [CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, JWInteger, SaveImage, LoadImage, VHS_VideoCombine, LoadLatent, VAELoader, VHS_VideoCombine, VAEDecode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, JWInteger, VHS_VideoCombine, JWInteger, SaveLatent, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CheckpointLoaderSimple, VHS_VideoCombine, VAEDecode, LoadImage, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 389557544230464, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 All-in-one V10+CineScale图生视频极速版V1_1962792289108115457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962792289108115457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `JWInteger`
- `SaveImage`
- `LoadImage`
- `VHS_VideoCombine`
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
- `VHS_VideoCombine`
- `JWInteger`
- `SaveLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `389557544230464`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`JWInteger`、`SaveImage`、`LoadImage`、`VHS_VideoCombine`、`LoadLatent`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`SaveLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
