---
key: 平台全量/小云雀seedance2.0水印去除_2033469559058993154.json
name: 小云雀seedance2.0水印去除_2033469559058993154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除_2033469559058993154.json
hash: a75f8f904c425523
coverage: 0.733333
learned_at: 2026-11-14 02:01:14
nodes: [SAM3Segment, DiffuEraserLoader, VHS_SelectMasks, easy cleanGpuUsed, RepeatImageBatch, MaskToImage, Reroute, VHS_VideoCombine, DiffuEraserSampler, Reroute, Reroute, VHS_LoadVideo, Fast Groups Bypasser (rgthree), VHS_SelectImages, VHS_VideoInfo]
patterns: []
missing: []
---

# 平台全量/小云雀seedance2.0水印去除_2033469559058993154.json

> 来源文件 `comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除_2033469559058993154.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（15 个）：
- `SAM3Segment`
- `DiffuEraserLoader`
- `VHS_SelectMasks`
- `easy cleanGpuUsed`
- `RepeatImageBatch`
- `MaskToImage`
- `Reroute`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `Reroute`
- `Reroute`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `VHS_SelectImages`
- `VHS_VideoInfo`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`SAM3Segment`、`DiffuEraserLoader`、`VHS_SelectMasks`、`easy cleanGpuUsed`、`RepeatImageBatch`、`MaskToImage`、`VHS_VideoCombine`、`DiffuEraserSampler`、`VHS_LoadVideo`、`VHS_SelectImages`、`VHS_VideoInfo`

**用到的条目**：DiffuEraserSampler、DiffuEraserLoader、easy cleanGpuUsed、MaskToImage、RepeatImageBatch、SAM3Segment、VHS_LoadVideo、VHS_SelectImages
