---
key: 图片生成/图生图/Vosr_2.0_极速高清修复_文本修复_一键4K图像_2102323097541107714.json
name: Vosr_2.0_极速高清修复_文本修复_一键4K图像_2102323097541107714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Vosr_2.0_极速高清修复_文本修复_一键4K图像_2102323097541107714.json
hash: a5f82217e387cb44
coverage: 0.777778
learned_at: 2026-10-15 22:25:32
nodes: [VOSR2ModelLoader, Int, SaveImage, VOSR2Upscale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Image Comparer (rgthree), EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/Vosr_2.0_极速高清修复_文本修复_一键4K图像_2102323097541107714.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Vosr_2.0_极速高清修复_文本修复_一键4K图像_2102323097541107714.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（9 个）：
- `VOSR2ModelLoader`
- `Int`
- `SaveImage`
- `VOSR2Upscale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Image Comparer (rgthree)`
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`VOSR2ModelLoader`、`Int`、`SaveImage`、`VOSR2Upscale`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`EmptyImage`

**用到的条目**：LoadImage、VOSR2Upscale、SaveImage、EmptyImage、Int、VOSR2ModelLoader、LayerUtility: ImageScaleByAspectRatio V2、sd15-t2i-basic
