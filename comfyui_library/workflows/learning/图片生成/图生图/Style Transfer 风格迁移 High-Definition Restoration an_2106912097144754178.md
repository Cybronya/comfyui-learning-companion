---
key: 图片生成/图生图/Style Transfer 风格迁移 High-Definition Restoration an_2106912097144754178.json
name: Style Transfer 风格迁移 High-Definition Restoration an_2106912097144754178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Style Transfer 风格迁移 High-Definition Restoration an_2106912097144754178.json
hash: bb38c589f7043390
coverage: 0.92
learned_at: 2026-10-21 00:44:34
nodes: [PainterFluxImageEdit, easy cleanGpuUsed, CLIPLoader, GetImageSize, VAEDecode, VAELoader, workflow>自定义采样器, MuyeTextEditOutput, MuyeTextEditOutput, LoraLoaderModelOnly, SaveImage, easy textIndexSwitch, UNETLoader, GetImageSize, ImageScaleToTotalPixels, LoadImage, Note, Note, PainterFluxImageEdit, SaveImage, LoraLoaderModelOnly, LoadImage, easy cleanGpuUsed, VAEDecode, workflow>自定义采样器]
patterns: []
missing: []
---

# 图片生成/图生图/Style Transfer 风格迁移 High-Definition Restoration an_2106912097144754178.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Style Transfer 风格迁移 High-Definition Restoration an_2106912097144754178.json`

## 结构

**生成流程**：Model → Decode → Process → Output → Other

**节点**（25 个）：
- `PainterFluxImageEdit`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `GetImageSize`
- `VAEDecode` ★核心
- `VAELoader`
- `workflow>自定义采样器`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `easy textIndexSwitch`
- `UNETLoader` ★核心
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `Note`
- `Note`
- `PainterFluxImageEdit`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `workflow>自定义采样器`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`PainterFluxImageEdit`、`easy cleanGpuUsed`、`CLIPLoader`、`GetImageSize`、`VAEDecode`、`VAELoader`、`workflow>自定义采样器`、`MuyeTextEditOutput`、`LoraLoaderModelOnly`、`SaveImage`、`easy textIndexSwitch`、`UNETLoader`、`ImageScaleToTotalPixels`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、SaveImage、LoadImage、workflow>自定义采样器
