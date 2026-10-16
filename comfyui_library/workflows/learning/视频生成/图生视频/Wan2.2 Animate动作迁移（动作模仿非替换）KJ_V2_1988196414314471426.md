---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移（动作模仿非替换）KJ_V2_1988196414314471426.json
name: Wan2.2 Animate动作迁移（动作模仿非替换）KJ_V2_1988196414314471426.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988196414314471426.json
hash: 97ee0d86cd1dba38
coverage: 0.566038
learned_at: 2026-10-15 22:33:02
nodes: [GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoBlockSwap, ttN float, ttN float, PrimitiveInt, LoadImage, PoseAndFaceDetection, VHS_VideoCombine, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoClipVisionEncode, Note, SetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VHS_LoadVideo, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, SetNode, SetNode, SetNode, SetNode, SetNode, String Literal, SimpleMath+, SetNode, SetNode, ttN float, ImageResizeKJv2, OnnxDetectionModelLoader, DrawViTPose, SetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, LayerUtility: PurgeVRAM, easy cleanGpuUsed, SetNode, easy cleanGpuUsed, CLIPVisionLoader, GetNode, GetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移（动作模仿非替换）KJ_V2_1988196414314471426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988196414314471426.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（53 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `ttN float`
- `ttN float`
- `PrimitiveInt`
- `LoadImage`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoClipVisionEncode`
- `Note`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VHS_LoadVideo`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `String Literal`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `ttN float`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `SetNode`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **57%**（30/53）

**有卡**：`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`ttN float`、`LoadImage`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`LayerUtility: PurgeVRAM`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`String Literal`、`SimpleMath+`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`DrawViTPose`、`WanVideoTextEncodeCached`、`easy cleanGpuUsed`、`CLIPVisionLoader`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
