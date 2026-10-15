---
key: 视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json
name: Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json
hash: 0544f7b8e02783c1
coverage: 0.630435
learned_at: 2026-10-15 22:47:16
nodes: [PreviewImage, WanVideoDecode, PreviewImage, VHS_VideoCombine, MarkdownNote, ImageResizeKJv2, ImageResizeKJv2, GroundingDinoSAMSegment (segment anything), PreviewImage, Bounded Image Crop, Bounded Image Crop with Mask, PreviewImage, Bounded Image Crop with Mask, Bounded Image Crop, PreviewImage, GrowMaskWithBlur, GroundingDinoSAMSegment (segment anything), PreviewImage, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, VHS_VideoInfo, SetNode, LoadImage, WanVideoLoraSelectMulti, Note, WanVideoExtraModelSelect, WanVideoExtraModelSelect, StringConstantMultiline, SAMModelLoader (segment anything), GroundingDinoModelLoader (segment anything), SetNode, SetNode, SetNode, SetNode, Note, GetImageSizeAndCount, GetNode, LoadAudio, VHS_LoadVideo, MultiTalkModelLoader, WanVideoExtraModelSelect, easy clearCacheAll, LayerUtility: PurgeVRAM V2, GetNode, DWPreprocessor, GetNode, GetNode, GetNode, MaskToImage, Mix Color By Mask, ImageFromBatch+, WanVideoAddLynxEmbeds, WanVideoVACEEncode, LynxEncodeFaceIP, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoContextOptions, LayerUtility: PurgeVRAM V2, GetNode, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM V2, GetNode, WanVideoVACEEncode, WanVideoSampler, SetNode, GetNode, WanVideoTorchCompileSettings, SetNode, SetNode, ImageResizeKJv2, ImageResizeKJv2, MultiTalkWav2VecEmbeds, WanVideoVAELoader, DownloadAndLoadWav2VecModel, WanVideoModelLoader, LayerUtility: PurgeVRAM V2, GetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoTextEncodeCached, LoadLynxResampler]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（92 个）：
- `PreviewImage`
- `WanVideoDecode`
- `PreviewImage`
- `VHS_VideoCombine`
- `MarkdownNote`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GroundingDinoSAMSegment (segment anything)`
- `PreviewImage`
- `Bounded Image Crop`
- `Bounded Image Crop with Mask`
- `PreviewImage`
- `Bounded Image Crop with Mask`
- `Bounded Image Crop`
- `PreviewImage`
- `GrowMaskWithBlur`
- `GroundingDinoSAMSegment (segment anything)`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `VHS_VideoInfo`
- `SetNode`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `Note`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `StringConstantMultiline`
- `SAMModelLoader (segment anything)`
- `GroundingDinoModelLoader (segment anything)`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetImageSizeAndCount`
- `GetNode`
- `LoadAudio`
- `VHS_LoadVideo`
- `MultiTalkModelLoader`
- `WanVideoExtraModelSelect`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `MaskToImage`
- `Mix Color By Mask`
- `ImageFromBatch+`
- `WanVideoAddLynxEmbeds`
- `WanVideoVACEEncode`
- `LynxEncodeFaceIP`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoContextOptions`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `MultiTalkWav2VecEmbeds`
- `WanVideoVAELoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTextEncodeCached`
- `LoadLynxResampler` ★核心

## 知识

覆盖率 **63%**（58/92）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`GroundingDinoSAMSegment (segment anything)`、`Bounded Image Crop`、`Bounded Image Crop with Mask`、`GrowMaskWithBlur`、`INTConstant`、`VHS_VideoInfo`、`LoadImage`、`WanVideoLoraSelectMulti`、`WanVideoExtraModelSelect`、`StringConstantMultiline`、`SAMModelLoader (segment anything)`、`GroundingDinoModelLoader (segment anything)`、`GetImageSizeAndCount`、`LoadAudio`、`VHS_LoadVideo`、`MultiTalkModelLoader`、`easy clearCacheAll`、`LayerUtility: PurgeVRAM V2`、`DWPreprocessor`、`MaskToImage`、`Mix Color By Mask`、`ImageFromBatch+`、`WanVideoAddLynxEmbeds`、`WanVideoVACEEncode`、`LynxEncodeFaceIP`、`WanVideoContextOptions`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`MultiTalkWav2VecEmbeds`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`LoadLynxResampler`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached
