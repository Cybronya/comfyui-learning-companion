---
key: 平台全量/seedance2.0小云雀豆包视频一键去除水印_2033713008693747714.json
name: seedance2.0小云雀豆包视频一键去除水印_2033713008693747714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0小云雀豆包视频一键去除水印_2033713008693747714.json
hash: 59725e90d9024ee0
coverage: 0.733333
learned_at: 2026-11-14 01:17:45
nodes: [VHS_LoadVideo, VHS_VideoInfo, SAM3Segment, VHS_SelectMasks, easy cleanGpuUsed, RepeatImageBatch, MaskToImage, Reroute, DiffuEraserSampler, Reroute, Reroute, VHS_SelectImages, DiffuEraserLoader, Fast Groups Bypasser (rgthree), VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/seedance2.0小云雀豆包视频一键去除水印_2033713008693747714.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0小云雀豆包视频一键去除水印_2033713008693747714.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（15 个）：
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `SAM3Segment`
- `VHS_SelectMasks`
- `easy cleanGpuUsed`
- `RepeatImageBatch`
- `MaskToImage`
- `Reroute`
- `DiffuEraserSampler` ★核心
- `Reroute`
- `Reroute`
- `VHS_SelectImages`
- `DiffuEraserLoader`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`VHS_LoadVideo`、`VHS_VideoInfo`、`SAM3Segment`、`VHS_SelectMasks`、`easy cleanGpuUsed`、`RepeatImageBatch`、`MaskToImage`、`DiffuEraserSampler`、`VHS_SelectImages`、`DiffuEraserLoader`、`VHS_VideoCombine`

**用到的条目**：DiffuEraserSampler、DiffuEraserLoader、easy cleanGpuUsed、MaskToImage、RepeatImageBatch、SAM3Segment、VHS_LoadVideo、VHS_SelectImages
