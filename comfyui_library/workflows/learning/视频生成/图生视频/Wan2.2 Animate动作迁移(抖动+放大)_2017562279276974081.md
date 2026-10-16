---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移(抖动+放大)_2017562279276974081.json
name: Wan2.2 Animate动作迁移(抖动+放大)_2017562279276974081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2017562279276974081.json
hash: 94c11facc90a8745
coverage: 0.492754
learned_at: 2026-10-15 22:34:49
nodes: [WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, GetNode, VHS_VideoInfo, OnnxDetectionModelLoader, easy cleanGpuUsed, ImageResizeKJv2, SetNode, SetNode, GetImageSizeAndCount, SetNode, LoadImage, SetNode, SetNode, WanVideoVAELoader, MemoryCleaner, WanVideoBlockSwap, MemoryCleaner, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoModelLoader, DrawViTPose, SetNode, MemoryCleaner, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PreviewImage, GetNode, MemoryCleaner, GetNode, GetNode, WanVideoTeaCache, VHS_LoadVideo, Int, Int, Int, PoseAndFaceDetection, VHS_VideoCombine, WanVideoTextEncodeCached, WanVideoDecode, GetNode, GetNode, WanVideoContextOptions, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, FlashVSRNode, GetNode, GetNode, WanVideoClipVisionEncode, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移(抖动+放大)_2017562279276974081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2017562279276974081.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（69 个）：
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `VHS_VideoInfo`
- `OnnxDetectionModelLoader`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `MemoryCleaner`
- `WanVideoBlockSwap`
- `MemoryCleaner`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `DrawViTPose`
- `SetNode`
- `MemoryCleaner`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `MemoryCleaner`
- `GetNode`
- `GetNode`
- `WanVideoTeaCache`
- `VHS_LoadVideo`
- `Int`
- `Int`
- `Int`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `FlashVSRNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `RHHiddenNodes`

## 知识

覆盖率 **49%**（34/69）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`VHS_VideoInfo`、`OnnxDetectionModelLoader`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`LoadImage`、`WanVideoVAELoader`、`MemoryCleaner`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoModelLoader`、`DrawViTPose`、`WanVideoTeaCache`、`VHS_LoadVideo`、`Int`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`WanVideoContextOptions`、`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSRNode`、`WanVideoClipVisionEncode`、`RHHiddenNodes`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
