---
key: 平台全量/Flux.1-Fill-OneRewar一键完美换装_1959869784093569026.json
name: Flux.1-Fill-OneRewar一键完美换装_1959869784093569026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1-Fill-OneRewar一键完美换装_1959869784093569026.json
hash: 1d363a4df511e07f
coverage: 0.819444
learned_at: 2026-11-14 00:28:49
nodes: [PreviewImage, LayerUtility: CropByMask V2, LayerUtility: TextJoin, InpaintModelConditioning, PreviewImage, LayerUtility: PurgeVRAM, MaskToImage, FluxGuidance, MaskToImage, MaskPreview+, RH_LLMAPI_NODE, ShowText|pysssss, ImageCrop+, VAEDecode, LoraLoaderModelOnly, ImageToMask, GrowMask, CR Text, InpaintModelConditioning, easy compare, easy compare, PreviewImage, CLIPTextEncode, ConditioningZeroOut, InpaintStitch, SaveImage, StyleModelLoader, CLIPVisionLoader, ReduxPromptStyler, PreviewImage, KSampler, KSampler, Int Literal, LoraLoaderModelOnly, Anything Everywhere3, PreviewImage, PreviewImage, VAEDecode, VAELoader, InpaintResize, InpaintCrop, ImageAndMaskPreview, easy makeImageForICLora, Int Literal, PreviewImage, MaskPreview+, Image Comparer (rgthree), CR Text, LayerMask: SegformerB2ClothesUltra, ShowText|pysssss, easy compare, easy compare, easy compare, CR Text, CR Text, CR Text, LoraLoaderModelOnly, Mask Fill Holes, LoadAndResizeImage, RH_LLMAPI_NODE, LayerMask: SegmentAnythingUltra V2, LoraLoaderModelOnly, DualCLIPLoader, Note, ImageMaskSwitch, Int Literal, LayerUtility: ImageRemoveAlpha, LayerUtility: ColorPicker, UNETLoader, LoadImage, CR Text, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 11454284801068, "steps": 25}
---

# 平台全量/Flux.1-Fill-OneRewar一键完美换装_1959869784093569026.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1-Fill-OneRewar一键完美换装_1959869784093569026.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: TextJoin`
- `InpaintModelConditioning`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `MaskToImage`
- `FluxGuidance`
- `MaskToImage`
- `MaskPreview+`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `ImageCrop+`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageToMask`
- `GrowMask`
- `CR Text`
- `InpaintModelConditioning`
- `easy compare`
- `easy compare`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `InpaintStitch`
- `SaveImage`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `ReduxPromptStyler`
- `PreviewImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `Int Literal`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAELoader`
- `InpaintResize`
- `InpaintCrop`
- `ImageAndMaskPreview`
- `easy makeImageForICLora`
- `Int Literal`
- `PreviewImage`
- `MaskPreview+`
- `Image Comparer (rgthree)`
- `CR Text`
- `LayerMask: SegformerB2ClothesUltra`
- `ShowText|pysssss`
- `easy compare`
- `easy compare`
- `easy compare`
- `CR Text`
- `CR Text`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `Mask Fill Holes`
- `LoadAndResizeImage`
- `RH_LLMAPI_NODE`
- `LayerMask: SegmentAnythingUltra V2`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `Note`
- `ImageMaskSwitch`
- `Int Literal`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ColorPicker`
- `UNETLoader` ★核心
- `LoadImage`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `11454284801068`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **82%**（59/72）

**有卡**：`LayerUtility: CropByMask V2`、`LayerUtility: TextJoin`、`InpaintModelConditioning`、`LayerUtility: PurgeVRAM`、`MaskToImage`、`FluxGuidance`、`MaskPreview+`、`RH_LLMAPI_NODE`、`ImageCrop+`、`VAEDecode`、`LoraLoaderModelOnly`、`ImageToMask`、`GrowMask`、`CR Text`、`easy compare`、`CLIPTextEncode`、`ConditioningZeroOut`、`InpaintStitch`、`SaveImage`、`StyleModelLoader`、`CLIPVisionLoader`、`ReduxPromptStyler`、`KSampler`、`Int Literal`、`VAELoader`、`InpaintResize`、`InpaintCrop`、`ImageAndMaskPreview`、`easy makeImageForICLora`、`LayerMask: SegformerB2ClothesUltra`、`Mask Fill Holes`、`LoadAndResizeImage`、`LayerMask: SegmentAnythingUltra V2`、`DualCLIPLoader`、`ImageMaskSwitch`、`LayerUtility: ImageRemoveAlpha`、`LayerUtility: ColorPicker`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
