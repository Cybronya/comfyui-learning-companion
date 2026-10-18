---
key: 视频生成/图生视频/SmoothMix2.0-角色设计动态展示-首尾帧15s长视频_2027726162666987522.json
name: SmoothMix2.0-角色设计动态展示-首尾帧15s长视频_2027726162666987522.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SmoothMix2.0-角色设计动态展示-首尾帧15s长视频_2027726162666987522.json
hash: 6be5ce0f6de0340e
coverage: 0.929577
learned_at: 2026-10-15 22:35:18
nodes: [FluxKontextMultiReferenceLatentMethod, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, FluxKontextMultiReferenceLatentMethod, CFGNorm, VAEEncode, VAEDecode, KSampler, PreviewBridge, ModelSamplingAuraFlow, CheckpointLoaderSimple, TextEncodeQwenImageEditPlus, VAEEncode, TextEncodeQwenImageEditPlus, KSamplerSelect, VAELoader, CFGNorm, CLIPLoader, BasicScheduler, CLIPLoader, BasicGuider, VAELoader, ReferenceLatent, CLIPTextEncode, VAEEncode, UNETLoader, BasicScheduler, VAEEncode, SamplerCustomAdvanced, SamplerEulerAncestral, VAEDecode, ImageScaleBy, RandomNoise, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAELoader, CLIPLoader, FluxKontextImageScale, ModelSamplingAuraFlow, ShowText|pysssss, SimpleMath+, CLIPTextEncode, WanFirstLastFrameToVideo, SimpleMath+, CLIPTextEncode, ImageResizeKJv2, QwenMultiangleCameraNode, WanFirstLastFrameToVideo, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, VAEDecode, VAEDecode, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced, ImageResizeKJv2, QwenMultiangleCameraNode, ModelPatchTorchSettings, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, INTConstant, CLIPLoader, FluxKontextImageScale, ImageResizeKJv2, ImageResizeKJv2, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, VAELoader, PathchSageAttentionKJ, PrimitiveNode, Note, easy promptConcat, easy promptConcat, easy positive, Note, QwenMultiangleCameraNode, easy positive, easy promptConcat, QwenMultiangleCameraNode, easy promptConcat, easy positive, Note, easy indexAnything, easy indexAnything, easy indexAnything, easy indexAnything, PreviewBridge, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, PreviewBridge, PreviewBridge, VHS_VideoCombine, VHS_VideoCombine, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, SamplerCustom, INTConstant, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, UNETLoader, PrimitiveNode, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, LoadImage, Note, Note, Note, easy positive, ImpactMakeAnyList, CheckpointLoaderSimple, VAEDecode, Note, INTConstant, PreviewBridge, INTConstant, PreviewBridge, INTConstant, INTConstant, UNETLoader, UNETLoader, WanFirstLastFrameToVideo, INTConstant]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 6, "checkpoint": "Qwen-Rapid-AIO-NSFW-v20.safetensors", "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/SmoothMix2.0-角色设计动态展示-首尾帧15s长视频_2027726162666987522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027726162666987522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（142 个）：
- `FluxKontextMultiReferenceLatentMethod`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `FluxKontextMultiReferenceLatentMethod`
- `CFGNorm`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PreviewBridge`
- `ModelSamplingAuraFlow`
- `CheckpointLoaderSimple` ★核心
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CFGNorm`
- `CLIPLoader`
- `BasicScheduler`
- `CLIPLoader`
- `BasicGuider`
- `VAELoader`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `BasicScheduler`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerEulerAncestral` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `RandomNoise`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `CLIPLoader`
- `FluxKontextImageScale`
- `ModelSamplingAuraFlow`
- `ShowText|pysssss`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `QwenMultiangleCameraNode`
- `WanFirstLastFrameToVideo`
- `SimpleMath+`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageResizeKJv2`
- `QwenMultiangleCameraNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `INTConstant`
- `CLIPLoader`
- `FluxKontextImageScale`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PathchSageAttentionKJ`
- `PrimitiveNode`
- `Note`
- `easy promptConcat`
- `easy promptConcat`
- `easy positive`
- `Note`
- `QwenMultiangleCameraNode`
- `easy positive`
- `easy promptConcat`
- `QwenMultiangleCameraNode`
- `easy promptConcat`
- `easy positive`
- `Note`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `easy indexAnything`
- `PreviewBridge`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `PreviewBridge`
- `PreviewBridge`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `SamplerCustom` ★核心
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveNode`
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `easy positive`
- `ImpactMakeAnyList`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `Note`
- `INTConstant`
- `PreviewBridge`
- `INTConstant`
- `PreviewBridge`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanFirstLastFrameToVideo`
- `INTConstant`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v20.safetensors`

## 知识

覆盖率 **93%**（132/142）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`CFGNorm`、`VAEEncode`、`VAEDecode`、`KSampler`、`PreviewBridge`、`ModelSamplingAuraFlow`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlus`、`KSamplerSelect`、`VAELoader`、`CLIPLoader`、`BasicScheduler`、`BasicGuider`、`ReferenceLatent`、`CLIPTextEncode`、`UNETLoader`、`SamplerCustomAdvanced`、`SamplerEulerAncestral`、`ImageScaleBy`、`RandomNoise`、`FluxKontextImageScale`、`SimpleMath+`、`WanFirstLastFrameToVideo`、`ImageResizeKJv2`、`QwenMultiangleCameraNode`、`KSamplerAdvanced`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`INTConstant`、`easy promptConcat`、`easy positive`、`easy indexAnything`、`VHS_VideoCombine`、`ImageBatchExtendWithOverlap`、`SamplerCustom`、`ModelSamplingSD3`、`RIFE VFI`、`LoadImage`、`ImpactMakeAnyList`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
