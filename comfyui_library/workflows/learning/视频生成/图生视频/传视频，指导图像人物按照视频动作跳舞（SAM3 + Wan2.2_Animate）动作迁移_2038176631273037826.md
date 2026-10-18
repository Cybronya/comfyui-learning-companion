---
key: 视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json
name: 传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json
hash: ec7f2a66f5c6114e
coverage: 0.625
learned_at: 2026-10-15 22:36:00
nodes: [Reroute, CLIPVisionLoader, ImageResizeKJv2, WanVideoSampler, LoadWanVideoT5TextEncoder, PreviewImage, Reroute, WanVideoVAELoader, Reroute, Reroute, Reroute, Reroute, WanVideoClipVisionEncode, OnnxDetectionModelLoader, PoseAndFaceDetection, Reroute, Reroute, Reroute, Reroute, WanVideoAnimateEmbeds, VHS_VideoInfo, DrawViTPose, Reroute, Reroute, Reroute, Reroute, VHS_VideoCombine, WanVideoDecode, ImageFromBatch, VHS_VideoCombine, WanVideoLoraSelectMulti, VHS_LoadVideo, INTConstant, INTConstant, WanVideoContextOptions, Note, WanVideoModelLoader, WanVideoBlockSwap, SimpleMath+, Int, SimpleMath+, Int, Int, LoadImage, WanVideoTextEncodeSingle, PrimitiveFloat, MarkdownNote, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/传视频，指导图像人物按照视频动作跳舞（SAM3 + Wan2.2_Animate）动作迁移_2038176631273037826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038176631273037826.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `Reroute`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `Reroute`
- `WanVideoVAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoAnimateEmbeds`
- `VHS_VideoInfo`
- `DrawViTPose`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `WanVideoContextOptions`
- `Note`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `Int`
- `SimpleMath+`
- `Int`
- `Int`
- `LoadImage`
- `WanVideoTextEncodeSingle`
- `PrimitiveFloat`
- `MarkdownNote`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **62%**（30/48）

**有卡**：`CLIPVisionLoader`、`ImageResizeKJv2`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoAnimateEmbeds`、`VHS_VideoInfo`、`DrawViTPose`、`VHS_VideoCombine`、`WanVideoDecode`、`ImageFromBatch`、`WanVideoLoraSelectMulti`、`VHS_LoadVideo`、`INTConstant`、`WanVideoContextOptions`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`SimpleMath+`、`Int`、`LoadImage`、`WanVideoTextEncodeSingle`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeSingle、WanVideoLoraSelectMulti
