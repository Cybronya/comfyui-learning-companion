---
key: 视频生成/图生视频/（本地解码）Wan2.2 All-in-one V10+CineScale图生视频极速版V1 林耀_2013897396320739330.json
name: （本地解码）Wan2.2 All-in-one V10+CineScale图生视频极速版V1 林耀_2013897396320739330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（本地解码）Wan2.2 All-in-one V10+CineScale图生视频极速版V1 林耀_2013897396320739330.json
hash: effd632ec297741f
coverage: 1
learned_at: 2026-10-15 22:34:33
nodes: [CLIPVisionEncode, WanImageToVideo, ModelSamplingSD3, SaveImage, LoadImage, LoadLatent, VAELoader, VHS_VideoCombine, VAEDecode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CheckpointLoaderSimple, LoadImage, JWInteger, JWInteger, JWInteger, SaveImage, TT_img_enc, VAEDecode, CR Prompt Text, SaveImage, TT_img_enc_v2, SaveLatent, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 900242796877168, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（本地解码）Wan2.2 All-in-one V10+CineScale图生视频极速版V1 林耀_2013897396320739330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013897396320739330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPVisionEncode`
- `WanImageToVideo`
- `ModelSamplingSD3`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `SaveImage`
- `TT_img_enc`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `SaveImage`
- `TT_img_enc_v2`
- `SaveLatent`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `900242796877168`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`CLIPVisionEncode`、`WanImageToVideo`、`ModelSamplingSD3`、`SaveImage`、`LoadImage`、`LoadLatent`、`VAELoader`、`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CheckpointLoaderSimple`、`JWInteger`、`TT_img_enc`、`CR Prompt Text`、`TT_img_enc_v2`、`SaveLatent`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
