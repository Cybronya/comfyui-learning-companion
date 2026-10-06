---
key: 图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json
name: F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json
hash: aeeb595963ccdffd
coverage: 0.457627
learned_at: 2026-10-07 03:04:57
nodes: [CLIPTextEncodeFlux, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VAEDecode, VAELoader, SaveImage, PreviewImage, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, PreviewImage, VAELoader, SaveImage, VAEDecode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CannyEdgePreprocessor, PreviewImage, VAELoader, VAEDecode, SaveImage, HEDPreprocessor, Reroute, Reroute, Reroute, Reroute, EmptyLatentImage, ApplyFluxControlNet, XlabsSampler, ApplyFluxControlNet, XlabsSampler, ApplyFluxControlNet, XlabsSampler, PreviewImage, PreviewImage, CLIPTextEncodeFlux, LoadImage, LoraLoader, DualCLIPLoader, UNETLoader, DepthAnythingV2Preprocessor, LoadFluxControlNet, LoadFluxControlNet, LoadFluxControlNet]
patterns: [lora]
missing: [HEDPreprocessor, LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "height": 1024, "lora_name": "精致古装.safetensors", "strength_clip": 1, "strength_model": 0.8, "width": 1024}
discoveries: [次要节点 `HEDPreprocessor` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `CLIPTextEncodeFlux` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VAEDecode` ★核心
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
- `VAEDecode` ★核心
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
- `VAEDecode` ★核心
- `SaveImage`
- `HEDPreprocessor`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `EmptyLatentImage` ★核心
- `ApplyFluxControlNet`
- `XlabsSampler` ★核心
- `ApplyFluxControlNet`
- `XlabsSampler` ★核心
- `ApplyFluxControlNet`
- `XlabsSampler` ★核心
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncodeFlux` ★核心
- `LoadImage`
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `DepthAnythingV2Preprocessor`
- `LoadFluxControlNet`
- `LoadFluxControlNet`
- `LoadFluxControlNet`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `精致古装.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **46%**（27/59）

**有卡**：`CLIPTextEncodeFlux`、`VAEDecode`、`VAELoader`、`SaveImage`、`CannyEdgePreprocessor`、`EmptyLatentImage`、`ApplyFluxControlNet`、`XlabsSampler`、`LoadImage`、`LoraLoader`、`DualCLIPLoader`、`UNETLoader`、`DepthAnythingV2Preprocessor`、`LoadFluxControlNet`

**缺卡**（2）：`HEDPreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、EmptyLatentImage、LoadImage、DepthAnythingV2Preprocessor、ApplyFluxControlNet、CannyEdgePreprocessor

## 学习发现

- 次要节点 `HEDPreprocessor` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
