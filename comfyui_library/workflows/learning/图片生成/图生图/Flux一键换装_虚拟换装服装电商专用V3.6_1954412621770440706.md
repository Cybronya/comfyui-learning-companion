---
key: 图片生成/图生图/Flux一键换装_虚拟换装服装电商专用V3.6_1954412621770440706.json
name: Flux一键换装_虚拟换装服装电商专用V3.6_1954412621770440706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux一键换装_虚拟换装服装电商专用V3.6_1954412621770440706.json
hash: 6c7d790ab2dcc81f
coverage: 0.77551
learned_at: 2026-10-23 11:01:52
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, ImageToMask, LoadImage, LoadImage, Reroute, EmptyImage, Reroute, Reroute, Reroute, Reroute, Int, Note, easy imageSize, InpaintStitch, Reroute, Note, LayerUtility: ImageScaleByAspectRatio V2, ImageCrop+, SaveImage, FluxGuidance, DifferentialDiffusion, VAEDecode, ConditioningZeroOut, Reroute, CLIPTextEncode, InpaintModelConditioning, Reroute, SaveImage, LoraLoader, Reroute, ImageConcanate, easy imageSize, ImageCrop, MathExpression|pysssss, MathExpression|pysssss, easy imageSize, ImageResizeKJ, ImageCrop, MathExpression|pysssss, MathExpression|pysssss, easy imageSize, ImageResizeKJ, easy imageSize, MathExpression|pysssss, MathExpression|pysssss, easy imageSize, MathExpression|pysssss, MaskToImage, easy imageSize, ImageCrop, PreviewImage, GrowMaskWithBlur, FeatheredMask, MaskToImage, Image Filter Adjustments, ImageConcanate, LayerMask: SegformerB2ClothesUltra, InspyrenetRembgAdvanced, ImageCompositeMasked, easy imageSize, easy imageSize, CLIPVisionEncode, StyleModelApply, ImageToMask, MaskToImage, easy imageSize, AddMask, PreviewImage, PreviewImage, GrowMaskWithBlur, FeatheredMask, MaskToImage, Image Filter Adjustments, MaskToImage, easy imageSize, MaskToImage, easy imageSize, ImageConcanate, ImageToMask, InpaintCrop, easy imageSize, MaskToImage, ImageResizeKJ, PreviewImage, Note, PreviewImage, VAELoader, CLIPTextEncode, UNETLoader, LoraLoader, DualCLIPLoader, StyleModelLoader, CLIPVisionLoader, KSampler]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "xiaoza-catvton-flux-lora-alpha_alpha.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 410402296162029, "steps": 25, "strength_clip": 0.8, "strength_model": 0.7}
---

# 图片生成/图生图/Flux一键换装_虚拟换装服装电商专用V3.6_1954412621770440706.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux一键换装_虚拟换装服装电商专用V3.6_1954412621770440706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageToMask`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `EmptyImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Note`
- `easy imageSize`
- `InpaintStitch`
- `Reroute`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCrop+`
- `SaveImage`
- `FluxGuidance`
- `DifferentialDiffusion`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `Reroute`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `Reroute`
- `SaveImage`
- `LoraLoader` ★核心
- `Reroute`
- `ImageConcanate`
- `easy imageSize`
- `ImageCrop`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy imageSize`
- `ImageResizeKJ`
- `ImageCrop`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy imageSize`
- `ImageResizeKJ`
- `easy imageSize`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy imageSize`
- `MathExpression|pysssss`
- `MaskToImage`
- `easy imageSize`
- `ImageCrop`
- `PreviewImage`
- `GrowMaskWithBlur`
- `FeatheredMask`
- `MaskToImage`
- `Image Filter Adjustments`
- `ImageConcanate`
- `LayerMask: SegformerB2ClothesUltra`
- `InspyrenetRembgAdvanced`
- `ImageCompositeMasked`
- `easy imageSize`
- `easy imageSize`
- `CLIPVisionEncode`
- `StyleModelApply`
- `ImageToMask`
- `MaskToImage`
- `easy imageSize`
- `AddMask`
- `PreviewImage`
- `PreviewImage`
- `GrowMaskWithBlur`
- `FeatheredMask`
- `MaskToImage`
- `Image Filter Adjustments`
- `MaskToImage`
- `easy imageSize`
- `MaskToImage`
- `easy imageSize`
- `ImageConcanate`
- `ImageToMask`
- `InpaintCrop`
- `easy imageSize`
- `MaskToImage`
- `ImageResizeKJ`
- `PreviewImage`
- `Note`
- `PreviewImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `KSampler` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `xiaoza-catvton-flux-lora-alpha_alpha.safetensors`
- `strength_model` = `0.7`
- `strength_clip` = `0.8`
- `seed` = `410402296162029`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（76/98）

**有卡**：`ImageToMask`、`LoadImage`、`EmptyImage`、`Int`、`easy imageSize`、`InpaintStitch`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCrop+`、`SaveImage`、`FluxGuidance`、`DifferentialDiffusion`、`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncode`、`InpaintModelConditioning`、`LoraLoader`、`ImageConcanate`、`ImageCrop`、`MathExpression|pysssss`、`ImageResizeKJ`、`MaskToImage`、`GrowMaskWithBlur`、`FeatheredMask`、`Image Filter Adjustments`、`LayerMask: SegformerB2ClothesUltra`、`InspyrenetRembgAdvanced`、`ImageCompositeMasked`、`CLIPVisionEncode`、`StyleModelApply`、`AddMask`、`InpaintCrop`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`StyleModelLoader`、`CLIPVisionLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
