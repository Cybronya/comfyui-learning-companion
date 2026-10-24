---
name: unknown_workflow_video_lora_sampler_675
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.649333
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSize, ImageCompositeMasked, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2075466870496522242.json, 视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2080060140501426177.json, 视频生成/文生视频/Scail2-动作迁移（单人+多人版）_2102405723132088321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_675

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2075466870496522242.json、视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2080060140501426177.json、视频生成/文生视频/Scail2-动作迁移（单人+多人版）_2102405723132088321.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Int`
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
- `GetNode` —— 2/3 个有
- `ImageConcatenate_UTK` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `Text` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `TextConcatenate_UTK` —— 2/3 个有
- `VHS_VideoInfoSource` —— 2/3 个有
- `easy imageCount` —— 2/3 个有
- `easy mathInt` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
