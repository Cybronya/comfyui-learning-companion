---
key: 图片生成/文生图/【数字人_文生图生视频】Wan2.2 S2V 文生图生视频工作流_1966350469507526658.json
name: 【数字人_文生图生视频】Wan2.2 S2V 文生图生视频工作流_1966350469507526658
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【数字人_文生图生视频】Wan2.2 S2V 文生图生视频工作流_1966350469507526658.json
hash: cf9b95b5ce18499e
coverage: 0.774194
learned_at: 2026-10-10 20:59:31
nodes: [EnhancedLoadDiffusionModel, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, AudioEncoderEncode, LoraLoaderModelOnly, WanSoundImageToVideo, VAEDecode, Note, Note, PrimitiveNode, PrimitiveNode, PrimitiveNode, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, EmptyLatentImage, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, KSamplerAdvanced, CLIPTextEncode, SaveImage, VAELoader, LoadAudio, VHS_VideoCombine, Fast Groups Bypasser (rgthree), PrimitiveNode, KSampler]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 1094293246584357, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【数字人_文生图生视频】Wan2.2 S2V 文生图生视频工作流_1966350469507526658.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【数字人_文生图生视频】Wan2.2 S2V 文生图生视频工作流_1966350469507526658.json`

## 结构

**节点**（31 个）：
- `EnhancedLoadDiffusionModel`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `AudioEncoderEncode`
- `LoraLoaderModelOnly`
- `WanSoundImageToVideo`
- `VAEDecode`
- `Note`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAELoader`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `VAEDecode`
- `EmptyLatentImage`
- `UNETLoader`
- `DualCLIPLoader`
- `LoraLoaderModelOnly`
- `KSamplerAdvanced`
- `CLIPTextEncode`
- `SaveImage`
- `VAELoader`
- `LoadAudio`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveNode`
- `KSampler`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `768`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1094293246584357`
- `steps` = `8`
- `width` = `512`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`EnhancedLoadDiffusionModel`、`AudioEncoderLoader`、`CLIPLoader`、`CLIPTextEncode`、`AudioEncoderEncode`、`LoraLoaderModelOnly`、`WanSoundImageToVideo`、`VAEDecode`、`Note`、`PrimitiveNode`、`VAELoader`、`EmptyLatentImage`、`UNETLoader`、`DualCLIPLoader`、`KSamplerAdvanced`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
