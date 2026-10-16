---
key: 视频生成/图生视频/Wan2.2 Animate人物动作+表情迁移_1972599286972231682.json
name: Wan2.2 Animate人物动作+表情迁移_1972599286972231682.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1972599286972231682.json
hash: 9bfff342993e401b
coverage: 0.485714
learned_at: 2026-10-15 22:32:00
nodes: [WanVideoDecode, GetNode, GetImageSizeAndCount, GetNode, LayerUtility: PurgeVRAM, ImageConcatMulti, GetNode, ImageResizeKJv2, CLIPVisionLoader, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoAnimateEmbeds, SetNode, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, GetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, easy showAnything, GetNode, LayerUtility: PurgeVRAM, GetImageSizeAndCount, GetNode, VHS_VideoCombine, Int, Int, GetNode, SetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, easy showAnything, WanVideoTextEncodeCached, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, PixelPerfectResolution, WanVideoModelLoader, SetNode, GetNode, SetNode, WanVideoVAELoader, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, Int, WanVideoLoraSelectMulti, DWPreprocessor, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, LoadImage, ImageConcatMulti, SetNode, GetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate人物动作+表情迁移_1972599286972231682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972599286972231682.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（70 个）：
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `ImageConcatMulti`
- `GetNode`
- `ImageResizeKJv2`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `GetImageSizeAndCount`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `GetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `easy showAnything`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `PixelPerfectResolution`
- `WanVideoModelLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `WanVideoLoraSelectMulti`
- `DWPreprocessor`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **49%**（34/70）

**有卡**：`WanVideoDecode`、`GetImageSizeAndCount`、`LayerUtility: PurgeVRAM`、`ImageConcatMulti`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`VHS_VideoInfo`、`VHS_VideoCombine`、`Int`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`PixelPerfectResolution`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`DWPreprocessor`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
