---
key: 图片生成/图生图/【多角色替换+ 动作迁移 】影视恶搞+ 多遮罩模式控制Wan2.2 Animate_2001328127429275650.json
name: 【多角色替换+ 动作迁移 】影视恶搞+ 多遮罩模式控制Wan2.2 Animate_2001328127429275650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【多角色替换+ 动作迁移 】影视恶搞+ 多遮罩模式控制Wan2.2 Animate_2001328127429275650.json
hash: 5d241393e5bb0ffb
coverage: 0.638037
learned_at: 2026-10-23 11:49:51
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageUpscaleWithModelBatched, ImageFromBatch+, CR String To Number, Display Any (rgthree), GetImageSizeAndCount, ImageUpscaleWithModelBatched, ImageFromBatch+, UpscaleModelLoader, CM_IntToFloat, CR Text, CR Text, CR Text, easy imageIndexSwitch, RIFE VFI, RIFE VFI, Sam2Segmentation, LayerMask: ObjectDetectorMask, DownloadAndLoadQwenModel, Mute / Bypass Repeater (rgthree), Note, ImageFromBatch, BBoxesToSAM2, easy cleanGpuUsed, easy clearCacheAll, Mute / Bypass Relay (rgthree), DownloadAndLoadSAM2Model, ResizeMask, DrawMaskOnImage, FaceSegment, ClothesSegment, RMBG, BlockifyMask, InvertMask (segment anything), GrowMask, Fast Groups Bypasser (rgthree), Any Switch (rgthree), ImageResizeKJv2, Any Switch (rgthree), GetImageSize+, ImageToMask, CR Text, VHS_VideoCombine, Note, easy seed, easy cleanGpuUsed, QwenVLDetection, LayerMask: SAM2VideoUltra, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM, easy cleanGpuUsed, Note, Display Any (rgthree), ImageResizeKJv2, easy anythingIndexSwitch, Any Switch (rgthree), CR String To Number, Note, MathExpression|pysssss, CM_IntToFloat, CR Text, VHS_VideoInfo, Display Any (rgthree), MathExpression|pysssss, Display Any (rgthree), VHS_VideoInfo, MathExpression|pysssss, CM_IntToFloat, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, GetImageSize, CR Float To String, ShowText|pysssss, Note, Note, Fast Groups Muter (rgthree), PointsEditor, LayerMask: DrawBBoxMaskV2, easy cleanGpuUsed, MarkdownNote, Note, WanVideoTextEncodeCached, WanVideoSetBlockSwap, Fast Groups Muter (rgthree), LoadImage, Fast Groups Muter (rgthree), VHS_VideoCombine, GetNode, SetNode, SetNode, SetNode, ImageResizeKJ, SetNode, GetNode, WanVideoDecode, Any Switch (rgthree), CR Integer To String, ShowText|pysssss, WanVideoSetLoRAs, WanVideoBlockSwap, LayerUtility: PurgeVRAM V2, WanVideoSampler, LayerUtility: PurgeVRAM V2, GetNode, GetImageSize+, PixelPerfectResolution, DrawViTPose, LayerUtility: PurgeVRAM V2, PoseAndFaceDetection, PreviewImage, ImageFromBatch, easy int, CropFace, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, DWPreprocessor, easy int, UpscaleModelLoader, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoVAELoader, WanVideoModelLoader, Fast Groups Muter (rgthree), VHS_LoadVideo, LoadImage, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/【多角色替换+ 动作迁移 】影视恶搞+ 多遮罩模式控制Wan2.2 Animate_2001328127429275650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【多角色替换+ 动作迁移 】影视恶搞+ 多遮罩模式控制Wan2.2 Animate_2001328127429275650.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（163 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageUpscaleWithModelBatched`
- `ImageFromBatch+`
- `CR String To Number`
- `Display Any (rgthree)`
- `GetImageSizeAndCount`
- `ImageUpscaleWithModelBatched`
- `ImageFromBatch+`
- `UpscaleModelLoader`
- `CM_IntToFloat`
- `CR Text`
- `CR Text`
- `CR Text`
- `easy imageIndexSwitch`
- `RIFE VFI`
- `RIFE VFI`
- `Sam2Segmentation`
- `LayerMask: ObjectDetectorMask`
- `DownloadAndLoadQwenModel`
- `Mute / Bypass Repeater (rgthree)`
- `Note`
- `ImageFromBatch`
- `BBoxesToSAM2`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `Mute / Bypass Relay (rgthree)`
- `DownloadAndLoadSAM2Model`
- `ResizeMask`
- `DrawMaskOnImage`
- `FaceSegment`
- `ClothesSegment`
- `RMBG`
- `BlockifyMask`
- `InvertMask (segment anything)`
- `GrowMask`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `ImageResizeKJv2`
- `Any Switch (rgthree)`
- `GetImageSize+`
- `ImageToMask`
- `CR Text`
- `VHS_VideoCombine`
- `Note`
- `easy seed`
- `easy cleanGpuUsed`
- `QwenVLDetection`
- `LayerMask: SAM2VideoUltra`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `Note`
- `Display Any (rgthree)`
- `ImageResizeKJv2`
- `easy anythingIndexSwitch`
- `Any Switch (rgthree)`
- `CR String To Number`
- `Note`
- `MathExpression|pysssss`
- `CM_IntToFloat`
- `CR Text`
- `VHS_VideoInfo`
- `Display Any (rgthree)`
- `MathExpression|pysssss`
- `Display Any (rgthree)`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `CM_IntToFloat`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetImageSize`
- `CR Float To String`
- `ShowText|pysssss`
- `Note`
- `Note`
- `Fast Groups Muter (rgthree)`
- `PointsEditor`
- `LayerMask: DrawBBoxMaskV2`
- `easy cleanGpuUsed`
- `MarkdownNote`
- `Note`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `Any Switch (rgthree)`
- `CR Integer To String`
- `ShowText|pysssss`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `GetImageSize+`
- `PixelPerfectResolution`
- `DrawViTPose`
- `LayerUtility: PurgeVRAM V2`
- `PoseAndFaceDetection`
- `PreviewImage`
- `ImageFromBatch`
- `easy int`
- `CropFace`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `PreviewImage`
- `DWPreprocessor`
- `easy int`
- `UpscaleModelLoader`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `Fast Groups Muter (rgthree)`
- `VHS_LoadVideo`
- `LoadImage`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **64%**（104/163）

