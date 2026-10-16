---
key: 视频生成/文生视频/Wan2.2 All-in-one  本地解码_1958350616806494210.json
name: Wan2.2 All-in-one  本地解码_1958350616806494210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1958350616806494210.json
hash: 76fbda74b9ad286c
coverage: 0.972973
learned_at: 2026-10-15 22:43:42
nodes: [EmptyHunyuanLatentVideo, CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, Fast Groups Bypasser (rgthree), JWInteger, JWInteger, JWInteger, CR Text, PathchSageAttentionKJ, JWInteger, CLIPVisionLoader, CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, JWInteger, VAELoader, VHS_VideoCombine, VAEDecode, LoadLatent, KSampler, SaveImage, LoadImage, VHS_VideoCombine, VAEDecode, SaveLatent, VHS_VideoCombine, VAEDecode, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, CR Text, SaveLatent, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v8.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 233090473853729, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 All-in-one  本地解码_1958350616806494210.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958350616806494210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Text`
- `PathchSageAttentionKJ`
- `JWInteger`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `JWInteger`
- `VAELoader`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LoadLatent`
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SaveLatent`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CR Text`
- `SaveLatent`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`

## 关键参数

- `seed` = `233090473853729`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v8.safetensors`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`ModelSamplingSD3`、`JWInteger`、`CR Text`、`PathchSageAttentionKJ`、`CLIPVisionLoader`、`CLIPVisionEncode`、`WanImageToVideo`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`LoadLatent`、`KSampler`、`SaveImage`、`LoadImage`、`SaveLatent`、`CheckpointLoaderSimple`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveLatent、CLIPVisionEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
