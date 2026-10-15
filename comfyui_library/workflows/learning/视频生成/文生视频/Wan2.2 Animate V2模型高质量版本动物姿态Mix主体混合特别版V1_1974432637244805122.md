---
key: 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json
name: Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json
hash: ef0ddc72db25f51d
coverage: 0.627907
learned_at: 2026-10-15 22:47:09
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, GetNode, WanVideoUni3C_embeds, Note, Note, SetNode, WanVideoTextEncodeCached, GrowMask, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, WanVideoClipVisionEncode, Note, VHS_LoadVideo, JWInteger, JWInteger, WanVideoLoraSelectMulti, WanVideoModelLoader, easy promptConcat, ShowText, RH_Captioner, easy showAnything, CR Prompt Text, WanVideoSampler, GetNode, SetNode, GetImageSizeAndCount, EmptyImage, CR Prompt Text, Reroute, VHS_VideoCombine, SetNode, SetNode, SetNode, BlockifyMask, PointsEditor, VHS_LoadVideo, LoadImage, WanVideoDecode, VHS_VideoCombine, JWInteger, PDIMAGE_LongerSize, ImageConcatMulti, ImageConcanate, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, AnimalPosePreprocessor, DrawMaskOnImage, LayerUtility: PurgeVRAM, PDIMAGE_LongerSize, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（86 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoUni3C_embeds`
- `Note`
- `Note`
- `SetNode`
- `WanVideoTextEncodeCached`
- `GrowMask`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoClipVisionEncode`
- `Note`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `easy promptConcat`
- `ShowText`
- `RH_Captioner`
- `easy showAnything`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `EmptyImage`
- `CR Prompt Text`
- `Reroute`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `PointsEditor`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `JWInteger`
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `AnimalPosePreprocessor`
- `DrawMaskOnImage`
- `LayerUtility: PurgeVRAM`
- `PDIMAGE_LongerSize`
- `VHS_VideoCombine`

## 知识

覆盖率 **63%**（54/86）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`GrowMask`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`WanVideoUni3C_ControlnetLoader`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`JWInteger`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`easy promptConcat`、`ShowText`、`RH_Captioner`、`CR Prompt Text`、`WanVideoSampler`、`EmptyImage`、`BlockifyMask`、`PointsEditor`、`LoadImage`、`WanVideoDecode`、`PDIMAGE_LongerSize`、`ImageConcanate`、`LayerUtility: PurgeVRAM`、`AnimalPosePreprocessor`、`DrawMaskOnImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
