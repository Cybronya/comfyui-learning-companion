---
key: 视频生成/图生视频/（自用）Wan2.2 All-in-one V9.1+CineScale图生视频极速版V1_1959492715388022786.json
name: （自用）Wan2.2 All-in-one V9.1+CineScale图生视频极速版V1_1959492715388022786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（自用）Wan2.2 All-in-one V9.1+CineScale图生视频极速版V1_1959492715388022786.json
hash: 30f8cfbac60fb78b
coverage: 1
learned_at: 2026-10-15 22:31:24
nodes: [CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, JWInteger, SaveImage, LoadImage, LoadLatent, VAELoader, VHS_VideoCombine, VAEDecode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CheckpointLoaderSimple, LoadImage, SaveImage, VAEDecode, JWFloat, TT_img_enc, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 20079441881423, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 All-in-one V9.1+CineScale图生视频极速版V1_1959492715388022786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1959492715388022786.json`

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
- `VAEDecode` ★核心
- `JWFloat`
- `TT_img_enc`
- `CR Prompt Text`

## 关键参数

- `seed` = `20079441881423`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`JWInteger`、`SaveImage`、`LoadImage`、`LoadLatent`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`JWFloat`、`TT_img_enc`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
