---
name: unknown_workflow_video_lora_sampler_816
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8975
common_nodes: [Any Switch (rgthree), AudioSeparation, BlockifyMask, CLIPVisionLoader, DownloadAndLoadWav2VecModel, DrawMaskOnImage, DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, GrowMask, ImageConcatMulti, ImageFromBatch, ImageResizeKJ, ImageResizeKJv2, Int, KEEP_ModelLoader, KEEP_ProcessImageSequence, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, OnnxDetectionModelLoader, PointsEditor, PoseAndFaceDetection, PrimitiveInt, RHHiddenNodes, ResizeMask, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, easy int]
problems: []
missing: []
members: [数字人/数字人/角色替换+动作迁移-表达式科技AIGC_1992618632486211585.json, 视频生成/图生视频/AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_816

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/角色替换+动作迁移-表达式科技AIGC_1992618632486211585.json、视频生成/图生视频/AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AudioSeparation`
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GrowMask`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `Int`
- `KEEP_ModelLoader`
- `KEEP_ProcessImageSequence`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `OnnxDetectionModelLoader`
- `PointsEditor`
- `PoseAndFaceDetection`
- `PrimitiveInt`
- `RHHiddenNodes`
- `ResizeMask`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `APersonMaskGenerator` —— 1/2 个有
- `ApplyFaceProcessor` —— 1/2 个有
- `FaceProcessorLoader` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `LayerMask: LoadSegformerModel` —— 1/2 个有
- `LayerMask: SegformerClothesSetting` —— 1/2 个有
- `LayerMask: SegformerUltraV3` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
