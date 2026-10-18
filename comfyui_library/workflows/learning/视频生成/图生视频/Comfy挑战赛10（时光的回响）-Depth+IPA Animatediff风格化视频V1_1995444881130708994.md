---
key: 视频生成/图生视频/Comfy挑战赛10（时光的回响）-Depth+IPA Animatediff风格化视频V1_1995444881130708994.json
name: Comfy挑战赛10（时光的回响）-Depth+IPA Animatediff风格化视频V1_1995444881130708994.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Comfy挑战赛10（时光的回响）-Depth+IPA Animatediff风格化视频V1_1995444881130708994.json
hash: 00d16036329c736b
coverage: 0.9375
learned_at: 2026-10-15 22:33:23
nodes: [ADE_AnimateDiffSamplingSettings, ADE_LoopedUniformContextOptions, ADE_ApplyAnimateDiffModelSimple, VAEDecode, DepthAnythingV2Preprocessor, PreviewImage, KSampler, EmptyLatentImage, ADE_UseEvolvedSampling, PrimitiveInt, ADE_MultivalDynamic, ADE_MultivalDynamic, ControlNetLoader, IPAdapterUnifiedLoader, InvertMask, CLIPTextEncode, CLIPTextEncode, ACN_AdvancedControlNetApply_v2, IPAdapterAdvanced, RepeatImageBatch, CheckpointLoaderSimple, ADE_LoadAnimateDiffModel, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, ImageConcatMulti, VHS_VideoCombine, PDIMAGE_LongerSize, ImageCompositeMasked, ImageConcanate, VHS_VideoCombine]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 24, "cfg": 2, "checkpoint": "realismBYSTABLEYOGI_v4LCM.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1080, "sampler_name": "lcm", "scheduler": "beta", "seed": 1092926705307409, "steps": 11, "width": 1920}
---

# 视频生成/图生视频/Comfy挑战赛10（时光的回响）-Depth+IPA Animatediff风格化视频V1_1995444881130708994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1995444881130708994.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ADE_AnimateDiffSamplingSettings`
- `ADE_LoopedUniformContextOptions`
- `ADE_ApplyAnimateDiffModelSimple`
- `VAEDecode` ★核心
- `DepthAnythingV2Preprocessor`
- `PreviewImage`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ADE_UseEvolvedSampling`
- `PrimitiveInt`
- `ADE_MultivalDynamic`
- `ADE_MultivalDynamic`
- `ControlNetLoader`
- `IPAdapterUnifiedLoader`
- `InvertMask`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ACN_AdvancedControlNetApply_v2` ★核心
- `IPAdapterAdvanced`
- `RepeatImageBatch`
- `CheckpointLoaderSimple` ★核心
- `ADE_LoadAnimateDiffModel`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `ImageCompositeMasked`
- `ImageConcanate`
- `VHS_VideoCombine`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1092926705307409`
- `steps` = `11`
- `cfg` = `2`
- `sampler_name` = `lcm`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `24`
- `controlnet_strength` = `1`
- `checkpoint` = `realismBYSTABLEYOGI_v4LCM.safetensors`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`ADE_AnimateDiffSamplingSettings`、`ADE_LoopedUniformContextOptions`、`ADE_ApplyAnimateDiffModelSimple`、`VAEDecode`、`DepthAnythingV2Preprocessor`、`KSampler`、`EmptyLatentImage`、`ADE_UseEvolvedSampling`、`ADE_MultivalDynamic`、`ControlNetLoader`、`IPAdapterUnifiedLoader`、`InvertMask`、`CLIPTextEncode`、`ACN_AdvancedControlNetApply_v2`、`IPAdapterAdvanced`、`RepeatImageBatch`、`CheckpointLoaderSimple`、`ADE_LoadAnimateDiffModel`、`VHS_VideoCombine`、`LoadImage`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`ImageCompositeMasked`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、DepthAnythingV2Preprocessor
