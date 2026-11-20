---
key: 平台全量/high quaility face swaping_1878643729715339266.json
name: high quaility face swaping_1878643729715339266
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/high quaility face swaping_1878643729715339266.json
hash: 33ba5078476fd80a
coverage: 0.764706
learned_at: 2026-11-14 01:12:27
nodes: [VAEEncode, VAEDecode, SetNode, SetNode, Anything Everywhere?, GetNode, GetNode, LoadImage, LoadImage, SetNode, UnetLoaderGGUF, SetNode, Anything Everywhere, GetImageSize+, ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PreviewImage, GetNode, MaskBlur+, SimpleMathInt+, ConstrainImage|pysssss, Node Collector (rgthree), SimpleMathInt+, SimpleMathInt+, SimpleMathInt+, Any Switch (rgthree), SetNode, SetNode, ImageResize+, easy cleanGpuUsed, SimpleMathInt+, SetLatentNoiseMask, GetNode, VAEEncode, CLIPTextEncode, ConditioningZeroOut, ModelSamplingFlux, GetNode, ApplyPulidFlux, ToBasicPipe, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SimpleCondition+, GetNode, SimpleMath+, SimpleMathInt+, SimpleMathInt+, SimpleMathInt+, easy cleanGpuUsed, easy cleanGpuUsed, ConstrainImage|pysssss, ImageUpscaleWithModel, UpscaleModelLoader, easy cleanGpuUsed, ConditioningZeroOut, SimpleComparison+, SimpleCondition+, VAEDecode, Label (rgthree), PulidFluxModelLoader, ControlNetInpaintingAliMamaApply, easy seed, FaceBoundingBox, FaceAnalysisModels, GetNode, GrowMask, LayerMask: PersonMaskUltra, ImageComposite+, LoadImage, ImageResize+, KSampler, KSampler, FluxGuidance, easy humanSegmentation, SimpleMathInt+, SimpleMathInt+, SimpleCondition+, GrowMask, Label (rgthree), ControlNetLoader, Miaoshouai_Tagger, VAELoader, GetNode, FluxGuidance, CLIPTextEncode, Miaoshouai_Tagger, DualCLIPLoaderGGUF, SetNode, Fast Bypasser (rgthree), LoadImage, SaveImage, GetNode, PreviewImage, easy humanSegmentation, MaskDetailerPipe]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.4, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 344930377200708, "steps": 15}
---

# 平台全量/high quaility face swaping_1878643729715339266.json

> 来源文件 `comfyui_library/workflows/平台全量/high quaility face swaping_1878643729715339266.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `Anything Everywhere?`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `UnetLoaderGGUF` ★核心
- `SetNode`
- `Anything Everywhere`
- `GetImageSize+`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PreviewImage`
- `GetNode`
- `MaskBlur+`
- `SimpleMathInt+`
- `ConstrainImage|pysssss`
- `Node Collector (rgthree)`
- `SimpleMathInt+`
- `SimpleMathInt+`
- `SimpleMathInt+`
- `Any Switch (rgthree)`
- `SetNode`
- `SetNode`
- `ImageResize+`
- `easy cleanGpuUsed`
- `SimpleMathInt+`
- `SetLatentNoiseMask`
- `GetNode`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ModelSamplingFlux`
- `GetNode`
- `ApplyPulidFlux`
- `ToBasicPipe`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SimpleCondition+`
- `GetNode`
- `SimpleMath+`
- `SimpleMathInt+`
- `SimpleMathInt+`
- `SimpleMathInt+`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ConstrainImage|pysssss`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `SimpleComparison+`
- `SimpleCondition+`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `PulidFluxModelLoader`
- `ControlNetInpaintingAliMamaApply`
- `easy seed`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `GetNode`
- `GrowMask`
- `LayerMask: PersonMaskUltra`
- `ImageComposite+`
- `LoadImage`
- `ImageResize+`
- `KSampler` ★核心
- `KSampler` ★核心
- `FluxGuidance`
- `easy humanSegmentation`
- `SimpleMathInt+`
- `SimpleMathInt+`
- `SimpleCondition+`
- `GrowMask`
- `Label (rgthree)`
- `ControlNetLoader`
- `Miaoshouai_Tagger`
- `VAELoader`
- `GetNode`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `Miaoshouai_Tagger`
- `DualCLIPLoaderGGUF`
- `SetNode`
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `SaveImage`
- `GetNode`
- `PreviewImage`
- `easy humanSegmentation`
- `MaskDetailerPipe`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `344930377200708`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.4`

## 知识

覆盖率 **76%**（78/102）

**有卡**：`VAEEncode`、`VAEDecode`、`Anything Everywhere?`、`LoadImage`、`UnetLoaderGGUF`、`GetImageSize+`、`ImageConcatMulti`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`MaskBlur+`、`SimpleMathInt+`、`ConstrainImage|pysssss`、`Node Collector (rgthree)`、`ImageResize+`、`easy cleanGpuUsed`、`SetLatentNoiseMask`、`CLIPTextEncode`、`ConditioningZeroOut`、`ModelSamplingFlux`、`ApplyPulidFlux`、`ToBasicPipe`、`Label (rgthree)`、`SimpleCondition+`、`SimpleMath+`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`SimpleComparison+`、`PulidFluxModelLoader`、`ControlNetInpaintingAliMamaApply`、`easy seed`、`FaceBoundingBox`、`FaceAnalysisModels`、`GrowMask`、`LayerMask: PersonMaskUltra`、`ImageComposite+`、`KSampler`、`FluxGuidance`、`easy humanSegmentation`、`ControlNetLoader`、`Miaoshouai_Tagger`、`VAELoader`、`DualCLIPLoaderGGUF`、`Fast Bypasser (rgthree)`、`SaveImage`、`MaskDetailerPipe`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader
