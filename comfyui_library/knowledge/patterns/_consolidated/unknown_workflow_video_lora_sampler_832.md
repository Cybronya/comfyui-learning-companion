---
name: unknown_workflow_video_lora_sampler_832
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.517
common_nodes: [CLIPVisionLoader, CR Text, DWPreprocessor, DownloadAndLoadGIMMVFIModel, EmptyImage, FaceMaskFromPoseKeypoints, Fast Groups Bypasser (rgthree), GIMMVFI_interpolate, GetNode, INTConstant, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, PlaySound|pysssss, PreviewImage, PrimitiveFloat, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [平台全量/视频换人_1975681832396173313.json, 平台全量/视频换人sec遮罩_1988221456612024321.json, 视频生成/图生视频/animate动作参考_1993657124511219713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_832

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频换人_1975681832396173313.json、平台全量/视频换人sec遮罩_1988221456612024321.json、视频生成/图生视频/animate动作参考_1993657124511219713.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `DWPreprocessor`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyImage`
- `FaceMaskFromPoseKeypoints`
- `Fast Groups Bypasser (rgthree)`
- `GIMMVFI_interpolate`
- `GetNode`
- `INTConstant`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `GrowMask` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImageRemoveBackground+` —— 1/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `RemBGSession+` —— 1/3 个有
- `SeCModelLoader` —— 1/3 个有
- `SeCVideoSegmentation` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
