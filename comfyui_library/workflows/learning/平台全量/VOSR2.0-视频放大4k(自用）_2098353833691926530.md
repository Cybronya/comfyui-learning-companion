---
key: 平台全量/VOSR2.0-视频放大4k(自用）_2098353833691926530.json
name: VOSR2.0-视频放大4k(自用）_2098353833691926530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR2.0-视频放大4k(自用）_2098353833691926530.json
hash: ca96df2e13749273
coverage: 0.625
learned_at: 2026-11-14 01:02:59
nodes: [VHS_VideoCombine, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, VHS_LoadVideo, SetNode, VHS_VideoInfo, SetNode, VOSR2ModelLoader, PDIMAGE_LongerSize, easy cleanGpuUsed, RTXVideoSuperResolution, VOSR2Upscale, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/VOSR2.0-视频放大4k(自用）_2098353833691926530.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR2.0-视频放大4k(自用）_2098353833691926530.json`

## 结构

**生成流程**：Model → Process → Other

**节点**（16 个）：
- `VHS_VideoCombine`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `VOSR2ModelLoader`
- `PDIMAGE_LongerSize`
- `easy cleanGpuUsed`
- `RTXVideoSuperResolution`
- `VOSR2Upscale`
- `VHS_VideoCombine`

## 知识

覆盖率 **62%**（10/16）

**有卡**：`VHS_VideoCombine`、`ImageConcatMulti`、`VHS_LoadVideo`、`VHS_VideoInfo`、`VOSR2ModelLoader`、`PDIMAGE_LongerSize`、`easy cleanGpuUsed`、`RTXVideoSuperResolution`、`VOSR2Upscale`

**用到的条目**：VOSR2Upscale、PDIMAGE_LongerSize、RTXVideoSuperResolution、easy cleanGpuUsed、ImageConcatMulti、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo
