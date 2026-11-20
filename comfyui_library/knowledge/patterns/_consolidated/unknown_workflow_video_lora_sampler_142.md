---
name: unknown_workflow_video_lora_sampler_142
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.4712
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DownloadAndLoadGIMMVFIModel, EmptyImage, GIMMVFI_interpolate, GetImageRangeFromBatch, GetImageSize, ImageCompositeMasked, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2075466870496522242.json, 视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2080060140501426177.json, 视频生成/图生视频/角色替换 高质量Scail2角色动作迁移V2 循环高清放大_2072124567392448513.json, 视频生成/图生视频/超牛Scail2动作迁移-无限循环任意时长版_2079110010835132417.json, 视频生成/图生视频/金扬定制款--高配2k 迁移无阉割纯血统 长续航版_2079943788537147394.json, 视频生成/图生视频/高帧率动作迁移，起号必备神器（直出）_2065314921063206914.json, 视频生成/图生视频/高帧率（角色替换）直出最佳效果_2065718640225382402.json, 视频生成/图生视频/高清长视频Scail2循环动作迁移数字人_2067440062316503041.json, 视频生成/图生视频/高质量Scail2角色动作迁移V2 循环高清放大_2072133229066412034.json, 视频生成/图生视频/高配2k 迁移无阉割纯血统 长续航版_2077767322877652993.json, 视频生成/图生视频/（高质量循环版）Scail2单人角色替换V1_2065070055372713986.json, 视频生成/图生视频/（高质量循环版）Scail2多人角色替换V1_2064906920871419906.json, 视频生成/图生视频/🦞🦞Scail2人物替换-低显存长视频生成_2065374469799108609.json, 视频生成/图生视频/🦞🦞Scail2动作迁移-低显存长视频生成_2065386686133129217.json, 视频生成/文生视频/Scail2-动作迁移（单人+多人版）_2102405723132088321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_142

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2075466870496522242.json、视频生成/图生视频/影视二创人物替换漫剧电商服装分镜真人_2080060140501426177.json、视频生成/图生视频/角色替换 高质量Scail2角色动作迁移V2 循环高清放大_2072124567392448513.json、视频生成/图生视频/超牛Scail2动作迁移-无限循环任意时长版_2079110010835132417.json、视频生成/图生视频/金扬定制款--高配2k 迁移无阉割纯血统 长续航版_2079943788537147394.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 15 个 workflow 都包含：
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
- `GetNode` —— 14/15 个有
- `PrimitiveInt` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `ImageConcatMulti` —— 13/15 个有
- `ImageResizeKJv2` —— 13/15 个有
- `PreviewImage` —— 13/15 个有
- `ResizeImageMaskNode` —— 13/15 个有
- `JWInteger` —— 11/15 个有
- `DiffusionModelLoaderKJ` —— 10/15 个有
- `CR Text` —— 6/15 个有
- `UNETLoader` —— 5/15 个有
- `Int` —— 4/15 个有
- `ImageConcatenate_UTK` —— 2/15 个有
- `RHHiddenNodes` —— 2/15 个有
- `RH_Captioner` —— 2/15 个有
- `SimpleMath+` —— 2/15 个有
- `Text` —— 2/15 个有
- `Text Multiline` —— 2/15 个有
- `TextConcatenate_UTK` —— 2/15 个有
- `VHS_VideoInfoSource` —— 2/15 个有
- `ZhipuAPIConfig` —— 2/15 个有
- `easy imageCount` —— 2/15 个有
- `easy int` —— 2/15 个有
- `easy mathInt` —— 2/15 个有
- `easy showAnything` —— 2/15 个有
- `Bjornulf_ShowInt` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/15 个有
- `MathExpression|pysssss` —— 1/15 个有
- `PathchSageAttentionKJ` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
