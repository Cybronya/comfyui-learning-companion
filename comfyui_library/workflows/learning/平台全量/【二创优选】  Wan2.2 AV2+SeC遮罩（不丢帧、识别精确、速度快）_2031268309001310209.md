---
key: 平台全量/【二创优选】  Wan2.2 AV2+SeC遮罩（不丢帧、识别精确、速度快）_2031268309001310209.json
name: 【二创优选】  Wan2.2 AV2+SeC遮罩（不丢帧、识别精确、速度快）_2031268309001310209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【二创优选】  Wan2.2 AV2+SeC遮罩（不丢帧、识别精确、速度快）_2031268309001310209.json
hash: f4fc07e9cb4388e1
coverage: 0.483607
learned_at: 2026-11-14 01:22:49
nodes: [GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, SetNode, SetNode, Note, WanVideoDecode, Note, WanVideoVAELoader, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, Note, WanVideoBlockSwap, Note, SetNode, Int, CLIPVisionLoader, GetNode, GetNode, VHS_VideoCombine, Note, Note, Note, DrawViTPose, PoseAndFaceDetection, SeCVideoSegmentation, InvertMask, BlockifyMask, PrimitiveInt, WanVideoClipVisionEncode, Note, Note, GetNode, SetNode, GetImageSizeAndCount, DrawMaskOnImage, SetNode, ImageFromBatch, VHS_VideoCombine, SetNode, DrawMaskOnImage, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, SeCModelLoader, Note, VHS_VideoInfo, WanVideoAnimateEmbeds, SetNode, SetNode, GetNode, SetNode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSamplerExtraArgs, WanVideoTeaCache, OnnxDetectionModelLoader, ImageFromBatch, CoordinatePlotter, CoordinatePlotter, ImageFromBatch, ImageFromBatch, ImageBatch, GetNode, ImageBlend, ImageConcatMulti, GetNode, VHS_VideoCombine, SetNode, MaskPreview+, GetNode, VHS_VideoCombine, Note, WanVideoContextOptions, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, GetNode, Note, VHS_VideoCombine, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoSampler, GrowMaskWithBlur, PreviewImage, GetNode, BatchCount+, RepeatImageBatch, RHHiddenNodes, BatchCount+, GetNode, VHS_LoadVideo, LoadImage, Int, Int, Text, Note, PreviewImage, PreviewImage, GetNode, PointsEditor]
patterns: []
missing: []
---

# 平台全量/【二创优选】  Wan2.2 AV2+SeC遮罩（不丢帧、识别精确、速度快）_2031268309001310209.json

> 来源文件 `comfyui_library/workflows/平台全量/【二创优选】  Wan2.2 AV2+SeC遮罩（不丢帧、识别精确、速度快）_2031268309001310209.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（122 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `WanVideoDecode`
- `Note`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `SetNode`
- `Int`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `SeCVideoSegmentation`
- `InvertMask`
- `BlockifyMask`
- `PrimitiveInt`
- `WanVideoClipVisionEncode`
- `Note`
- `Note`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `DrawMaskOnImage`
- `SetNode`
- `ImageFromBatch`
- `VHS_VideoCombine`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SeCModelLoader`
- `Note`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerv2` ★核心
- `WanVideoSchedulerv2`
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoTeaCache`
- `OnnxDetectionModelLoader`
- `ImageFromBatch`
- `CoordinatePlotter`
- `CoordinatePlotter`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageBatch`
- `GetNode`
- `ImageBlend`
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `MaskPreview+`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `GrowMaskWithBlur`
- `PreviewImage`
- `GetNode`
- `BatchCount+`
- `RepeatImageBatch`
- `RHHiddenNodes`
- `BatchCount+`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `Int`
- `Int`
- `Text`
- `Note`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `PointsEditor`

## 知识

覆盖率 **48%**（59/122）

**有卡**：`ImageConcatMulti`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`Int`、`CLIPVisionLoader`、`VHS_VideoCombine`、`DrawViTPose`、`PoseAndFaceDetection`、`SeCVideoSegmentation`、`InvertMask`、`BlockifyMask`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`DrawMaskOnImage`、`ImageFromBatch`、`SeCModelLoader`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSamplerv2`、`WanVideoSchedulerv2`、`WanVideoSamplerExtraArgs`、`WanVideoTeaCache`、`OnnxDetectionModelLoader`、`CoordinatePlotter`、`ImageBatch`、`ImageBlend`、`MaskPreview+`、`WanVideoContextOptions`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`GrowMaskWithBlur`、`BatchCount+`、`RepeatImageBatch`、`RHHiddenNodes`、`VHS_LoadVideo`、`LoadImage`、`Text`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoSamplerExtraArgs、WanVideoSamplerv2、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader
