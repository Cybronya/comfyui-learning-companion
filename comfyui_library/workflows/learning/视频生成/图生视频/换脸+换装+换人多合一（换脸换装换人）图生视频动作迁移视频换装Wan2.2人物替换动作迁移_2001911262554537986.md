---
key: 视频生成/图生视频/换脸+换装+换人多合一（换脸换装换人）图生视频动作迁移视频换装Wan2.2人物替换动作迁移_2001911262554537986.json
name: 换脸+换装+换人多合一（换脸换装换人）图生视频动作迁移视频换装Wan2.2人物替换动作迁移_2001911262554537986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/换脸+换装+换人多合一（换脸换装换人）图生视频动作迁移视频换装Wan2.2人物替换动作迁移_2001911262554537986.json
hash: acab1502ded9da37
coverage: 0.662791
learned_at: 2026-10-15 22:33:47
nodes: [GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, WanVideoAnimateEmbeds, CLIPVisionLoader, GetNode, ImageResizeKJv2, ImageCropByMaskAndResize, DWPreprocessor, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, LayerUtility: PurgeVRAM, JWInteger, JWInteger, FaceMaskFromPoseKeypoints, PixelPerfectResolution, Reroute, WanVideoBlockSwap, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, CR Text, Int, MathExpression|pysssss, Int, MathExpression|pysssss, easy cleanGpuUsed, ImageConcatMulti, ImageConcatMulti, Int, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, PreviewImage, LoadImage, SetNode, DrawMaskOnImage, GetNode, easy imageBatchToImageList, MaskListToMaskBatch, SetNode, LoadSAM3Model, easy sam3VideoSegmentation, easy imageListToImageBatch, LayerMask: SegformerB2ClothesUltra, GrowMask, BlockifyMask, MaskToImage, LoadImage, LoadImage, WanVideoSampler, WanVideoDecode, CR Text, SetNode, SetNode, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, SetNode, VHS_VideoInfo, PreviewImage, VHS_VideoCombine, RH_Translator, easy sam3ModelLoader, GetNode, Int, SAM3Segmentation, PreviewImage, MaskToImage, VHS_VideoCombine, PreviewImage, LayerUtility: PurgeVRAM V2, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/换脸+换装+换人多合一（换脸换装换人）图生视频动作迁移视频换装Wan2.2人物替换动作迁移_2001911262554537986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001911262554537986.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（86 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `LayerUtility: PurgeVRAM`
- `JWInteger`
- `JWInteger`
- `FaceMaskFromPoseKeypoints`
- `PixelPerfectResolution`
- `Reroute`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `CR Text`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `MathExpression|pysssss`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `Int`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `easy imageBatchToImageList`
- `MaskListToMaskBatch`
- `SetNode`
- `LoadSAM3Model`
- `easy sam3VideoSegmentation`
- `easy imageListToImageBatch`
- `LayerMask: SegformerB2ClothesUltra`
- `GrowMask`
- `BlockifyMask`
- `MaskToImage`
- `LoadImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `CR Text`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `VHS_VideoInfo`
- `PreviewImage`
- `VHS_VideoCombine`
- `RH_Translator`
- `easy sam3ModelLoader`
- `GetNode`
- `Int`
- `SAM3Segmentation`
- `PreviewImage`
- `MaskToImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`

## 知识

覆盖率 **66%**（57/86）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`ImageResizeKJv2`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`JWInteger`、`FaceMaskFromPoseKeypoints`、`PixelPerfectResolution`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`CR Text`、`Int`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`ImageConcatMulti`、`LoadImage`、`DrawMaskOnImage`、`easy imageBatchToImageList`、`MaskListToMaskBatch`、`LoadSAM3Model`、`easy sam3VideoSegmentation`、`easy imageListToImageBatch`、`LayerMask: SegformerB2ClothesUltra`、`GrowMask`、`BlockifyMask`、`MaskToImage`、`WanVideoSampler`、`WanVideoDecode`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfo`、`VHS_VideoCombine`、`RH_Translator`、`easy sam3ModelLoader`、`SAM3Segmentation`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
