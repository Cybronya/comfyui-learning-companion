---
key: 图片生成/文生图/PuLID + Pose CN 2.0_1914263520249114625.json
name: PuLID + Pose CN 2.0_1914263520249114625.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/PuLID + Pose CN 2.0_1914263520249114625.json
hash: 1c9d15a33cdb4b8c
coverage: 0.629032
learned_at: 2026-10-07 19:46:18
nodes: [CLIPTextEncodeFlux, CLIPTextEncode, PreviewImage, SetShakkerLabsUnionControlNetType, LoraLoader, ControlNetLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, FaceAnalysisModels, PreviewImage, GrowMaskWithBlur, preview_mask, PreviewImage, LoraLoader, PulidFluxModelLoader, FaceBoundingBox, LayerMask: PersonMaskUltra V2, GetImageSize, VAEDecode, VAEDecode, ControlNetApplyAdvanced, VAELoader, EmptyLatentImage, DWPreprocessor, easy cleanGpuUsed, ApplyPulidFlux, Reroute, Reroute, Reroute, Reroute, Reroute, KSampler, VAEDecode, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, Reroute, KSampler, easy cleanGpuUsed, KSampler, easy cleanGpuUsed, LoadImage, LoadImage, SaveImage, SaveImage, SaveImage, SaveImage, ShowText|pysssss, LoadImage, RH_Captioner, TextInput_, Text Concatenate (JPS), KSampler, RH_Captioner, Fast Groups Bypasser (rgthree), ConstrainImage|pysssss, UNETLoader, DualCLIPLoader]
patterns: [text_to_image, lora]
missing: [ConstrainImage|pysssss, LayerMask: PersonMaskUltra V2, Text Concatenate (JPS), easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.7000000000000001, "denoise": 1, "height": 1536, "lora_name": "爱妃Zhang Yuxi.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 62239091599981, "steps": 20, "strength_clip": 1, "strength_model": 0.6, "width": 1024}
discoveries: [次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/PuLID + Pose CN 2.0_1914263520249114625.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1914263520249114625.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `SetShakkerLabsUnionControlNetType`
- `LoraLoader` ★核心
- `ControlNetLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `FaceAnalysisModels`
- `PreviewImage`
- `GrowMaskWithBlur`
- `preview_mask`
- `PreviewImage`
- `LoraLoader` ★核心
- `PulidFluxModelLoader`
- `FaceBoundingBox`
- `LayerMask: PersonMaskUltra V2`
- `GetImageSize`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `DWPreprocessor`
- `easy cleanGpuUsed`
- `ApplyPulidFlux`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `ShowText|pysssss`
- `LoadImage`
- `RH_Captioner`
- `TextInput_`
- `Text Concatenate (JPS)`
- `KSampler` ★核心
- `RH_Captioner`
- `Fast Groups Bypasser (rgthree)`
- `ConstrainImage|pysssss`
- `UNETLoader` ★核心
- `DualCLIPLoader`

**识别到的模式**：text_to_image、lora

## 关键参数

- `lora_name` = `爱妃Zhang Yuxi.safetensors`
- `strength_model` = `0.6`
- `strength_clip` = `1`
- `controlnet_strength` = `0.7000000000000001`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `62239091599981`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（39/62）

**有卡**：`CLIPTextEncodeFlux`、`CLIPTextEncode`、`SetShakkerLabsUnionControlNetType`、`LoraLoader`、`ControlNetLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`FaceAnalysisModels`、`GrowMaskWithBlur`、`preview_mask`、`PulidFluxModelLoader`、`FaceBoundingBox`、`GetImageSize`、`VAEDecode`、`ControlNetApplyAdvanced`、`VAELoader`、`EmptyLatentImage`、`DWPreprocessor`、`ApplyPulidFlux`、`KSampler`、`LoadImage`、`SaveImage`、`RH_Captioner`、`TextInput_`、`UNETLoader`、`DualCLIPLoader`

**缺卡**（8）：`ConstrainImage|pysssss`、`LayerMask: PersonMaskUltra V2`、`Text Concatenate (JPS)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced

## 学习发现

- 次要节点 `ConstrainImage|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
