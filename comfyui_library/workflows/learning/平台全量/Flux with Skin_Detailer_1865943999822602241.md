---
key: 平台全量/Flux with Skin_Detailer_1865943999822602241.json
name: Flux with Skin_Detailer_1865943999822602241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux with Skin_Detailer_1865943999822602241.json
hash: adb223c101409d58
coverage: 0.528571
learned_at: 2026-11-14 00:28:11
nodes: [SegsToCombinedMask, MaskPreview+, PrimitiveNode, ImpactSimpleDetectorSEGS, ImpactSEGSOrderedFilter, SegsToCombinedMask, ImpactSimpleDetectorSEGS, MaskPreview+, SegsToCombinedMask, SegsToCombinedMask, MaskPreview+, SubtractMaskForEach, CLIPTextEncode, CLIPTextEncode, SaveImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Image Comparer (rgthree), DetailerForEach, Note, Note, CR Upscale Image, ImageSharpen, MaskPreview+, Note, BasicScheduler, VAEDecode, UltralyticsDetectorProvider, Note, KSamplerSelect, EmptyLatentImage, GlobalSeed //Inspire, Note, Note, Note, BasicGuider, RandomNoise, SamplerCustomAdvanced, CR SDXL Aspect Ratio, VAELoader, UNETLoader, DualCLIPLoader, UltralyticsDetectorProvider, SAMLoader, LoraLoader, CheckpointLoaderSimple, CLIPTextEncode, ImageApplyLUT+]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "epicrealism_naturalSinRC1VAE.safetensors", "height": 1024, "lora_name": "more_details.safetensors", "strength_clip": 1, "strength_model": 0.75, "width": 1024}
---

# 平台全量/Flux with Skin_Detailer_1865943999822602241.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux with Skin_Detailer_1865943999822602241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `SegsToCombinedMask`
- `MaskPreview+`
- `PrimitiveNode`
- `ImpactSimpleDetectorSEGS`
- `ImpactSEGSOrderedFilter`
- `SegsToCombinedMask`
- `ImpactSimpleDetectorSEGS`
- `MaskPreview+`
- `SegsToCombinedMask`
- `SegsToCombinedMask`
- `MaskPreview+`
- `SubtractMaskForEach`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `DetailerForEach`
- `Note`
- `Note`
- `CR Upscale Image`
- `ImageSharpen`
- `MaskPreview+`
- `Note`
- `BasicScheduler`
- `VAEDecode` ★核心
- `UltralyticsDetectorProvider`
- `Note`
- `KSamplerSelect` ★核心
- `EmptyLatentImage` ★核心
- `GlobalSeed //Inspire`
- `Note`
- `Note`
- `Note`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CR SDXL Aspect Ratio`
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `LoraLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `ImageApplyLUT+`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `more_details.safetensors`
- `strength_model` = `0.75`
- `strength_clip` = `1`
- `checkpoint` = `epicrealism_naturalSinRC1VAE.safetensors`

## 知识

覆盖率 **53%**（37/70）

**有卡**：`SegsToCombinedMask`、`MaskPreview+`、`ImpactSimpleDetectorSEGS`、`ImpactSEGSOrderedFilter`、`SubtractMaskForEach`、`CLIPTextEncode`、`SaveImage`、`DetailerForEach`、`CR Upscale Image`、`ImageSharpen`、`BasicScheduler`、`VAEDecode`、`UltralyticsDetectorProvider`、`KSamplerSelect`、`EmptyLatentImage`、`GlobalSeed //Inspire`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`CR SDXL Aspect Ratio`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`SAMLoader`、`LoraLoader`、`CheckpointLoaderSimple`、`ImageApplyLUT+`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage、GlobalSeed //Inspire、KSamplerSelect
