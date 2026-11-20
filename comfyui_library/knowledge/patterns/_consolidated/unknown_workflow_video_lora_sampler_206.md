---
name: unknown_workflow_video_lora_sampler_206
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.431
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Scail2视频角色替换_2065006346432503810.json, 视频生成/图生视频/Wan-SCAIL2 动作迁移_人物替换_2064423977212272642.json, 视频生成/图生视频/Wan21_SCAIL2_5段扩展长视频_2065365595184521217.json, 视频生成/图生视频/Wan21_SCAIL2_FOR 循环长视频生成工作流_2065680641039093761.json, 视频生成/图生视频/Wan21_SCAIL2_expression_2064969130989670401.json, 视频生成/图生视频/Wan21_SCAIL2_kimoto_no_replace_2066352425379909633.json, 视频生成/图生视频/Wan21_SCAIL2_no_replace_2064637391054397441.json, 视频生成/图生视频/Wan21_SCAIL2_no_replace_two_person_2064981162845622273.json, 视频生成/图生视频/Wan21_SCAIL2_replace_2064994418565931010.json, 视频生成/图生视频/Wan21_SCAIL2_replace_two_person_2064998971084468225.json, 视频生成/图生视频/全新动作模仿 SCAIL2！单人or双人角色替换_2065258951524048898.json, 视频生成/图生视频/双人多人全新动作迁移复制对打_2065406697937657858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_206

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Scail2视频角色替换_2065006346432503810.json、视频生成/图生视频/Wan-SCAIL2 动作迁移_人物替换_2064423977212272642.json、视频生成/图生视频/Wan21_SCAIL2_5段扩展长视频_2065365595184521217.json、视频生成/图生视频/Wan21_SCAIL2_FOR 循环长视频生成工作流_2065680641039093761.json、视频生成/图生视频/Wan21_SCAIL2_expression_2064969130989670401.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `ImageConcatMulti` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `ImageFromBatch` —— 9/12 个有
- `GetImageSize` —— 6/12 个有
- `WanChunkFeedForward` —— 6/12 个有
- `PrimitiveBoolean` —— 4/12 个有
- `JjkText` —— 3/12 个有
- `PreviewAny` —— 3/12 个有
- `PrimitiveInt` —— 3/12 个有
- `SimpleMath+` —— 3/12 个有
- `ttN int` —— 3/12 个有
- `MathExpression|pysssss` —— 2/12 个有
- `VHS_VideoInfoLoaded` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `easy imageRemBg` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `INTConstant` —— 1/12 个有
- `Int` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `TT_img_enc` —— 1/12 个有
- `easy forLoopEnd` —— 1/12 个有
- `easy forLoopStart` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
