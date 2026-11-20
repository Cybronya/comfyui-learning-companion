---
name: unknown_workflow_video_lora_sampler_395
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.426
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSize, GetNode, ImageCompositeMasked, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, PrimitiveInt, ResizeImageMaskNode, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/⓫ SCAIL2循环迁移-单图-人物替换-动作迁移-去字幕（官流）6.21_2066818951413325825.json, 视频生成/图生视频/双人跳舞动作迁移高质量Scail2双角色动作迁移_2066566906378805250.json, 视频生成/图生视频/图生视频-Scail2循环动作迁移_2067501661681180674.json, 视频生成/图生视频/宇宙最强动作迁移Scail2_2064708143938097154.json, 视频生成/图生视频/（循环高质量版）Scail2角色动作迁移V2_2064910481986506754.json, 视频生成/图生视频/（循环高质量版）Scail2角色动作迁移V5_2064739614107193346.json, 视频生成/图生视频/（高质量循环版）Scail2单人角色替换V5_2064746470225567745.json, 视频生成/图生视频/（高质量循环版）Scail2多人角色替换V5_2064727828876316673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_395

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/⓫ SCAIL2循环迁移-单图-人物替换-动作迁移-去字幕（官流）6.21_2066818951413325825.json、视频生成/图生视频/双人跳舞动作迁移高质量Scail2双角色动作迁移_2066566906378805250.json、视频生成/图生视频/图生视频-Scail2循环动作迁移_2067501661681180674.json、视频生成/图生视频/宇宙最强动作迁移Scail2_2064708143938097154.json、视频生成/图生视频/（循环高质量版）Scail2角色动作迁移V2_2064910481986506754.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyImage`
- `GIMMVFI_interpolate`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetNode`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `TensorLoopClose`
- `TensorLoopOpen`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 7/8 个有
- `JWInteger` —— 5/8 个有
- `RunningHub Deepcleaner` —— 3/8 个有
- `ImageStitch` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `Convert Masks to Images` —— 1/8 个有
- `FL_RIFE` —— 1/8 个有
- `FL_VideoTrim` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageFlip+` —— 1/8 个有
- `InvertMask` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `SAM3_TrackPreview` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
