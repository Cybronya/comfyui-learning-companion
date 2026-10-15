---
key: 视频生成/文生视频/Wan2.2-Stand-in人脸一致性保持_2004807715740413953.json
name: Wan2.2-Stand-in人脸一致性保持_2004807715740413953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-Stand-in人脸一致性保持_2004807715740413953.json
hash: b56e77f9df0a0d90
coverage: 0.867925
learned_at: 2026-10-15 22:47:12
nodes: [WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, GetImageSizeAndCount, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVAELoader, LynxInsightFaceCrop, PreviewImage, OnnxDetectionModelLoader, InvertMask, WanVideoSampler, VHS_VideoCombine, PoseAndFaceDetection, WanVideoEncode, FaceProcessorLoader, PreviewImage, ImageRemoveBackground+, TransparentBGSession+, DrawMaskOnImage, PreviewImage, ImagePadKJ, PreviewImage, ImageResizeKJv2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, LoadImage, WanVideoTextEncodeCached, LynxEncodeFaceIP, WanVideoAddStandInLatent, WanVideoAddLynxEmbeds, LoadLynxResampler, WanVideoExtraModelSelect, WanVideoExtraModelSelect, PrimitiveInt, PrimitiveInt, WanVideoEmptyEmbeds, WanVideoModelLoader, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, GetImageSizeAndCount, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVAELoader, LynxInsightFaceCrop, PreviewImage, OnnxDetectionModelLoader, InvertMask, WanVideoSampler, VHS_VideoCombine, PoseAndFaceDetection, WanVideoEncode, ApplyFaceProcessor, FaceProcessorLoader, MinNode, PreviewImage, ImageRemoveBackground+, TransparentBGSession+, DrawMaskOnImage, PreviewImage, ImagePadKJ, PreviewImage, ImageResizeKJv2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, WanVideoTextEncodeCached, LynxEncodeFaceIP, WanVideoAddLynxEmbeds, LoadLynxResampler, WanVideoExtraModelSelect, WanVideoExtraModelSelect, PrimitiveInt, PrimitiveInt, WanVideoEmptyEmbeds, WanVideoModelLoader, easy showAnything, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoTextEncode, WanVideoAddStandInLatent, ApplyFaceProcessor, MinNode, easy showAnything]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-Stand-in人脸一致性保持_2004807715740413953.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-Stand-in人脸一致性保持_2004807715740413953.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（106 个）：
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `InvertMask`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `WanVideoEncode`
- `FaceProcessorLoader`
- `PreviewImage`
- `ImageRemoveBackground+`
- `TransparentBGSession+`
- `DrawMaskOnImage`
- `PreviewImage`
- `ImagePadKJ`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `LynxEncodeFaceIP`
- `WanVideoAddStandInLatent`
- `WanVideoAddLynxEmbeds`
- `LoadLynxResampler` ★核心
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LynxInsightFaceCrop`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `InvertMask`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `WanVideoEncode`
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `MinNode`
- `PreviewImage`
- `ImageRemoveBackground+`
- `TransparentBGSession+`
- `DrawMaskOnImage`
- `PreviewImage`
- `ImagePadKJ`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `LynxEncodeFaceIP`
- `WanVideoAddLynxEmbeds`
- `LoadLynxResampler` ★核心
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `easy showAnything`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `WanVideoAddStandInLatent`
- `ApplyFaceProcessor`
- `MinNode`
- `easy showAnything`

## 知识

覆盖率 **87%**（92/106）

**有卡**：`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LynxInsightFaceCrop`、`OnnxDetectionModelLoader`、`InvertMask`、`PoseAndFaceDetection`、`WanVideoEncode`、`FaceProcessorLoader`、`ImageRemoveBackground+`、`TransparentBGSession+`、`DrawMaskOnImage`、`ImagePadKJ`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`LoadImage`、`WanVideoTextEncodeCached`、`LynxEncodeFaceIP`、`WanVideoAddStandInLatent`、`WanVideoAddLynxEmbeds`、`LoadLynxResampler`、`WanVideoExtraModelSelect`、`WanVideoEmptyEmbeds`、`INTConstant`、`CreateCFGScheduleFloatList`、`ApplyFaceProcessor`、`MinNode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
