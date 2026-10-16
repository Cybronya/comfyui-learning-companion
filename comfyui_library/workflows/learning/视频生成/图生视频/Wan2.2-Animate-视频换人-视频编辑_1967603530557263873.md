---
key: 视频生成/图生视频/Wan2.2-Animate-视频换人-视频编辑_1967603530557263873.json
name: Wan2.2-Animate-视频换人-视频编辑_1967603530557263873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967603530557263873.json
hash: 427268eb4e40c6f1
coverage: 0.553191
learned_at: 2026-10-15 22:31:42
nodes: [WanVideoTorchCompileSettings, GetImageSizeAndCount, GetNode, GetNode, GetNode, easy cleanGpuUsed, easy clearCacheAll, BlockifyMask, ResizeMask, DrawMaskOnImage, WanVideoVAELoader, WanVideoModelLoader, MarkdownNote, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoLoraSelectMulti, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, Sam2Segmentation, DownloadAndLoadSAM2Model, GetNode, SetNode, PrimitiveStringMultiline, GrowMask, GetNode, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawViTPose, GetImageSize, GetNode, SetNode, GetNode, GetNode, ImageConcatMulti, GetNode, PrimitiveString, PreviewAny, PrimitiveString, StringConcatenate, StringConcatenate, GetNode, SetNode, GetImageRangeFromBatch, GetImageSize+, GetNode, WanVideoClipVisionEncode, WanVideoDecode, WanVideoTextEncode, easy seed, GetNode, GetNode, WanVideoSampler, LoadImage, ImageConcatMulti, WanVideoAnimateEmbeds, GetNode, PrimitiveString, SetNode, Int, Int, ImageResizeKJv2, GetNode, GetImageSize, GetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, VHS_LoadVideo, SetNode, Bjornulf_ShowInt, SetNode, ImageFromBatch, GetNode, PreviewImage, GetNode, GetImageSize, SetNode, ImageResizeKJv2, PreviewImage, LoadImage, SetNode, VHS_VideoInfo, Bjornulf_ShowFloat, Bjornulf_ShowInt, SetNode, SimpleMath+, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate-视频换人-视频编辑_1967603530557263873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967603530557263873.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（94 个）：
- `WanVideoTorchCompileSettings`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `BlockifyMask`
- `ResizeMask`
- `DrawMaskOnImage`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `MarkdownNote`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `GrowMask`
- `GetNode`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `PrimitiveString`
- `PreviewAny`
- `PrimitiveString`
- `StringConcatenate`
- `StringConcatenate`
- `GetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetImageSize+`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `easy seed`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `LoadImage`
- `ImageConcatMulti`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `PrimitiveString`
- `SetNode`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `SetNode`
- `Bjornulf_ShowInt`
- `SetNode`
- `ImageFromBatch`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetImageSize`
- `SetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `VHS_VideoInfo`
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowInt`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **55%**（52/94）

**有卡**：`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`easy clearCacheAll`、`BlockifyMask`、`ResizeMask`、`DrawMaskOnImage`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`GrowMask`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawViTPose`、`GetImageSize`、`ImageConcatMulti`、`StringConcatenate`、`GetImageRangeFromBatch`、`GetImageSize+`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoTextEncode`、`easy seed`、`WanVideoSampler`、`LoadImage`、`WanVideoAnimateEmbeds`、`Int`、`ImageResizeKJv2`、`VHS_LoadVideo`、`Bjornulf_ShowInt`、`ImageFromBatch`、`VHS_VideoInfo`、`Bjornulf_ShowFloat`、`SimpleMath+`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
