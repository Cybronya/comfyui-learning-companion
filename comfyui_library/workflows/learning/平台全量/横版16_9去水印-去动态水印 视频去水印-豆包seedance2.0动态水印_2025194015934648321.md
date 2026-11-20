---
key: 平台全量/横版16_9去水印-去动态水印 视频去水印-豆包seedance2.0动态水印_2025194015934648321.json
name: 横版16_9去水印-去动态水印 视频去水印-豆包seedance2.0动态水印_2025194015934648321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/横版16_9去水印-去动态水印 视频去水印-豆包seedance2.0动态水印_2025194015934648321.json
hash: 26c0b1c1eb3c5f3f
coverage: 0.7
learned_at: 2026-11-14 02:18:40
nodes: [easy showAnything, easy showAnything, easy showAnything, easy showAnything, easy showAnything, PreviewImage, ImageResizeKJv2, MaskToImage, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoInfo, DiffuEraserLoader, DiffuEraserSampler, RepeatImageBatch, easy cleanGpuUsed, ImageConcanate, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/横版16_9去水印-去动态水印 视频去水印-豆包seedance2.0动态水印_2025194015934648321.json

> 来源文件 `comfyui_library/workflows/平台全量/横版16_9去水印-去动态水印 视频去水印-豆包seedance2.0动态水印_2025194015934648321.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（20 个）：
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `PreviewImage`
- `ImageResizeKJv2`
- `MaskToImage`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `DiffuEraserLoader`
- `DiffuEraserSampler` ★核心
- `RepeatImageBatch`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **70%**（14/20）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`VHS_VideoInfo`、`DiffuEraserLoader`、`DiffuEraserSampler`、`RepeatImageBatch`、`ImageConcanate`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、ImageResizeKJv2、DiffuEraserLoader、easy cleanGpuUsed、ImageConcanate、MaskToImage