**有卡**：`GetImageSizeAndCount`、`ImageUpscaleWithModelBatched`、`ImageFromBatch+`、`CR String To Number`、`Display Any (rgthree)`、`UpscaleModelLoader`、`CM_IntToFloat`、`CR Text`、`easy imageIndexSwitch`、`RIFE VFI`、`Sam2Segmentation`、`LayerMask: ObjectDetectorMask`、`DownloadAndLoadQwenModel`、`Mute / Bypass Repeater (rgthree)`、`ImageFromBatch`、`BBoxesToSAM2`、`easy cleanGpuUsed`、`easy clearCacheAll`、`Mute / Bypass Relay (rgthree)`、`DownloadAndLoadSAM2Model`、`ResizeMask`、`DrawMaskOnImage`、`FaceSegment`、`ClothesSegment`、`RMBG`、`BlockifyMask`、`InvertMask (segment anything)`、`GrowMask`、`ImageResizeKJv2`、`GetImageSize+`、`ImageToMask`、`VHS_VideoCombine`、`easy seed`、`QwenVLDetection`、`LayerMask: SAM2VideoUltra`、`LayerUtility: PurgeVRAM`、`easy anythingIndexSwitch`、`MathExpression|pysssss`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`GetImageSize`、`CR Float To String`、`PointsEditor`、`LayerMask: DrawBBoxMaskV2`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`LoadImage`、`ImageResizeKJ`、`WanVideoDecode`、`CR Integer To String`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM V2`、`WanVideoSampler`、`PixelPerfectResolution`、`DrawViTPose`、`PoseAndFaceDetection`、`easy int`、`CropFace`、`DWPreprocessor`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
