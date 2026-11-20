---
key: 平台全量/Qwen-Image-Edit-2511 图片高清修复+上色+放大工作流V1.0_2012703581962510337.json
name: Qwen-Image-Edit-2511 图片高清修复+上色+放大工作流V1.0_2012703581962510337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-Edit-2511 图片高清修复+上色+放大工作流V1.0_2012703581962510337.json
hash: b22f7c58f4d4e270
coverage: 0.666667
learned_at: 2026-11-14 00:51:43
nodes: [VAEDecode, QwenEditAdaptiveLongestEdge, VAELoader, QwenEditOutputExtractor, GetNode, GetNode, QwenEditConfigPreparer, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResize+, GetImageSize+, ImageScaleBy, GetNode, ImageScaleBy, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, GetNode, GetNode, GetImageSize+, SetNode, TTP_Image_Tile_Batch, TTP_Image_Assy, ImageResize+, TTP_Tile_image_size, GetNode, easy cleanGpuUsed, ImageCASharpening+, Note Plus (mtb), Label (rgthree), Label (rgthree), Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), Note, ModelSamplingAuraFlow, CFGNorm, PathchSageAttentionKJ, CR Text, KSamplerAdvanced, ConditioningZeroOut, ModelPatchTorchSettings, SaveImage, Image Comparer (rgthree), Label (rgthree), Note, CropWithPadInfo, CLIPLoader, TextEncodeQwenImageEditPlusCustom_lrzjason, LoraLoader, UNETLoader, Label (rgthree), LoadImage, SetNode, PrimitiveFloat, SetNode, LoadImage]
patterns: [lora]
missing: []
parameters: {"cfg": 4, "denoise": "simple", "lora_name": "Qwen-Image-Edit-Unblur-Upscale_20.safetensors", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/Qwen-Image-Edit-2511 图片高清修复+上色+放大工作流V1.0_2012703581962510337.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-Edit-2511 图片高清修复+上色+放大工作流V1.0_2012703581962510337.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `VAEDecode` ★核心
- `QwenEditAdaptiveLongestEdge`
- `VAELoader`
- `QwenEditOutputExtractor`
- `GetNode`
- `GetNode`
- `QwenEditConfigPreparer`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResize+`
- `GetImageSize+`
- `ImageScaleBy`
- `GetNode`
- `ImageScaleBy`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `GetNode`
- `GetNode`
- `GetImageSize+`
- `SetNode`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `ImageResize+`
- `TTP_Tile_image_size`
- `GetNode`
- `easy cleanGpuUsed`
- `ImageCASharpening+`
- `Note Plus (mtb)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PathchSageAttentionKJ`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `ConditioningZeroOut`
- `ModelPatchTorchSettings`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Label (rgthree)`
- `Note`
- `CropWithPadInfo`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `Label (rgthree)`
- `LoadImage`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `lora_name` = `Qwen-Image-Edit-Unblur-Upscale_20.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **67%**（40/60）

**有卡**：`VAEDecode`、`QwenEditAdaptiveLongestEdge`、`VAELoader`、`QwenEditOutputExtractor`、`QwenEditConfigPreparer`、`ImageResize+`、`GetImageSize+`、`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`ImageCASharpening+`、`Note Plus (mtb)`、`Label (rgthree)`、`SaveImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`PathchSageAttentionKJ`、`CR Text`、`KSamplerAdvanced`、`ConditioningZeroOut`、`ModelPatchTorchSettings`、`CropWithPadInfo`、`CLIPLoader`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`LoraLoader`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage、UNETLoader、CFGNorm
