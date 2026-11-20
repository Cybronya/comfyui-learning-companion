---
key: 平台全量/小云雀seedance2.0水印去除_2025291039346532354.json
name: 小云雀seedance2.0水印去除_2025291039346532354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除_2025291039346532354.json
hash: a59ec8b7b061b2bb
coverage: 0.785714
learned_at: 2026-11-14 02:01:13
nodes: [VHS_VideoInfo, SAM3Segment, VHS_SelectImages, VHS_VideoCombine, easy cleanGpuUsed, VHS_SelectMasks, RepeatImageBatch, VHS_LoadVideo, DiffuEraserLoader, DiffuEraserSampler, Reroute, Reroute, Reroute, MaskToImage]
patterns: []
missing: []
---

# 平台全量/小云雀seedance2.0水印去除_2025291039346532354.json

> 来源文件 `comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除_2025291039346532354.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（14 个）：
- `VHS_VideoInfo`
- `SAM3Segment`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `VHS_SelectMasks`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `DiffuEraserLoader`
- `DiffuEraserSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `MaskToImage`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`VHS_VideoInfo`、`SAM3Segment`、`VHS_SelectImages`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`VHS_SelectMasks`、`RepeatImageBatch`、`VHS_LoadVideo`、`DiffuEraserLoader`、`DiffuEraserSampler`、`MaskToImage`

**用到的条目**：DiffuEraserSampler、DiffuEraserLoader、easy cleanGpuUsed、MaskToImage、RepeatImageBatch、SAM3Segment、VHS_LoadVideo、VHS_SelectImages
