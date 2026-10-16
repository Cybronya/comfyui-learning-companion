---
key: 视频生成/图生视频/（人体解剖学CLIP）Wan2.2 All-in-one V8图生视频极速版V1（自用）_1958145251049353218.json
name: （人体解剖学CLIP）Wan2.2 All-in-one V8图生视频极速版V1（自用）_1958145251049353218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958145251049353218.json
hash: d6e88c0695a84bb7
coverage: 1
learned_at: 2026-10-15 22:31:21
nodes: [JWInteger, CLIPVisionLoader, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, WanImageToVideo, ModelSamplingSD3, JWInteger, SaveLatent, SaveImage, LoadImage, VAEDecode, VHS_VideoCombine, KSampler, VHS_VideoCombine, LoadImage, PathchSageAttentionKJ, CheckpointLoaderSimple, LoadLatent, VAELoader, VHS_VideoCombine, VHS_VideoCombine, VAEDecode, CLIPTextEncode, CLIPLoader, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v8.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 187689099624870, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（人体解剖学CLIP）Wan2.2 All-in-one V8图生视频极速版V1（自用）_1958145251049353218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958145251049353218.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `JWInteger`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `JWInteger`
- `SaveLatent`
- `SaveImage`
- `LoadImage`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `PathchSageAttentionKJ`
- `CheckpointLoaderSimple` ★核心
- `LoadLatent`
- `VAELoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `187689099624870`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v8.safetensors`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`JWInteger`、`CLIPVisionLoader`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanImageToVideo`、`ModelSamplingSD3`、`SaveLatent`、`SaveImage`、`LoadImage`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`LoadLatent`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、SaveLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
