---
key: 视频生成/图生视频/最新wan2.1上传图片生成跳舞视频_1910518744249237505.json
name: 最新wan2.1上传图片生成跳舞视频_1910518744249237505.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1910518744249237505.json
hash: 62af878d0496e742
coverage: 0.779412
learned_at: 2026-10-15 22:29:30
nodes: [PrimitiveNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VAELoader, VAEEncode, Note, FluxGuidance, StringConstantMultiline, KSampler, Seed Everywhere, CLIPTextEncode, ShowText|pysssss, ShowText|pysssss, SimpleCondition+, CLIPTextEncode, JanusModelLoader, LayerUtility: ImageScaleByAspectRatio V2, RepeatLatentBatch, Note, Int, DualCLIPLoader, VAEDecode, Reroute, Reroute, PreviewImage, JanusImageUnderstanding, Reroute, LoraLoader, LoraLoader, UNETLoader, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoSampler, WanVideoVAELoader, WanVideoControlEmbeds, WanVideoExperimentalArgs, ImageUpscaleWithModel, UpscaleModelLoader, VHS_VideoCombine, WanVideoDecode, WanVideoBlockSwap, WanVideoEncode, WanVideoModelLoader, ImageBlend, ImageResizeKJ, WanVideoTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, JanusModelLoader, JanusImageUnderstanding, AIO_Preprocessor, AIO_Preprocessor, WanVideoClipVisionEncode, Fast Groups Bypasser (rgthree), LoraLoader, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), WanVideoImageToVideoEncode, LoadImage, VHS_LoadVideo, VHS_VideoCombine, ImageResizeKJ, LoadWanVideoClipTextEncoder]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "lora_name": "麦橘x极氪白白酱-majicFlus_麦橘x极氪白白酱", "sampler_name": "euler", "scheduler": "normal", "seed": 18268136955394, "steps": 20, "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/最新wan2.1上传图片生成跳舞视频_1910518744249237505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1910518744249237505.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `PrimitiveNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `VAEEncode` ★核心
- `Note`
- `FluxGuidance`
- `StringConstantMultiline`
- `KSampler` ★核心
- `Seed Everywhere`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SimpleCondition+`
- `CLIPTextEncode` ★核心
- `JanusModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatLatentBatch`
- `Note`
- `Int`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `PreviewImage`
- `JanusImageUnderstanding`
- `Reroute`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoControlEmbeds`
- `WanVideoExperimentalArgs`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `ImageBlend`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `JanusModelLoader`
- `JanusImageUnderstanding`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `WanVideoClipVisionEncode`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoader` ★核心
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `LoadWanVideoClipTextEncoder` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `18268136955394`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.8000000000000002`
- `lora_name` = `麦橘x极氪白白酱-majicFlus_麦橘x极氪白白酱`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **78%**（53/68）

**有卡**：`VAELoader`、`VAEEncode`、`FluxGuidance`、`StringConstantMultiline`、`KSampler`、`Seed Everywhere`、`CLIPTextEncode`、`SimpleCondition+`、`JanusModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatLatentBatch`、`Int`、`DualCLIPLoader`、`VAEDecode`、`JanusImageUnderstanding`、`LoraLoader`、`UNETLoader`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoControlEmbeds`、`WanVideoExperimentalArgs`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoEncode`、`WanVideoModelLoader`、`ImageBlend`、`ImageResizeKJ`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`AIO_Preprocessor`、`WanVideoClipVisionEncode`、`LoadImage`、`WanVideoImageToVideoEncode`、`VHS_LoadVideo`、`LoadWanVideoClipTextEncoder`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、FluxGuidance
