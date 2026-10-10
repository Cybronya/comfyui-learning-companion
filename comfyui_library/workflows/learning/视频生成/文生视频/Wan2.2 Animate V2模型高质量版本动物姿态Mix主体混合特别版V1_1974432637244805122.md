---
key: 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json
name: Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本动物姿态Mix主体混合特别版V1_1974432637244805122.json
hash: ef0ddc72db25f51d
coverage: 0.55814
learned_at: 2026-10-10 23:06:43
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, GetNode, WanVideoUni3C_embeds, Note, Note, SetNode, WanVideoTextEncodeCached, GrowMask, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, WanVideoClipVisionEncode, Note, VHS_LoadVideo, JWInteger, JWInteger, WanVideoLoraSelectMulti, WanVideoModelLoader, easy promptConcat, ShowText, RH_Captioner, easy showAnything, CR Prompt Text, WanVideoSampler, GetNode, SetNode, GetImageSizeAndCount, EmptyImage, CR Prompt Text, Reroute, VHS_VideoCombine, SetNode, SetNode, SetNode, BlockifyMask, PointsEditor, VHS_LoadVideo, LoadImage, WanVideoDecode, VHS_VideoCombine, JWInteger, PDIMAGE_LongerSize, ImageConcatMulti, ImageConcanate, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, AnimalPosePreprocessor, DrawMaskOnImage, LayerUtility: PurgeVRAM, PDIMAGE_LongerSize, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CR Prompt Text, CR Prompt Text, easy promptConcat]
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
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

覆盖率 **56%**（48/86）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`GrowMask`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`WanVideoUni3C_ControlnetLoader`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`JWInteger`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`ShowText`、`RH_Captioner`、`WanVideoSampler`、`EmptyImage`、`BlockifyMask`、`PointsEditor`、`LoadImage`、`WanVideoDecode`、`PDIMAGE_LongerSize`、`ImageConcanate`、`AnimalPosePreprocessor`、`DrawMaskOnImage`

**缺卡**（6）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`CR Prompt Text`、`CR Prompt Text`、`easy promptConcat`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
