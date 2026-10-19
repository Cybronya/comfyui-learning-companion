---
name: unknown_workflow_controlnet_video_lora_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.605
common_nodes: [ACE_ImageFaceCrop, ApplyPoseScalesToFrames, BlockifyMask, CLIPVisionLoader, CR Prompt Text, CalculatePoseScales, ConvertPoseToStandardFormat, DWPreprocessor, DownloadAndLoadQwenModel, DownloadAndLoadSAM2Model, DrawMaskOnImage, DrawViTPose, EmptyImage, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSizeAndCount, GetNode, GrowMask, INTConstant, ImageConcatMulti, ImageResizeKJv2, JWImageExtractFromBatch, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, OnnxDetectionModelLoader, PixelPerfectResolution, PoseAndFaceDetection, PreviewImage, QwenVLDetection, RenderKps, Sam2Segmentation, SetNode, Show any to JSON [Crystools], VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy ifElse, easy seed, huchenlei.LoadOpenposeJSON]
problems: []
missing: [LayerUtility: PurgeVRAM V2, Show any to JSON [Crystools], CR Prompt Text, easy seed, huchenlei.LoadOpenposeJSON]
members: [视频生成/文生视频/1970420554413076481.json, 视频生成/文生视频/Wan-Animate通用节点组_2072999544880930816.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1970420554413076481.json、视频生成/文生视频/Wan-Animate通用节点组_2072999544880930816.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_ImageFaceCrop`
- `ApplyPoseScalesToFrames`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CalculatePoseScales`
- `ConvertPoseToStandardFormat`
- `DWPreprocessor`
- `DownloadAndLoadQwenModel`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `DrawViTPose`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JWImageExtractFromBatch`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `OnnxDetectionModelLoader`
- `PixelPerfectResolution`
- `PoseAndFaceDetection`
- `PreviewImage`
- `QwenVLDetection`
- `RenderKps`
- `Sam2Segmentation`
- `SetNode`
- `Show any to JSON [Crystools]`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy ifElse`
- `easy seed`
- `huchenlei.LoadOpenposeJSON`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、Show any to JSON [Crystools]、CR Prompt Text、easy seed、huchenlei.LoadOpenposeJSON
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
