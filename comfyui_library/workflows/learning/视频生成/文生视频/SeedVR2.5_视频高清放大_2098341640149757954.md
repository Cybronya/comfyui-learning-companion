---
key: 视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json
name: SeedVR2.5_视频高清放大_2098341640149757954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json
hash: 791e53360dfd6763
coverage: 0.533333
learned_at: 2026-10-11 21:41:51
nodes: [Reroute, Reroute, Reroute, SeedVR2LoadDiTModel, Reroute, VHS_LoadVideo, ImageScaleToTotalPixels, VHS_VideoInfo, VHS_VideoCombine, Note, INTConstant, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Note, SetNode]
patterns: []
missing: []
---

# 视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SeedVR2.5_视频高清放大_2098341640149757954.json`

## 结构

**生成流程**：Process → Other

**节点**（15 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `SeedVR2LoadDiTModel`
- `Reroute`
- `VHS_LoadVideo`
- `ImageScaleToTotalPixels`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `Note`
- `INTConstant`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Note`
- `SetNode`

## 知识

覆盖率 **53%**（8/15）

**有卡**：`SeedVR2LoadDiTModel`、`VHS_LoadVideo`、`ImageScaleToTotalPixels`、`VHS_VideoInfo`、`VHS_VideoCombine`、`INTConstant`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、ImageScaleToTotalPixels、INTConstant、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo
