---
key: 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-提示词控制)_2030210973105135617.json
name: Qwen-Image-Layered-Control-V2(图像分层控制-提示词控制)_2030210973105135617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-提示词控制)_2030210973105135617.json
hash: 31d99af3f7c9d76b
coverage: 0.8
learned_at: 2026-10-23 11:17:13
nodes: [SaveImage, SaveImage, PreviewImage, PreviewImage, LoadLayeredControlV2Pipe, LoadImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayeredControlV2Sampler, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-提示词控制)_2030210973105135617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Layered-Control-V2(图像分层控制-提示词控制)_2030210973105135617.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（10 个）：
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `LoadLayeredControlV2Pipe`
- `LoadImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayeredControlV2Sampler` ★核心
- `CR Prompt Text`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`SaveImage`、`LoadLayeredControlV2Pipe`、`LoadImage`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayeredControlV2Sampler`、`CR Prompt Text`

**用到的条目**：LoadImage、LayeredControlV2Sampler、CR Prompt Text、SaveImage、JWInteger、LayerUtility: ImageScaleByAspectRatio V2、LoadLayeredControlV2Pipe、sd15-t2i-basic
