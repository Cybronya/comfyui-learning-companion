---
key: 视频生成/图生视频/【简便版】Wan2.2 图生视频 人物动作迁移 复制姿态_1976803129901699073.json
name: 【简便版】Wan2.2 图生视频 人物动作迁移 复制姿态_1976803129901699073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976803129901699073.json
hash: 91ea364a76d4815c
coverage: 0.44
learned_at: 2026-10-15 22:32:12
nodes: [WanVideoSampler, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, ImageResizeKJv2, ImageConcatMulti, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, PrimitiveString, PrimitiveString, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, StringConcatenate, StringConcatenate, SetNode, PreviewAny, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PreviewImage, ImageFromBatch, GetNode, GetNode, GetImageSize+, easy cleanGpuUsed, ResizeMask, OnnxDetectionModelLoader, Sam2Segmentation, DownloadAndLoadSAM2Model, BlockifyMask, GetNode, DrawMaskOnImage, GetImageSize, SetNode, PreviewImage, GetNode, easy clearCacheAll, WanVideoVAELoader, GetImageSizeAndCount, GetImageSize, SetNode, VHS_VideoCombine, DrawViTPose, SetNode, GetImageSize, PoseAndFaceDetection, SetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, MarkdownNote, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, SetNode, SetNode, GrowMask, GetNode, WanVideoTextEncode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetImageRangeFromBatch, easy seed, WanVideoLoraSelectMulti, WanVideoModelLoader, LoadImage, VHS_LoadVideo, PrimitiveStringMultiline, easy int, SetNode, ImageResizeKJ, SetNode, SetNode, PrimitiveString]
patterns: []
missing: []
---

# 视频生成/图生视频/【简便版】Wan2.2 图生视频 人物动作迁移 复制姿态_1976803129901699073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976803129901699073.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（100 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveString`
- `PrimitiveString`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `StringConcatenate`
- `StringConcatenate`
- `SetNode`
- `PreviewAny`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetImageSize+`
- `easy cleanGpuUsed`
- `ResizeMask`
- `OnnxDetectionModelLoader`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `BlockifyMask`
- `GetNode`
- `DrawMaskOnImage`
- `GetImageSize`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `easy clearCacheAll`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `GetImageSize`
- `SetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `SetNode`
- `GetImageSize`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GrowMask`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `easy seed`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `PrimitiveStringMultiline`
- `easy int`
- `SetNode`
- `ImageResizeKJ`
- `SetNode`
- `SetNode`
- `PrimitiveString`

## 知识

覆盖率 **44%**（44/100）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`ImageConcatMulti`、`VHS_VideoInfo`、`StringConcatenate`、`ImageFromBatch`、`GetImageSize+`、`easy cleanGpuUsed`、`ResizeMask`、`OnnxDetectionModelLoader`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`BlockifyMask`、`DrawMaskOnImage`、`GetImageSize`、`easy clearCacheAll`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`GrowMask`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`GetImageRangeFromBatch`、`easy seed`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`LoadImage`、`VHS_LoadVideo`、`easy int`、`ImageResizeKJ`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
