---
key: 视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json
name: Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json
hash: 0544f7b8e02783c1
coverage: 0.445652
learned_at: 2026-10-10 23:08:15
nodes: [PreviewImage, WanVideoDecode, PreviewImage, VHS_VideoCombine, MarkdownNote, ImageResizeKJv2, ImageResizeKJv2, GroundingDinoSAMSegment (segment anything), PreviewImage, Bounded Image Crop, Bounded Image Crop with Mask, PreviewImage, Bounded Image Crop with Mask, Bounded Image Crop, PreviewImage, GrowMaskWithBlur, GroundingDinoSAMSegment (segment anything), PreviewImage, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, VHS_VideoInfo, SetNode, LoadImage, WanVideoLoraSelectMulti, Note, WanVideoExtraModelSelect, WanVideoExtraModelSelect, StringConstantMultiline, SAMModelLoader (segment anything), GroundingDinoModelLoader (segment anything), SetNode, SetNode, SetNode, SetNode, Note, GetImageSizeAndCount, GetNode, LoadAudio, VHS_LoadVideo, MultiTalkModelLoader, WanVideoExtraModelSelect, easy clearCacheAll, LayerUtility: PurgeVRAM V2, GetNode, DWPreprocessor, GetNode, GetNode, GetNode, MaskToImage, Mix Color By Mask, ImageFromBatch+, WanVideoAddLynxEmbeds, WanVideoVACEEncode, LynxEncodeFaceIP, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoContextOptions, LayerUtility: PurgeVRAM V2, GetNode, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, LayerUtility: PurgeVRAM V2, GetNode, WanVideoVACEEncode, WanVideoSampler, SetNode, GetNode, WanVideoTorchCompileSettings, SetNode, SetNode, ImageResizeKJv2, ImageResizeKJv2, MultiTalkWav2VecEmbeds, WanVideoVAELoader, DownloadAndLoadWav2VecModel, WanVideoModelLoader, LayerUtility: PurgeVRAM V2, GetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoTextEncodeCached, LoadLynxResampler]
patterns: []
missing: [Bounded Image Crop, Bounded Image Crop, Bounded Image Crop with Mask, Bounded Image Crop with Mask, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GroundingDinoSAMSegment (segment anything), ImageFromBatch+, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, Mix Color By Mask, SAMModelLoader (segment anything), easy clearCacheAll]
discoveries: [次要节点 `Bounded Image Crop` 知识库中没有该节点类型的任何知识, 次要节点 `Bounded Image Crop` 知识库中没有该节点类型的任何知识, 次要节点 `Bounded Image Crop with Mask` 知识库中没有该节点类型的任何知识, 次要节点 `Bounded Image Crop with Mask` 知识库中没有该节点类型的任何知识, 次要节点 `GroundingDinoModelLoader (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Mix Color By Mask` 知识库中没有该节点类型的任何知识, 次要节点 `SAMModelLoader (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
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

覆盖率 **45%**（41/92）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`INTConstant`、`VHS_VideoInfo`、`LoadImage`、`WanVideoLoraSelectMulti`、`WanVideoExtraModelSelect`、`StringConstantMultiline`、`GetImageSizeAndCount`、`LoadAudio`、`VHS_LoadVideo`、`MultiTalkModelLoader`、`DWPreprocessor`、`MaskToImage`、`WanVideoAddLynxEmbeds`、`WanVideoVACEEncode`、`LynxEncodeFaceIP`、`WanVideoContextOptions`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`MultiTalkWav2VecEmbeds`、`WanVideoVAELoader`、`DownloadAndLoadWav2VecModel`、`WanVideoModelLoader`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`LoadLynxResampler`

**缺卡**（17）：`Bounded Image Crop`、`Bounded Image Crop`、`Bounded Image Crop with Mask`、`Bounded Image Crop with Mask`、`GroundingDinoModelLoader (segment anything)`、`GroundingDinoSAMSegment (segment anything)`、`GroundingDinoSAMSegment (segment anything)`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`Mix Color By Mask`、`SAMModelLoader (segment anything)`、`easy clearCacheAll`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、LoadLynxResampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached

## 学习发现

- 次要节点 `Bounded Image Crop` 知识库中没有该节点类型的任何知识
- 次要节点 `Bounded Image Crop` 知识库中没有该节点类型的任何知识
- 次要节点 `Bounded Image Crop with Mask` 知识库中没有该节点类型的任何知识
- 次要节点 `Bounded Image Crop with Mask` 知识库中没有该节点类型的任何知识
- 次要节点 `GroundingDinoModelLoader (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `GroundingDinoSAMSegment (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Mix Color By Mask` 知识库中没有该节点类型的任何知识
- 次要节点 `SAMModelLoader (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
