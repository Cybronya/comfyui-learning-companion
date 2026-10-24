---
key: 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红色保留）_2030193673991888898.json
name: Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红色保留）_2030193673991888898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红色保留）_2030193673991888898.json
hash: ef46f8f76821e237
coverage: 0.7
learned_at: 2026-10-23 11:17:13
nodes: [SaveImage, SaveImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, LoadLayeredControlV2Pipe, Mask To Image (mtb), LayeredControlV2Sampler]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红色保留）_2030193673991888898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手画遮罩模式-红色保留）_2030193673991888898.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（10 个）：
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `LoadLayeredControlV2Pipe`
- `Mask To Image (mtb)`
- `LayeredControlV2Sampler` ★核心

## 知识

覆盖率 **70%**（7/10）

**有卡**：`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LoadLayeredControlV2Pipe`、`Mask To Image (mtb)`、`LayeredControlV2Sampler`

**用到的条目**：LoadImage、LayeredControlV2Sampler、SaveImage、LayerUtility: ImageScaleByAspectRatio V2、Mask To Image (mtb)、LoadLayeredControlV2Pipe、sd15-t2i-basic、sd15-t2i-lora
