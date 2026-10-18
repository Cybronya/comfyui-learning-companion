---
key: 视频生成/图生视频/WanAnimate_V9高质量动作迁移High‑quality motion transfer_2100757667223523330.json
name: WanAnimate_V9高质量动作迁移High‑quality motion transfer_2100757667223523330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WanAnimate_V9高质量动作迁移High‑quality motion transfer_2100757667223523330.json
hash: 52155e8600bee9fc
coverage: 0.597938
learned_at: 2026-10-17 02:14:42
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoSetBlockSwap, SetNode, MarkdownNote, Note, WanVideoDecode, CLIPVisionLoader, MarkdownNote, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, SetNode, INTConstant, CR SDXL Aspect Ratio, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoSetLoRAs, WanVideoVAELoader, ImageConcatMulti, ImageConcatMulti, GetNode, GetImageSizeAndCount, PrimitiveString, CR Text Concatenate, WanVideoContextOptions, WanVideoLoraSelectMulti, VHS_VideoCombine, GetNode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, easy cleanGpuUsed, Note, CR Clamp Value, NumberClamp, VHS_VideoCombine, SetNode, Note, SetNode, SAM3Segmentation, GetImageSizeAndCount, OnnxDetectionModelLoader, DrawViTPose, PoseAndFaceDetection, BlockifyMask, easy cleanGpuUsed, GrowMaskWithBlur, DownloadAndLoadSAM2Model, ImageResizeKJv2, Image Crop Face, WanVideoSampler, GrowMaskWithBlur, Sam2Segmentation, BlockifyMask, GetNode, FlashVSRNode, Sam2Segmentation, easy cleanGpuUsed, easy ifElse, SetNode, easy ifElse, DrawMaskOnImage, GetNode, VHS_VideoInfoLoaded, easy cleanGpuUsed, SaveImage, DetectFaces, VHS_VideoCombine, CropFace, CropFaces, SaveImage, PrimitiveInt, PrimitiveInt, WanVideoBlockSwap, VHS_LoadVideo, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, LoadImage, PrimitiveInt, PrimitiveBoolean, PrimitiveString, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WanAnimate_V9高质量动作迁移High‑quality motion transfer_2100757667223523330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/WanAnimate_V9高质量动作迁移High‑quality motion transfer_2100757667223523330.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（97 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `MarkdownNote`
- `Note`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `CR SDXL Aspect Ratio`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetImageSizeAndCount`
- `PrimitiveString`
- `CR Text Concatenate`
- `WanVideoContextOptions`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `Note`
- `CR Clamp Value`
- `NumberClamp`
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `SetNode`
- `SAM3Segmentation`
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `easy cleanGpuUsed`
- `GrowMaskWithBlur`
- `DownloadAndLoadSAM2Model`
- `ImageResizeKJv2`
- `Image Crop Face`
- `WanVideoSampler` ★核心
- `GrowMaskWithBlur`
- `Sam2Segmentation`
- `BlockifyMask`
- `GetNode`
- `FlashVSRNode`
- `Sam2Segmentation`
- `easy cleanGpuUsed`
- `easy ifElse`
- `SetNode`
- `easy ifElse`
- `DrawMaskOnImage`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `easy cleanGpuUsed`
- `SaveImage`
- `DetectFaces`
- `VHS_VideoCombine`
- `CropFace`
- `CropFaces`
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveString`
- `VHS_VideoCombine`

## 知识

覆盖率 **60%**（58/97）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoDecode`、`CLIPVisionLoader`、`INTConstant`、`CR SDXL Aspect Ratio`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`ImageConcatMulti`、`GetImageSizeAndCount`、`CR Text Concatenate`、`WanVideoContextOptions`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`CR Clamp Value`、`NumberClamp`、`SAM3Segmentation`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`BlockifyMask`、`GrowMaskWithBlur`、`DownloadAndLoadSAM2Model`、`ImageResizeKJv2`、`Image Crop Face`、`WanVideoSampler`、`Sam2Segmentation`、`FlashVSRNode`、`DrawMaskOnImage`、`VHS_VideoInfoLoaded`、`SaveImage`、`DetectFaces`、`CropFace`、`CropFaces`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`WanVideoModelLoader`、`LoadImage`、`PrimitiveBoolean`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
