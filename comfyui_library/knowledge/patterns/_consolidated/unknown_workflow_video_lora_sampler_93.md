---
name: unknown_workflow_video_lora_sampler_93
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.4655
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSize, ImageCompositeMasked, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2075466870496522242.json, 视频生成/图生视频/2080060140501426177.json, 视频生成/图生视频/2072124567392448513.json, 视频生成/图生视频/2079110010835132417.json, 视频生成/图生视频/2079943788537147394.json, 视频生成/图生视频/2065314921063206914.json, 视频生成/图生视频/2065718640225382402.json, 视频生成/图生视频/2072133229066412034.json, 视频生成/图生视频/高配2k 迁移无阉割纯血统 长续航版_2077767322877652993.json, 视频生成/图生视频/2064910481986506754.json, 视频生成/图生视频/2064739614107193346.json, 视频生成/图生视频/2065070055372713986.json, 视频生成/图生视频/2064746470225567745.json, 视频生成/图生视频/2064906920871419906.json, 视频生成/图生视频/2064727828876316673.json, 视频生成/文生视频/Scail2-动作迁移（单人+多人版）_2102405723132088321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_93

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2075466870496522242.json、视频生成/图生视频/2080060140501426177.json、视频生成/图生视频/2072124567392448513.json、视频生成/图生视频/2079110010835132417.json、视频生成/图生视频/2079943788537147394.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfyMathExpression`
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
- `GetNode` —— 15/16 个有
- `PrimitiveInt` —— 15/16 个有
- `SetNode` —— 15/16 个有
- `ImageConcatMulti` —— 14/16 个有
- `ImageResizeKJv2` —— 14/16 个有
- `PreviewImage` —— 14/16 个有
- `ResizeImageMaskNode` —— 14/16 个有
- `DiffusionModelLoaderKJ` —— 13/16 个有
- `JWInteger` —— 13/16 个有
- `Int` —— 4/16 个有
- `CR Text` —— 3/16 个有
- `RunningHub Deepcleaner` —— 3/16 个有
- `UNETLoader` —— 3/16 个有
- `ImageConcatenate_UTK` —— 2/16 个有
- `RHHiddenNodes` —— 2/16 个有
- `RH_Captioner` —— 2/16 个有
- `Text` —— 2/16 个有
- `Text Multiline` —— 2/16 个有
- `TextConcatenate_UTK` —— 2/16 个有
- `VHS_VideoInfoSource` —— 2/16 个有
- `ZhipuAPIConfig` —— 2/16 个有
- `easy imageCount` —— 2/16 个有
- `easy mathInt` —— 2/16 个有
- `easy showAnything` —— 2/16 个有
- `Label (rgthree)` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
