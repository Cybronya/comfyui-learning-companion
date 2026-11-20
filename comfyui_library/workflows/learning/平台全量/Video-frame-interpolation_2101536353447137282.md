---
key: 平台全量/Video-frame-interpolation_2101536353447137282.json
name: Video-frame-interpolation_2101536353447137282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Video-frame-interpolation_2101536353447137282.json
hash: fa3885db2a4aa513
coverage: 0.692308
learned_at: 2026-11-14 01:03:16
nodes: [MarkdownNote, FrameInterpolationModelLoader, FrameInterpolate, PrimitiveInt, GetVideoComponents, PrimitiveInt, CreateVideo, ComfyMathExpression, ComfySwitchNode, PrimitiveBoolean, LoadVideo, easy cleanGpuUsed, SaveVideo]
patterns: []
missing: []
---

# 平台全量/Video-frame-interpolation_2101536353447137282.json

> 来源文件 `comfyui_library/workflows/平台全量/Video-frame-interpolation_2101536353447137282.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（13 个）：
- `MarkdownNote`
- `FrameInterpolationModelLoader`
- `FrameInterpolate`
- `PrimitiveInt`
- `GetVideoComponents`
- `PrimitiveInt`
- `CreateVideo`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `LoadVideo`
- `easy cleanGpuUsed`
- `SaveVideo`

## 知识

覆盖率 **69%**（9/13）

**有卡**：`FrameInterpolationModelLoader`、`FrameInterpolate`、`GetVideoComponents`、`CreateVideo`、`ComfyMathExpression`、`PrimitiveBoolean`、`LoadVideo`、`easy cleanGpuUsed`、`SaveVideo`

**用到的条目**：SaveVideo、ComfyMathExpression、CreateVideo、easy cleanGpuUsed、FrameInterpolate、FrameInterpolationModelLoader、GetVideoComponents、LoadVideo
