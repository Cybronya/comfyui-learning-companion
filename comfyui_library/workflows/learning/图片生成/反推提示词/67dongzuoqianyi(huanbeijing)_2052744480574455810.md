---
key: 图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json
name: 67dongzuoqianyi(huanbeijing)_2052744480574455810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json
hash: 43b05bde49b24f4e
coverage: 0.491071
learned_at: 2026-10-26 01:44:37
nodes: [SetNode, SetNode, ImageResizeKJv2, SetNode, easy seed, SetNode, PrimitiveString, Fast Groups Bypasser (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, WanVideoLoraSelectMulti, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, SetNode, LoadWanVideoT5TextEncoder, MarkdownNote, GetNode, ImageFromBatch, PreviewImage, DownloadAndLoadSAM2Model, GetNode, GetImageSize+, Mute / Bypass Repeater (rgthree), DrawMaskOnImage, StringConcatenate, GetNode, StringConcatenate, PrimitiveString, PrimitiveString, PreviewAny, SetNode, Sam2Segmentation, Mute / Bypass Relay (rgthree), GetNode, BlockifyMask, GrowMask, ResizeMask, easy cleanGpuUsed, easy clearCacheAll, SetNode, SetNode, GetNode, GetNode, GetImageSize, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose, SetNode, SetNode, SetNode, GetImageSize, GetNode, GetNode, SetNode, ImageConcatMulti, PreviewImage, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetImageSize, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoTextEncode, WanVideoAnimateEmbeds, SetNode, SetNode, PrimitiveStringMultiline, SetNode, GetNode, GetNode, VHS_VideoInfo, ImageResizeKJv2, GetNode, CreateVideo, SaveVideo, SetNode, VHS_LoadVideo, SetNode, SetNode, LoadImage, easy int]
patterns: []
missing: []
---

# 图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/67dongzuoqianyi(huanbeijing)_2052744480574455810.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（112 个）：
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `easy seed`
- `SetNode`
- `PrimitiveString`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `MarkdownNote`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `GetImageSize+`
- `Mute / Bypass Repeater (rgthree)`
- `DrawMaskOnImage`
- `StringConcatenate`
- `GetNode`
- `StringConcatenate`
- `PrimitiveString`
- `PrimitiveString`
- `PreviewAny`
- `SetNode`
- `Sam2Segmentation`
- `Mute / Bypass Relay (rgthree)`
- `GetNode`
- `BlockifyMask`
- `GrowMask`
- `ResizeMask`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `GetNode`
- `CreateVideo`
- `SaveVideo`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `LoadImage`
- `easy int`

## 知识

覆盖率 **49%**（55/112）

**有卡**：`ImageResizeKJv2`、`easy seed`、`Label (rgthree)`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`ImageFromBatch`、`DownloadAndLoadSAM2Model`、`GetImageSize+`、`Mute / Bypass Repeater (rgthree)`、`DrawMaskOnImage`、`StringConcatenate`、`Sam2Segmentation`、`Mute / Bypass Relay (rgthree)`、`BlockifyMask`、`GrowMask`、`ResizeMask`、`easy cleanGpuUsed`、`easy clearCacheAll`、`GetImageSize`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoAnimateEmbeds`、`VHS_VideoInfo`、`CreateVideo`、`SaveVideo`、`VHS_LoadVideo`、`LoadImage`、`easy int`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
