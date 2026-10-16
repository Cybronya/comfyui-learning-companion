---
key: 视频生成/图生视频/视频二创人物角色替换Wan+Animate+OneToAll+SeedVR2.5_2002709997517717506.json
name: 视频二创人物角色替换Wan+Animate+OneToAll+SeedVR2.5_2002709997517717506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2002709997517717506.json
hash: 08f4a9b00957fdb9
coverage: 0.962963
learned_at: 2026-10-15 22:33:49
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, OnnxDetectionModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoSampler, WanVideoAnimateEmbeds, VHS_VideoCombine, WanVideoDecode, LayerUtility: PurgeVRAM V2, RHHiddenNodes, VHS_VideoCombine, WanVideoBlockSwap, PoseDetectionOneToAllAnimation, PoseAndFaceDetection, Fast Groups Bypasser (rgthree), FlashVSRNode, ImageResizeKJv2, ImageResizeKJv2, Int, Int, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/视频二创人物角色替换Wan+Animate+OneToAll+SeedVR2.5_2002709997517717506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2002709997517717506.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `OnnxDetectionModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `PoseDetectionOneToAllAnimation`
- `PoseAndFaceDetection`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`RHHiddenNodes`、`WanVideoBlockSwap`、`PoseDetectionOneToAllAnimation`、`PoseAndFaceDetection`、`FlashVSRNode`、`ImageResizeKJv2`、`Int`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
