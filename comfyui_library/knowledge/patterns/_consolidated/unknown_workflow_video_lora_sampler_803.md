---
name: unknown_workflow_video_lora_sampler_803
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.9
common_nodes: [Any Switch (rgthree), AudioSeparation, BlockifyMask, CLIPVisionLoader, DownloadAndLoadWav2VecModel, DrawMaskOnImage, DrawViTPose, GetImageRangeFromBatch, GetImageSizeAndCount, GrowMask, ImageConcatMulti, ImageResizeKJ, ImageResizeKJv2, Int, KEEP_ModelLoader, KEEP_ProcessImageSequence, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, OnnxDetectionModelLoader, PoseAndFaceDetection, RHHiddenNodes, ResizeMask, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy clearCacheAll, easy int]
problems: []
missing: []
members: [平台全量/AnimateV2+wan2.2单人OR多人极速角色背景替换、动作迁移极速生成复刻视频_1976130068323938305.json, 数字人/数字人/角色替换+动作迁移-表达式科技AIGC_1992618632486211585.json, 视频生成/图生视频/AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_803

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/AnimateV2+wan2.2单人OR多人极速角色背景替换、动作迁移极速生成复刻视频_1976130068323938305.json、数字人/数字人/角色替换+动作迁移-表达式科技AIGC_1992618632486211585.json、视频生成/图生视频/AnimateV2 wan2.2+SeC+CPM可多人手自一体换角色、衣服、背景、动作迁移复刻视频等_1960236846783606786.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
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
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `ResizeMask`
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
- `APersonMaskGenerator` —— 2/3 个有
- `ApplyFaceProcessor` —— 2/3 个有
- `FaceProcessorLoader` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `SeCModelLoader` —— 2/3 个有
- `SeCVideoSegmentation` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `LayerMask: LoadSegformerModel` —— 1/3 个有
- `LayerMask: SegformerClothesSetting` —— 1/3 个有
- `LayerMask: SegformerUltraV3` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
