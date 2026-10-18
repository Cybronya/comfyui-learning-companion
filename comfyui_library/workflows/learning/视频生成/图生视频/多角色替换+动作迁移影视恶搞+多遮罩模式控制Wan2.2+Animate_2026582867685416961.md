---
key: 视频生成/图生视频/多角色替换+动作迁移影视恶搞+多遮罩模式控制Wan2.2+Animate_2026582867685416961.json
name: 多角色替换+动作迁移影视恶搞+多遮罩模式控制Wan2.2+Animate_2026582867685416961.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多角色替换+动作迁移影视恶搞+多遮罩模式控制Wan2.2+Animate_2026582867685416961.json
hash: c6bb6163d404d500
coverage: 0.638037
learned_at: 2026-10-15 22:35:14
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageUpscaleWithModelBatched, ImageFromBatch+, CR String To Number, Display Any (rgthree), GetImageSizeAndCount, ImageUpscaleWithModelBatched, ImageFromBatch+, UpscaleModelLoader, CM_IntToFloat, CR Text, CR Text, CR Text, easy imageIndexSwitch, RIFE VFI, RIFE VFI, Sam2Segmentation, LayerMask: ObjectDetectorMask, DownloadAndLoadQwenModel, Mute / Bypass Repeater (rgthree), Note, ImageFromBatch, BBoxesToSAM2, easy cleanGpuUsed, easy clearCacheAll, Mute / Bypass Relay (rgthree), DownloadAndLoadSAM2Model, ResizeMask, DrawMaskOnImage, FaceSegment, ClothesSegment, RMBG, BlockifyMask, InvertMask (segment anything), GrowMask, Fast Groups Bypasser (rgthree), Any Switch (rgthree), ImageResizeKJv2, Any Switch (rgthree), GetImageSize+, ImageToMask, CR Text, VHS_VideoCombine, easy seed, easy cleanGpuUsed, QwenVLDetection, LayerMask: SAM2VideoUltra, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM, easy cleanGpuUsed, Note, Display Any (rgthree), ImageResizeKJv2, easy anythingIndexSwitch, Any Switch (rgthree), CR String To Number, Note, MathExpression|pysssss, CM_IntToFloat, CR Text, VHS_VideoInfo, Display Any (rgthree), MathExpression|pysssss, Display Any (rgthree), VHS_VideoInfo, MathExpression|pysssss, CM_IntToFloat, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, GetImageSize, CR Float To String, ShowText|pysssss, Note, Fast Groups Muter (rgthree), PointsEditor, LayerMask: DrawBBoxMaskV2, easy cleanGpuUsed, MarkdownNote, Note, WanVideoTextEncodeCached, WanVideoSetBlockSwap, Fast Groups Muter (rgthree), LoadImage, Fast Groups Muter (rgthree), VHS_VideoCombine, GetNode, SetNode, SetNode, SetNode, ImageResizeKJ, SetNode, GetNode, WanVideoDecode, Any Switch (rgthree), CR Integer To String, ShowText|pysssss, WanVideoSetLoRAs, WanVideoBlockSwap, LayerUtility: PurgeVRAM V2, WanVideoSampler, LayerUtility: PurgeVRAM V2, GetNode, GetImageSize+, PixelPerfectResolution, DrawViTPose, LayerUtility: PurgeVRAM V2, PoseAndFaceDetection, PreviewImage, ImageFromBatch, easy int, CropFace, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, DWPreprocessor, easy int, UpscaleModelLoader, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoVAELoader, WanVideoModelLoader, Fast Groups Muter (rgthree), VHS_LoadVideo, Fast Groups Muter (rgthree), LoadImage, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/多角色替换+动作迁移影视恶搞+多遮罩模式控制Wan2.2+Animate_2026582867685416961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2026582867685416961.json`

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
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `Note`
- `Note`

## 知识

覆盖率 **64%**（104/163）

**有卡**：`GetImageSizeAndCount`、`ImageUpscaleWithModelBatched`、`ImageFromBatch+`、`CR String To Number`、`Display Any (rgthree)`、`UpscaleModelLoader`、`CM_IntToFloat`、`CR Text`、`easy imageIndexSwitch`、`RIFE VFI`、`Sam2Segmentation`、`LayerMask: ObjectDetectorMask`、`DownloadAndLoadQwenModel`、`Mute / Bypass Repeater (rgthree)`、`ImageFromBatch`、`BBoxesToSAM2`、`easy cleanGpuUsed`、`easy clearCacheAll`、`Mute / Bypass Relay (rgthree)`、`DownloadAndLoadSAM2Model`、`ResizeMask`、`DrawMaskOnImage`、`FaceSegment`、`ClothesSegment`、`RMBG`、`BlockifyMask`、`InvertMask (segment anything)`、`GrowMask`、`ImageResizeKJv2`、`GetImageSize+`、`ImageToMask`、`VHS_VideoCombine`、`easy seed`、`QwenVLDetection`、`LayerMask: SAM2VideoUltra`、`LayerUtility: PurgeVRAM`、`easy anythingIndexSwitch`、`MathExpression|pysssss`、`VHS_VideoInfo`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`GetImageSize`、`CR Float To String`、`PointsEditor`、`LayerMask: DrawBBoxMaskV2`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`LoadImage`、`ImageResizeKJ`、`WanVideoDecode`、`CR Integer To String`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM V2`、`WanVideoSampler`、`PixelPerfectResolution`、`DrawViTPose`、`PoseAndFaceDetection`、`easy int`、`CropFace`、`DWPreprocessor`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
