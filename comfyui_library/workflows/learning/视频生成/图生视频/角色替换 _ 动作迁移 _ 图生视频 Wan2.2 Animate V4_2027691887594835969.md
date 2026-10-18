---
key: 视频生成/图生视频/角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate V4_2027691887594835969.json
name: 角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate V4_2027691887594835969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate V4_2027691887594835969.json
hash: 5cdf6841c1cca2e6
coverage: 0.666667
learned_at: 2026-10-15 22:35:18
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, Display Any (rgthree), ImageFromBatch+, CR String To Number, CR String To Number, Display Any (rgthree), GetImageSizeAndCount, ImageUpscaleWithModelBatched, Display Any (rgthree), ImageFromBatch+, CM_IntToFloat, CM_IntToFloat, CR Text, CR Text, Display Any (rgthree), MathExpression|pysssss, VHS_VideoInfo, VHS_VideoInfo, ImageConcatMulti, ImageConcatMulti, LayerUtility: PurgeVRAM V2, Fast Groups Muter (rgthree), CR Integer To String, Note, ImageResizeKJ, easy imageIndexSwitch, WanVideoSetLoRAs, GetImageSizeAndCount, UpscaleModelLoader, ImageUpscaleWithModelBatched, ShowText|pysssss, MathExpression|pysssss, FaceMaskFromPoseKeypoints, UpscaleModelLoader, Note, WanVideoBlockSwap, Note, CropFace, ImageScale, VHS_VideoCombine, VHS_VideoCombine, easy anythingIndexSwitch, VHS_VideoInfo, MathExpression|pysssss, VHS_VideoInfo, MathExpression|pysssss, CR Text, Any Switch (rgthree), Any Switch (rgthree), WanVideoVAELoader, Note, ReActorFaceSwap, CropFace, LayerUtility: PurgeVRAM V2, DWPreprocessor, LayerUtility: PurgeVRAM V2, RIFE VFI, RIFE VFI, Note, PreviewImage, PreviewImage, Fast Groups Muter (rgthree), Reroute, WanVideoDecode, CM_IntToFloat, MathExpression|pysssss, CM_IntToFloat, RIFE VFI, CR Text, WanVideoTextEncodeCached, CR Text, Note, Float, easy int, LoadImage, VHS_LoadVideo, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, CLIPVisionLoader, WanVideoAnimateEmbeds, PixelPerfectResolution, GetImageSize+, WanVideoClipVisionEncode, ImageResizeKJv2, WanVideoSampler, GetImageSize, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/角色替换 _ 动作迁移 _ 图生视频 Wan2.2 Animate V4_2027691887594835969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027691887594835969.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（114 个）：
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
- `GetImageSizeAndCount`
- `Display Any (rgthree)`
- `ImageFromBatch+`
- `CR String To Number`
- `CR String To Number`
- `Display Any (rgthree)`
- `GetImageSizeAndCount`
- `ImageUpscaleWithModelBatched`
- `Display Any (rgthree)`
- `ImageFromBatch+`
- `CM_IntToFloat`
- `CM_IntToFloat`
- `CR Text`
- `CR Text`
- `Display Any (rgthree)`
- `MathExpression|pysssss`
- `VHS_VideoInfo`
- `VHS_VideoInfo`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LayerUtility: PurgeVRAM V2`
- `Fast Groups Muter (rgthree)`
- `CR Integer To String`
- `Note`
- `ImageResizeKJ`
- `easy imageIndexSwitch`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `UpscaleModelLoader`
- `ImageUpscaleWithModelBatched`
- `ShowText|pysssss`
- `MathExpression|pysssss`
- `FaceMaskFromPoseKeypoints`
- `UpscaleModelLoader`
- `Note`
- `WanVideoBlockSwap`
- `Note`
- `CropFace`
- `ImageScale`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `CR Text`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `WanVideoVAELoader`
- `Note`
- `ReActorFaceSwap`
- `CropFace`
- `LayerUtility: PurgeVRAM V2`
- `DWPreprocessor`
- `LayerUtility: PurgeVRAM V2`
- `RIFE VFI`
- `RIFE VFI`
- `Note`
- `PreviewImage`
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `Reroute`
- `WanVideoDecode`
- `CM_IntToFloat`
- `MathExpression|pysssss`
- `CM_IntToFloat`
- `RIFE VFI`
- `CR Text`
- `WanVideoTextEncodeCached`
- `CR Text`
- `Note`
- `Float`
- `easy int`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`
- `WanVideoAnimateEmbeds`
- `PixelPerfectResolution`
- `GetImageSize+`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `GetImageSize`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`

## 知识

覆盖率 **67%**（76/114）

**有卡**：`GetImageSizeAndCount`、`Display Any (rgthree)`、`ImageFromBatch+`、`CR String To Number`、`ImageUpscaleWithModelBatched`、`CM_IntToFloat`、`CR Text`、`MathExpression|pysssss`、`VHS_VideoInfo`、`ImageConcatMulti`、`LayerUtility: PurgeVRAM V2`、`CR Integer To String`、`ImageResizeKJ`、`easy imageIndexSwitch`、`WanVideoSetLoRAs`、`UpscaleModelLoader`、`FaceMaskFromPoseKeypoints`、`WanVideoBlockSwap`、`CropFace`、`ImageScale`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`WanVideoVAELoader`、`ReActorFaceSwap`、`DWPreprocessor`、`RIFE VFI`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`Float`、`easy int`、`LoadImage`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`CLIPVisionLoader`、`WanVideoAnimateEmbeds`、`PixelPerfectResolution`、`GetImageSize+`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`WanVideoSampler`、`GetImageSize`、`WanVideoSetBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
