---
key: 视频生成/图生视频/人物角色替换Wan Animate+SeedVR2.5 wan2.2 视频重绘动作迁移参考图片_1997869036803436545.json
name: 人物角色替换Wan Animate+SeedVR2.5 wan2.2 视频重绘动作迁移参考图片_1997869036803436545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物角色替换Wan Animate+SeedVR2.5 wan2.2 视频重绘动作迁移参考图片_1997869036803436545.json
hash: 2649229614193e00
coverage: 0.964286
learned_at: 2026-10-15 22:33:30
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, SDPoseOODLoader, SDPoseOODProcessor, OnnxDetectionModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, PoseAndFaceDetection, WanVideoSampler, WanVideoAnimateEmbeds, ImageResizeKJv2, ImageResizeKJv2, FlashVSRNode, WanVideoDecode, LayerUtility: PurgeVRAM V2, Fast Groups Bypasser (rgthree), RHHiddenNodes, LoadImage, VHS_LoadVideo, Int, Int, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/人物角色替换Wan Animate+SeedVR2.5 wan2.2 视频重绘动作迁移参考图片_1997869036803436545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997869036803436545.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `OnnxDetectionModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `FlashVSRNode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `Fast Groups Bypasser (rgthree)`
- `RHHiddenNodes`
- `LoadImage`
- `VHS_LoadVideo`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`FlashVSRNode`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`RHHiddenNodes`、`LoadImage`、`VHS_LoadVideo`、`Int`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
