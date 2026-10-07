---
key: comfyui-workflow-templates-json/utility_sam3d_body.json
name: utility_sam3d_body
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_sam3d_body.json
hash: 4b989539c6e4b385
official: true
coverage: 0.76
learned_at: 2026-10-07 21:36:50
nodes: [CLIPTextEncode, SAM3_VideoTrack, CheckpointLoaderSimple, RTDETR_detect, SAM3DBody_FaceExpression, SAM3DBody_Predict, SAM3DBody_Smooth, SAM3DBody_Loader, MoGeGeometryToFOV, MoGeInference, LoadMoGeModel, BuildPoseFile, CreateVideo, SaveVideo, LoadVideo, Video Slice, GetVideoComponents, Note, Note, Note, Note, UNETLoader, SAM3DBody_Render, MarkdownNote, Save3DAdvanced]
patterns: []
missing: [Video Slice]
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
discoveries: [次要节点 `Video Slice` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/utility_sam3d_body.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/utility_sam3d_body.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `CheckpointLoaderSimple` ★核心
- `RTDETR_detect`
- `SAM3DBody_FaceExpression`
- `SAM3DBody_Predict`
- `SAM3DBody_Smooth`
- `SAM3DBody_Loader`
- `MoGeGeometryToFOV`
- `MoGeInference`
- `LoadMoGeModel`
- `BuildPoseFile`
- `CreateVideo`
- `SaveVideo`
- `LoadVideo`
- `Video Slice`
- `GetVideoComponents`
- `Note`
- `Note`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `SAM3DBody_Render`
- `MarkdownNote`
- `Save3DAdvanced`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`CLIPTextEncode`、`SAM3_VideoTrack`、`CheckpointLoaderSimple`、`RTDETR_detect`、`SAM3DBody_FaceExpression`、`SAM3DBody_Predict`、`SAM3DBody_Smooth`、`SAM3DBody_Loader`、`MoGeGeometryToFOV`、`MoGeInference`、`LoadMoGeModel`、`BuildPoseFile`、`CreateVideo`、`SaveVideo`、`LoadVideo`、`GetVideoComponents`、`UNETLoader`、`SAM3DBody_Render`、`Save3DAdvanced`

**缺卡**（1）：`Video Slice`

**用到的条目**：CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、SaveVideo、Save3DAdvanced、CreateVideo、GetVideoComponents、LoadVideo

## 学习发现

- 次要节点 `Video Slice` 知识库中没有该节点类型的任何知识
