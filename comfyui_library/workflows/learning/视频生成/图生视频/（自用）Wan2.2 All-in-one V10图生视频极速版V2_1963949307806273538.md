---
key: 视频生成/图生视频/（自用）Wan2.2 All-in-one V10图生视频极速版V2_1963949307806273538.json
name: （自用）Wan2.2 All-in-one V10图生视频极速版V2_1963949307806273538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（自用）Wan2.2 All-in-one V10图生视频极速版V2_1963949307806273538.json
hash: 85c99d3ed82ba18c
coverage: 1
learned_at: 2026-10-15 22:31:34
nodes: [CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, JWInteger, SaveImage, LoadImage, LoadLatent, VAELoader, VHS_VideoCombine, VAEDecode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CheckpointLoaderSimple, LoadImage, SaveImage, CR Prompt Text, VAEDecode, JWFloat, TT_img_enc]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 37936175864580, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 All-in-one V10图生视频极速版V2_1963949307806273538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963949307806273538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
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
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `SaveImage`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `JWFloat`
- `TT_img_enc`

## 关键参数

- `seed` = `37936175864580`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`JWInteger`、`SaveImage`、`LoadImage`、`LoadLatent`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`CR Prompt Text`、`JWFloat`、`TT_img_enc`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
