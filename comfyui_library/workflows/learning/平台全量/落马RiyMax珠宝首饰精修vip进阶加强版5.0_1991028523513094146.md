---
key: 平台全量/落马RiyMax珠宝首饰精修vip进阶加强版5.0_1991028523513094146.json
name: 落马RiyMax珠宝首饰精修vip进阶加强版5.0_1991028523513094146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/落马RiyMax珠宝首饰精修vip进阶加强版5.0_1991028523513094146.json
hash: 33604680645732c3
coverage: 0.714286
learned_at: 2026-11-14 02:33:03
nodes: [SaveImage, SaveImage, PrimitiveNode, PrimitiveNode, Note, LoadImage, PrimitiveNode, INTConstant, InspyrenetRembg, Fast Groups Bypasser (rgthree), LayerUtility: CropByMask V2, JanusModelLoader, JanusImageUnderstanding, LayerUtility: ImageScaleByAspectRatio V2, MaskToImage, PreviewImage, InspyrenetRembgProcess, InspyrenetRembgLoader, MaskToImage, easy cleanGpuUsed, Image Comparer (rgthree), VAELoader, DualCLIPLoader, UNETLoader, LoraLoader, ModelSamplingFlux, workflow>核心模组, PreviewImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "F.1_RiyMax-ZhuBao_.safetensors", "strength_clip": 1, "strength_model": 0.6000000000000001}
---

# 平台全量/落马RiyMax珠宝首饰精修vip进阶加强版5.0_1991028523513094146.json

> 来源文件 `comfyui_library/workflows/平台全量/落马RiyMax珠宝首饰精修vip进阶加强版5.0_1991028523513094146.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（28 个）：
- `SaveImage`
- `SaveImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `Note`
- `LoadImage`
- `PrimitiveNode`
- `INTConstant`
- `InspyrenetRembg`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: CropByMask V2`
- `JanusModelLoader`
- `JanusImageUnderstanding`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskToImage`
- `PreviewImage`
- `InspyrenetRembgProcess`
- `InspyrenetRembgLoader`
- `MaskToImage`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `ModelSamplingFlux`
- `workflow>核心模组`
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `F.1_RiyMax-ZhuBao_.safetensors`
- `strength_model` = `0.6000000000000001`
- `strength_clip` = `1`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`SaveImage`、`LoadImage`、`INTConstant`、`InspyrenetRembg`、`LayerUtility: CropByMask V2`、`JanusModelLoader`、`JanusImageUnderstanding`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskToImage`、`InspyrenetRembgProcess`、`InspyrenetRembgLoader`、`easy cleanGpuUsed`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`LoraLoader`、`ModelSamplingFlux`、`workflow>核心模组`

**用到的条目**：VAELoader、UNETLoader、LoadImage、LoraLoader、LoRALoader、DualCLIPLoader、ModelSamplingFlux、SaveImage
