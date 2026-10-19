---
name: unknown_workflow_video_lora_sampler_553
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.76125
common_nodes: [GetImageSize, GetImageSizeAndCount, INTConstant, Image Blank, ImageCompositeMasked, ImageResizeKJ, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, LynxInsightFaceCrop, MaskToImage, PreviewImage, RH_Captioner, SolidMask, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy showAnything]
problems: []
missing: [Image Blank, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM]
members: [视频生成/文生视频/1975862492029169665.json, 视频生成/文生视频/1975863056892866561.json, 视频生成/文生视频/lynx-VACE-ID双一致性姿态视频引导视频生成_2072999520222617600.json, 视频生成/文生视频/lynx-VACE-ID双一致性文生视频_2072999520814014464.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_553

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1975862492029169665.json、视频生成/文生视频/1975863056892866561.json、视频生成/文生视频/lynx-VACE-ID双一致性姿态视频引导视频生成_2072999520222617600.json、视频生成/文生视频/lynx-VACE-ID双一致性文生视频_2072999520814014464.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSize`
- `GetImageSizeAndCount`
- `INTConstant`
- `Image Blank`
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `LynxInsightFaceCrop`
- `MaskToImage`
- `PreviewImage`
- `RH_Captioner`
- `SolidMask`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Image Blank、LayerMask: LoadFlorence2Model、LayerMask: ObjectDetectorFL2、LayerMask: SAM2Ultra、LayerUtility: PurgeVRAM
