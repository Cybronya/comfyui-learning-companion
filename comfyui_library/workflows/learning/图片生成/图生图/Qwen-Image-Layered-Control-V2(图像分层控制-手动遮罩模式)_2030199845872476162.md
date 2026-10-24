---
key: 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手动遮罩模式)_2030199845872476162.json
name: Qwen-Image-Layered-Control-V2(图像分层控制-手动遮罩模式)_2030199845872476162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手动遮罩模式)_2030199845872476162.json
hash: 6d17f3c9df53534a
coverage: 0.727273
learned_at: 2026-10-23 11:17:13
nodes: [PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LayeredControlV2Sampler, LoadLayeredControlV2Pipe, SaveImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手动遮罩模式)_2030199845872476162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-手动遮罩模式)_2030199845872476162.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（11 个）：
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LayeredControlV2Sampler` ★核心
- `LoadLayeredControlV2Pipe`
- `SaveImage`
- `SaveImage`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LayeredControlV2Sampler`、`LoadLayeredControlV2Pipe`、`SaveImage`

**用到的条目**：LoadImage、LayeredControlV2Sampler、SaveImage、LayerUtility: ImageScaleByAspectRatio V2、LoadLayeredControlV2Pipe、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
