---
key: 视频生成/文生视频/hunyuanvideo1.5_图文生视频以及超分放大_1993577420943015938.json
name: hunyuanvideo1.5_图文生视频以及超分放大_1993577420943015938
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/hunyuanvideo1.5_图文生视频以及超分放大_1993577420943015938.json
hash: 556a8807c68225dd
coverage: 0.875
learned_at: 2026-10-11 02:57:39
nodes: [PreviewImage, CLIPTextEncode, ImageCrop, HunyuanVideo15ImageToVideo, CLIPTextEncode, EmptyHunyuanVideo15Latent, ModelSamplingSD3, ModelSamplingSD3, KSampler, HunyuanVideo15LatentUpscaleWithModel, LoraLoaderModelOnly, DualCLIPLoader, CLIPVisionLoader, LatentUpscaleModelLoader, LoadImage, VAELoader, VAEDecodeTiled, VHS_VideoCombine, VHS_VideoCombine, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, KSampler, Reroute, VAEDecode, Reroute, Reroute, VAEEncode, VHS_LoadVideo, CLIPVisionEncode, HunyuanVideo15SuperResolution]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 592768531317173, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/hunyuanvideo1.5_图文生视频以及超分放大_1993577420943015938.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/hunyuanvideo1.5_图文生视频以及超分放大_1993577420943015938.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ImageCrop`
- `HunyuanVideo15ImageToVideo`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanVideo15Latent`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `HunyuanVideo15LatentUpscaleWithModel`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `CLIPVisionLoader`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `VAEEncode` ★核心
- `VHS_LoadVideo`
- `CLIPVisionEncode`
- `HunyuanVideo15SuperResolution`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `592768531317173`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`CLIPTextEncode`、`ImageCrop`、`HunyuanVideo15ImageToVideo`、`EmptyHunyuanVideo15Latent`、`ModelSamplingSD3`、`KSampler`、`HunyuanVideo15LatentUpscaleWithModel`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`CLIPVisionLoader`、`LatentUpscaleModelLoader`、`LoadImage`、`VAELoader`、`VAEDecodeTiled`、`VHS_VideoCombine`、`UNETLoader`、`PathchSageAttentionKJ`、`VAEDecode`、`VAEEncode`、`VHS_LoadVideo`、`CLIPVisionEncode`、`HunyuanVideo15SuperResolution`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、VAEDecodeTiled

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
