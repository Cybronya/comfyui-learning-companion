---
name: unknown_workflow_video_upscale_lora_37
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.532
common_nodes: [AILab_Preview, BlockifyMask, CLIPVisionLoader, Display Int (rgthree), DownloadAndLoadGIMMVFIModel, DrawMaskOnImage, GIMMVFI_interpolate, GetImageSizeAndCount, GetNode, GrowMask, GrowMaskWithBlur, INTConstant, ImageBatchRepeatInterleaving, ImageBlend, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, ImageScaleBy, ImageScaleToMaxDimension, ImageToMask, LoadImage, LoadSAM3Model, LoadWanVideoT5TextEncoder, MaskToImage, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, PreviewAny, SAM3Segmentation, SeCModelLoader, SeCVideoSegmentation, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SimpleCalculatorKJ, SolidMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoImageResizeToClosest, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy boolean, easy compare, easy ifElse, easy int, easy lengthAnything, easy mathInt]
problems: []
missing: []
members: [平台全量/视频编辑_WanAnimate_长视频_指定角色替换或动作迁移_2007797762489847810.json, 平台全量/视频编辑_WanVACE_Stand-In_指定角色替换或动作迁移_2007853415845601281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频编辑_WanAnimate_长视频_指定角色替换或动作迁移_2007797762489847810.json、平台全量/视频编辑_WanVACE_Stand-In_指定角色替换或动作迁移_2007853415845601281.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_Preview`
- `BlockifyMask`
- `CLIPVisionLoader`
- `Display Int (rgthree)`
- `DownloadAndLoadGIMMVFIModel`
- `DrawMaskOnImage`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageBatchRepeatInterleaving`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToMaxDimension`
- `ImageToMask`
- `LoadImage`
- `LoadSAM3Model`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `PreviewAny`
- `SAM3Segmentation`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageResizeToClosest`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy boolean`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `ApplyFaceProcessor` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `FaceProcessorLoader` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `WanVideoAddStandInLatent` —— 1/2 个有
- `WanVideoAnimateEmbeds` —— 1/2 个有
- `WanVideoClipVisionEncode` —— 1/2 个有
- `WanVideoContextOptions` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
