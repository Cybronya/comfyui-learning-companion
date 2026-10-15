---
key: 图片生成/图生图/Vosr 2.0_极速高清修复_文本修复_一键4K图像_2097239382121078785.json
name: Vosr 2.0_极速高清修复_文本修复_一键4K图像_2097239382121078785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Vosr 2.0_极速高清修复_文本修复_一键4K图像_2097239382121078785.json
hash: d3e9d1b9afc86a86
coverage: 0.857143
learned_at: 2026-10-15 22:25:32
nodes: [VOSR2ModelLoader, Int, SaveImage, VOSR2Upscale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Vosr 2.0_极速高清修复_文本修复_一键4K图像_2097239382121078785.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Vosr 2.0_极速高清修复_文本修复_一键4K图像_2097239382121078785.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（7 个）：
- `VOSR2ModelLoader`
- `Int`
- `SaveImage`
- `VOSR2Upscale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`VOSR2ModelLoader`、`Int`、`SaveImage`、`VOSR2Upscale`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoadImage、VOSR2Upscale、SaveImage、Int、VOSR2ModelLoader、LayerUtility: ImageScaleByAspectRatio V2、sd15-t2i-basic、sd15-t2i-lora
