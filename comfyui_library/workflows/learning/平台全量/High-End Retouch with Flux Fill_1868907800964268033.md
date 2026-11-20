---
key: 平台全量/High-End Retouch with Flux Fill_1868907800964268033.json
name: High-End Retouch with Flux Fill_1868907800964268033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/High-End Retouch with Flux Fill_1868907800964268033.json
hash: 97095683d5b375ca
coverage: 0.647059
learned_at: 2026-11-14 00:32:03
nodes: [GetNode, SetNode, SimpleMathSlider+, SetNode, ConditioningZeroOut, FluxGuidance, KSampler, VAEDecode, GetNode, GetNode, StringFunction|pysssss, SetNode, SetNode, GetNode, SetNode, Lora Loader, Any Switch (rgthree), CLIPTextEncode, Any Switch (rgthree), GetNode, InpaintModelConditioning, GetNode, InpaintStitch, Label (rgthree), Label (rgthree), SetNode, GetNode, ttN text, Fast Bypasser (rgthree), Label (rgthree), Label (rgthree), SetNode, InpaintCrop, Get Image Size, SimpleMathInt+, Bookmark (rgthree), SimpleMathInt+, SimpleMath+, SimpleMath+, SimpleComparison+, SimpleMath+, SimpleCondition+, SimpleMathInt+, SimpleMathInt+, SimpleMath+, DisplayAny, SimpleComparison+, SetNode, SimpleCondition+, GetNode, GetNode, MaskToImage, GetNode, MaskComposite, GroundingDinoSAMSegment (segment anything), GetNode, GroundingDinoModelLoader (segment anything), ImageToMask, GetImageSize+, SetNode, Any Switch (rgthree), SolidMask, MaskComposite, MaskComposite, MaskPreview+, SetNode, LoadImage, LayerMask: MaskGrow, Note, LayerMask: PersonMaskUltra V2, Fast Groups Bypasser (rgthree), GetNode, UNETLoader, VAELoader, DualCLIPLoader, InpaintResize, SAMModelLoader (segment anything), GetNode, MaskComposite, LayerMask: PersonMaskUltra V2, APersonMaskGenerator, CR Simple Image Compare, SaveImage, PreviewImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1.01, "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 20}
---

# 平台全量/High-End Retouch with Flux Fill_1868907800964268033.json

> 来源文件 `comfyui_library/workflows/平台全量/High-End Retouch with Flux Fill_1868907800964268033.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `GetNode`
- `SetNode`
- `SimpleMathSlider+`
- `SetNode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `StringFunction|pysssss`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Lora Loader`
- `Any Switch (rgthree)`
- `CLIPTextEncode` ★核心
- `Any Switch (rgthree)`
- `GetNode`
- `InpaintModelConditioning`
- `GetNode`
- `InpaintStitch`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `GetNode`
- `ttN text`
- `Fast Bypasser (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `InpaintCrop`
- `Get Image Size`
- `SimpleMathInt+`
- `Bookmark (rgthree)`
- `SimpleMathInt+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleComparison+`
- `SimpleMath+`
- `SimpleCondition+`
- `SimpleMathInt+`
- `SimpleMathInt+`
- `SimpleMath+`
- `DisplayAny`
- `SimpleComparison+`
- `SetNode`
- `SimpleCondition+`
- `GetNode`
- `GetNode`
- `MaskToImage`
- `GetNode`
- `MaskComposite`
- `GroundingDinoSAMSegment (segment anything)`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `ImageToMask`
- `GetImageSize+`
- `SetNode`
- `Any Switch (rgthree)`
- `SolidMask`
- `MaskComposite`
- `MaskComposite`
- `MaskPreview+`
- `SetNode`
- `LoadImage`
- `LayerMask: MaskGrow`
- `Note`
- `LayerMask: PersonMaskUltra V2`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `InpaintResize`
- `SAMModelLoader (segment anything)`
- `GetNode`
- `MaskComposite`
- `LayerMask: PersonMaskUltra V2`
- `APersonMaskGenerator`
- `CR Simple Image Compare`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `0`
- `steps` = `20`
- `cfg` = `1.01`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **65%**（55/85）

**有卡**：`SimpleMathSlider+`、`ConditioningZeroOut`、`FluxGuidance`、`KSampler`、`VAEDecode`、`StringFunction|pysssss`、`Lora Loader`、`CLIPTextEncode`、`InpaintModelConditioning`、`InpaintStitch`、`Label (rgthree)`、`ttN text`、`Fast Bypasser (rgthree)`、`InpaintCrop`、`Get Image Size`、`SimpleMathInt+`、`Bookmark (rgthree)`、`SimpleMath+`、`SimpleComparison+`、`SimpleCondition+`、`DisplayAny`、`MaskToImage`、`MaskComposite`、`GroundingDinoSAMSegment (segment anything)`、`GroundingDinoModelLoader (segment anything)`、`ImageToMask`、`GetImageSize+`、`SolidMask`、`MaskPreview+`、`LoadImage`、`LayerMask: MaskGrow`、`LayerMask: PersonMaskUltra V2`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`InpaintResize`、`SAMModelLoader (segment anything)`、`APersonMaskGenerator`、`CR Simple Image Compare`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
