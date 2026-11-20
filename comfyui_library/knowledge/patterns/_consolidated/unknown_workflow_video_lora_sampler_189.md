---
name: unknown_workflow_video_lora_sampler_189
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.510545
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSize, ImageCompositeMasked, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/SCAIL2替换视频中的单个人物漫剧电商服装分镜真人_2071782259115511810.json, 视频生成/图生视频/SCAIL2替换视频人物漫剧电商服装分镜真人_2071786306396573698.json, 视频生成/图生视频/Scail  2 双人互动替换_2066357363409510402.json, 视频生成/图生视频/Scail2-动作迁移（单人+多人版）_2065351817646661633.json, 视频生成/图生视频/Scail2全自动单人角色替换工作流_2065037170393575426.json, 视频生成/图生视频/scail 2 单人电商带货 人物产品替换_2067503598057123841.json, 视频生成/图生视频/scail 2 单人电商带货 人物产品替换自动版_2067564547317264386.json, 视频生成/图生视频/scail 2双人互动异步动作迁移_2067087693439397890.json, 视频生成/图生视频/scail2带货视频 电商带货，人货互动_2067282833252634625.json, 视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2075466870496522242.json, 视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2080060140501426177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_189

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/SCAIL2替换视频中的单个人物漫剧电商服装分镜真人_2071782259115511810.json、视频生成/图生视频/SCAIL2替换视频人物漫剧电商服装分镜真人_2071786306396573698.json、视频生成/图生视频/Scail  2 双人互动替换_2066357363409510402.json、视频生成/图生视频/Scail2-动作迁移（单人+多人版）_2065351817646661633.json、视频生成/图生视频/Scail2全自动单人角色替换工作流_2065037170393575426.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 11 个 workflow 都包含：
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
- `GetNode` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `ImageResizeKJv2` —— 9/11 个有
- `RH_Captioner` —— 9/11 个有
- `VHS_VideoInfoSource` —— 9/11 个有
- `easy imageCount` —— 9/11 个有
- `easy showAnything` —— 9/11 个有
- `Text` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/11 个有
- `JWInteger` —— 6/11 个有
- `TextConcatenate_UTK` —— 6/11 个有
- `Int` —— 5/11 个有
- `easy indexAnything` —— 5/11 个有
- `DrawMaskOnImage` —— 4/11 个有
- `InvertMask` —— 4/11 个有
- `RH_RhartImageG2OfficialImageToImage` —— 4/11 个有
- `Text Multiline` —— 4/11 个有
- `easy mathInt` —— 4/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `ResizeImageMaskNode` —— 3/11 个有
- `1hew_MaskMathOps` —— 2/11 个有
- `ColorPickerMW` —— 2/11 个有
- `FillMaskWithColor` —— 2/11 个有
- `ImageConcatenate_UTK` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `Switch` —— 2/11 个有
- `Bjornulf_ShowInt` —— 1/11 个有
- `ComfySwitchNode` —— 1/11 个有
- `ImageCrop` —— 1/11 个有
- `ImageFromBatch` —— 1/11 个有
- `PointsEditor` —— 1/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `ReActorFaceSwap` —— 1/11 个有
- `RemoveWatermarks_LoadModel` —— 1/11 个有
- `RemoveWatermarks_Run` —— 1/11 个有
- `SeCModelLoader` —— 1/11 个有
- `SeCVideoSegmentation` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `string_util_StrConcat` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
