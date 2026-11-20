---
name: unknown_workflow_video_lora_sampler_337
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.512111
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSize, ImageCompositeMasked, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/SCAIL2替换视频中的单个人物漫剧电商服装分镜真人_2071782259115511810.json, 视频生成/图生视频/SCAIL2替换视频人物漫剧电商服装分镜真人_2071786306396573698.json, 视频生成/图生视频/Scail  2 双人互动替换_2066357363409510402.json, 视频生成/图生视频/Scail2-人物360度动作迁移_2067529633486168065.json, 视频生成/图生视频/Scail2-动作迁移（单人+多人版）_2065351817646661633.json, 视频生成/图生视频/Scail2全自动单人角色替换工作流_2065037170393575426.json, 视频生成/图生视频/scail 2 单人电商带货 人物产品替换_2067503598057123841.json, 视频生成/图生视频/scail 2 单人电商带货 人物产品替换自动版_2067564547317264386.json, 视频生成/图生视频/scail 2双人互动异步动作迁移_2067087693439397890.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_337

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/SCAIL2替换视频中的单个人物漫剧电商服装分镜真人_2071782259115511810.json、视频生成/图生视频/SCAIL2替换视频人物漫剧电商服装分镜真人_2071786306396573698.json、视频生成/图生视频/Scail  2 双人互动替换_2066357363409510402.json、视频生成/图生视频/Scail2-人物360度动作迁移_2067529633486168065.json、视频生成/图生视频/Scail2-动作迁移（单人+多人版）_2065351817646661633.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PreviewImage`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `TensorLoopClose`
- `TensorLoopOpen`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `PrimitiveInt` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `RH_Captioner` —— 6/9 个有
- `VHS_VideoInfoSource` —— 6/9 个有
- `easy imageCount` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `JWInteger` —— 5/9 个有
- `Text` —— 5/9 个有
- `ImageConcatMulti` —— 4/9 个有
- `Int` —— 4/9 个有
- `RH_RhartImageG2OfficialImageToImage` —— 4/9 个有
- `ResizeImageMaskNode` —— 4/9 个有
- `easy indexAnything` —— 4/9 个有
- `DrawMaskOnImage` —— 3/9 个有
- `InvertMask` —— 3/9 个有
- `TextConcatenate_UTK` —— 3/9 个有
- `1hew_MaskMathOps` —— 2/9 个有
- `ColorPickerMW` —— 2/9 个有
- `FillMaskWithColor` —— 2/9 个有
- `Switch` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `easy mathInt` —— 2/9 个有
- `Bjornulf_ShowInt` —— 1/9 个有
- `ComfySwitchNode` —— 1/9 个有
- `ImageCrop` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `PointsEditor` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `ReActorFaceSwap` —— 1/9 个有
- `RemoveWatermarks_LoadModel` —— 1/9 个有
- `RemoveWatermarks_Run` —— 1/9 个有
- `SeCModelLoader` —— 1/9 个有
- `SeCVideoSegmentation` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `string_util_StrConcat` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
