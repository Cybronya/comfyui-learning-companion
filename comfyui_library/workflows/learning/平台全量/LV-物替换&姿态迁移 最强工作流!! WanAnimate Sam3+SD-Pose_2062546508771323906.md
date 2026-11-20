---
key: 平台全量/LV-物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2062546508771323906.json
name: LV-物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2062546508771323906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LV-物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2062546508771323906.json
hash: d5a68e4ad662194a
coverage: 0.455172
learned_at: 2026-11-14 00:39:17
nodes: [SetNode, SetNode, WanVideoTorchCompileSettings, WanVideoClipVisionEncode, GetNode, WanVideoVAELoader, CLIPVisionLoader, PreviewAny, SetNode, SetNode, WanVideoSetBlockSwap, SetNode, SetNode, Note, Note, Note, Note, PlaySound|pysssss, Note, GetNode, SetNode, GetNode, MarkdownNote, WanVideoUni3C_ControlnetLoader, WanVideoEncode, SetNode, WanVideoBlockSwap, ImageFlip, GetNode, GetNode, WanVideoUni3C_embeds, GetNode, SetNode, easy sam3ModelLoader, easy sam3VideoModelExtraConfig, MaskToImage, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), GetNode, Note, DrawMaskOnImage, SetNode, Note, GetNode, GetNode, SetNode, GetNode, GetNode, SDPoseOODLoader, YOLOModelLoader, MarkdownNote, GetNode, VHS_VideoCombine, GetNode, WanVideoLoraSelectMulti, Fast Groups Bypasser (rgthree), VHS_VideoCombine, MarkdownNote, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoModelLoader, VHS_VideoCombine, VHS_VideoCombine, ImageBlend, LayerUtility: PurgeVRAM, Note, WanVideoContextOptions, Note, Seed (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), PreviewImage, GetNode, GetNode, ImageResizeKJv2, GetNode, easy framesEditor, easy sam3GetObjectMask, easy sam3GetObjectMask, VHS_VideoCombine, easy sam3Visualization, PreviewAny, MaskToImage, MaskToImage, easy sam3GetObjectIds, GrowMaskWithBlur, BlockifyMask, VHS_VideoCombine, easy sam3VideoSegmentation, Note, Note, Fast Groups Bypasser (rgthree), GetNode, GetNode, ImageConcatMulti, WanVideoTextEncodeCached, Note, GetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, Note, GetNode, WanVideoAnimateEmbeds, WanVideoSamplerSettings, WanVideoDecode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), GetNode, SetNode, GetNode, VHS_LoadVideo, GetNode, GetNode, ImageResizeKJv2, WanVideoSamplerFromSettings, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, FastUnsharpSharpen, SetNode, VHS_VideoInfoLoaded, LamCommonPrint, SDPoseOODProcessor, LoadImage, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/LV-物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2062546508771323906.json

> 来源文件 `comfyui_library/workflows/平台全量/LV-物替换&姿态迁移 最强工作流!! WanAnimate Sam3+SD-Pose_2062546508771323906.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（145 个）：
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `PreviewAny`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `Note`
- `PlaySound|pysssss`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `SetNode`
- `WanVideoBlockSwap`
- `ImageFlip`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `SetNode`
- `easy sam3ModelLoader`
- `easy sam3VideoModelExtraConfig`
- `MaskToImage`
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Note`
- `DrawMaskOnImage`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `MarkdownNote`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `MarkdownNote`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageBlend`
- `LayerUtility: PurgeVRAM`
- `Note`
- `WanVideoContextOptions`
- `Note`
- `Seed (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `easy framesEditor`
- `easy sam3GetObjectMask`
- `easy sam3GetObjectMask`
- `VHS_VideoCombine`
- `easy sam3Visualization`
- `PreviewAny`
- `MaskToImage`
- `MaskToImage`
- `easy sam3GetObjectIds`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `VHS_VideoCombine`
- `easy sam3VideoSegmentation`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoTextEncodeCached`
- `Note`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSamplerSettings` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoSamplerFromSettings` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `FastUnsharpSharpen`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `LamCommonPrint`
- `SDPoseOODProcessor`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **46%**（66/145）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`PlaySound|pysssss`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoBlockSwap`、`ImageFlip`、`WanVideoUni3C_embeds`、`easy sam3ModelLoader`、`easy sam3VideoModelExtraConfig`、`MaskToImage`、`INTConstant`、`DrawMaskOnImage`、`SDPoseOODLoader`、`YOLOModelLoader`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`ImageBlend`、`LayerUtility: PurgeVRAM`、`WanVideoContextOptions`、`Seed (rgthree)`、`Label (rgthree)`、`ImageResizeKJv2`、`easy framesEditor`、`easy sam3GetObjectMask`、`easy sam3Visualization`、`easy sam3GetObjectIds`、`GrowMaskWithBlur`、`BlockifyMask`、`easy sam3VideoSegmentation`、`ImageConcatMulti`、`WanVideoTextEncodeCached`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoAnimateEmbeds`、`WanVideoSamplerSettings`、`WanVideoDecode`、`VHS_LoadVideo`、`WanVideoSamplerFromSettings`、`FastUnsharpSharpen`、`VHS_VideoInfoLoaded`、`LamCommonPrint`、`SDPoseOODProcessor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode
