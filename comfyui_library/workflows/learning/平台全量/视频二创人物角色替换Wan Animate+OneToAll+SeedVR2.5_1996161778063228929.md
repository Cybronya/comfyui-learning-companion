---
key: 平台全量/视频二创人物角色替换Wan Animate+OneToAll+SeedVR2.5_1996161778063228929.json
name: 视频二创人物角色替换Wan Animate+OneToAll+SeedVR2.5_1996161778063228929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频二创人物角色替换Wan Animate+OneToAll+SeedVR2.5_1996161778063228929.json
hash: 0416b69357131d42
coverage: 0.964286
learned_at: 2026-11-14 02:35:06
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, OnnxDetectionModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoSampler, WanVideoAnimateEmbeds, VHS_VideoCombine, LoadImage, WanVideoDecode, LayerUtility: PurgeVRAM V2, Int, RHHiddenNodes, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, WanVideoBlockSwap, ImageResizeKJv2, ImageResizeKJv2, PoseDetectionOneToAllAnimation, Int, PoseAndFaceDetection, Fast Groups Bypasser (rgthree), FlashVSRNode]
patterns: []
missing: []
---

# 平台全量/视频二创人物角色替换Wan Animate+OneToAll+SeedVR2.5_1996161778063228929.json

> 来源文件 `comfyui_library/workflows/平台全量/视频二创人物角色替换Wan Animate+OneToAll+SeedVR2.5_1996161778063228929.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
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
- `LoadImage`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `RHHiddenNodes`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PoseDetectionOneToAllAnimation`
- `Int`
- `PoseAndFaceDetection`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`LoadImage`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`Int`、`RHHiddenNodes`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`PoseAndFaceDetection`、`FlashVSRNode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
