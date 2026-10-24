---
key: 图片生成/图生图/✅Flux.1 fill OneReward 扩图，外扩-贴回原图_1966574973043290113.json
name: ✅Flux.1 fill OneReward 扩图，外扩-贴回原图_1966574973043290113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/✅Flux.1 fill OneReward 扩图，外扩-贴回原图_1966574973043290113.json
hash: 098aa0cf427fde9e
coverage: 0.544118
learned_at: 2026-10-23 11:47:40
nodes: [ConditioningZeroOut, CLIPTextEncode, VAELoader, CLIPTextEncode, SetNode, GetNode, SetNode, LoadJanusModel, SetNode, easy cleanGpuUsed, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, FluxGuidance, GetNode, GetNode, SetNode, GetNode, VAEDecode, GetNode, PreviewImage, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, RepeatLatentBatch, RebatchLatents, GetNode, CR Text, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerMask: MaskPreview, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, NunchakuTextEncoderLoaderV2, GetNode, GetNode, PreviewImage, PreviewImage, CR Text Concatenate, ShowText|pysssss, ImagePadForOutpaintMasked, InpaintExtendOutpaint, PrimitiveFloat, SetNode, UNETLoader, SetNode, SetNode, JanusImage2Text, Image Comparer (rgthree), ImpactSwitch, LayerUtility: ImageScaleRestore V2, JoinImageWithAlpha, GetNode, InpaintModelConditioning, LoadImage, Int, ImpactSwitch, LayerUtility: RestoreCropBox, DifferentialDiffusion, SetNode, LoraLoaderModelOnly, KSampler, EasyCache, ImagePadForOutpaintTargetSize, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 851790835830000, "steps": 20}
---

# 图片生成/图生图/✅Flux.1 fill OneReward 扩图，外扩-贴回原图_1966574973043290113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/✅Flux.1 fill OneReward 扩图，外扩-贴回原图_1966574973043290113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadJanusModel`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FluxGuidance`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatLatentBatch`
- `RebatchLatents`
- `GetNode`
- `CR Text`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerMask: MaskPreview`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `NunchakuTextEncoderLoaderV2`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `CR Text Concatenate`
- `ShowText|pysssss`
- `ImagePadForOutpaintMasked`
- `InpaintExtendOutpaint`
- `PrimitiveFloat`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `JanusImage2Text`
- `Image Comparer (rgthree)`
- `ImpactSwitch`
- `LayerUtility: ImageScaleRestore V2`
- `JoinImageWithAlpha`
- `GetNode`
- `InpaintModelConditioning`
- `LoadImage`
- `Int`
- `ImpactSwitch`
- `LayerUtility: RestoreCropBox`
- `DifferentialDiffusion`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EasyCache`
- `ImagePadForOutpaintTargetSize`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `851790835830000`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **54%**（37/68）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`VAELoader`、`LoadJanusModel`、`easy cleanGpuUsed`、`FluxGuidance`、`VAEDecode`、`LayerMask: MaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatLatentBatch`、`RebatchLatents`、`CR Text`、`LayerMask: MaskGrow`、`LayerUtility: CropByMask V2`、`NunchakuTextEncoderLoaderV2`、`CR Text Concatenate`、`ImagePadForOutpaintMasked`、`InpaintExtendOutpaint`、`UNETLoader`、`JanusImage2Text`、`LayerUtility: ImageScaleRestore V2`、`JoinImageWithAlpha`、`InpaintModelConditioning`、`LoadImage`、`Int`、`LayerUtility: RestoreCropBox`、`DifferentialDiffusion`、`LoraLoaderModelOnly`、`KSampler`、`EasyCache`、`ImagePadForOutpaintTargetSize`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
