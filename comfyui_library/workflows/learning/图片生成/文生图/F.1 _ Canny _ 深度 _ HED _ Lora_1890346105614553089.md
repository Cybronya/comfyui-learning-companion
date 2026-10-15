---
key: 图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json
name: F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json
hash: aeeb595963ccdffd
coverage: 0.474576
learned_at: 2026-10-10 20:58:30
nodes: [CLIPTextEncodeFlux, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VAEDecode, VAELoader, SaveImage, PreviewImage, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, PreviewImage, VAELoader, SaveImage, VAEDecode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CannyEdgePreprocessor, PreviewImage, VAELoader, VAEDecode, SaveImage, HEDPreprocessor, Reroute, Reroute, Reroute, Reroute, EmptyLatentImage, ApplyFluxControlNet, XlabsSampler, ApplyFluxControlNet, XlabsSampler, ApplyFluxControlNet, XlabsSampler, PreviewImage, PreviewImage, CLIPTextEncodeFlux, LoadImage, LoraLoader, DualCLIPLoader, UNETLoader, DepthAnythingV2Preprocessor, LoadFluxControlNet, LoadFluxControlNet, LoadFluxControlNet]
patterns: [lora]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "height": 1024, "lora_name": "精致古装.safetensors", "strength_clip": 1, "strength_model": 0.8, "width": 1024}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json`

## 结构

**节点**（59 个）：
- `CLIPTextEncodeFlux`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VAEDecode`
- `VAELoader`
- `SaveImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `VAELoader`
- `SaveImage`
- `VAEDecode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CannyEdgePreprocessor`
- `PreviewImage`
- `VAELoader`
- `VAEDecode`
- `SaveImage`
- `HEDPreprocessor`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `EmptyLatentImage`
- `ApplyFluxControlNet`
- `XlabsSampler`
- `ApplyFluxControlNet`
- `XlabsSampler`
- `ApplyFluxControlNet`
- `XlabsSampler`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncodeFlux`
- `LoadImage`
- `LoraLoader`
- `DualCLIPLoader`
- `UNETLoader`
- `DepthAnythingV2Preprocessor`
- `LoadFluxControlNet`
- `LoadFluxControlNet`
- `LoadFluxControlNet`

**识别到的模式**：lora

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `lora_name` = `精致古装.safetensors`
- `strength_clip` = `1`
- `strength_model` = `0.8`
- `width` = `1024`

## 知识

覆盖率 **47%**（28/59）

**有卡**：`CLIPTextEncodeFlux`、`LayerUtility: ImageScaleByAspectRatio V2`、`PreviewImage`、`VAEDecode`、`VAELoader`、`SaveImage`、`Reroute`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
