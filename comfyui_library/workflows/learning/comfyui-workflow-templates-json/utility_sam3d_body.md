---
key: comfyui-workflow-templates-json/utility_sam3d_body.json
name: utility_sam3d_body
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/utility_sam3d_body.json
hash: 4b989539c6e4b385
official: true
coverage: 0.8
learned_at: 2026-10-15 22:24:57
nodes: [CLIPTextEncode, SAM3_VideoTrack, CheckpointLoaderSimple, RTDETR_detect, SAM3DBody_FaceExpression, SAM3DBody_Predict, SAM3DBody_Smooth, SAM3DBody_Loader, MoGeGeometryToFOV, MoGeInference, LoadMoGeModel, BuildPoseFile, CreateVideo, SaveVideo, LoadVideo, Video Slice, GetVideoComponents, Note, Note, Note, Note, UNETLoader, SAM3DBody_Render, MarkdownNote, Save3DAdvanced]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
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

覆盖率 **80%**（20/25）

**有卡**：`CLIPTextEncode`、`SAM3_VideoTrack`、`CheckpointLoaderSimple`、`RTDETR_detect`、`SAM3DBody_FaceExpression`、`SAM3DBody_Predict`、`SAM3DBody_Smooth`、`SAM3DBody_Loader`、`MoGeGeometryToFOV`、`MoGeInference`、`LoadMoGeModel`、`BuildPoseFile`、`CreateVideo`、`SaveVideo`、`LoadVideo`、`Video Slice`、`GetVideoComponents`、`UNETLoader`、`SAM3DBody_Render`、`Save3DAdvanced`

**用到的条目**：CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、SaveVideo、Save3DAdvanced、CreateVideo、GetVideoComponents、LoadVideo
