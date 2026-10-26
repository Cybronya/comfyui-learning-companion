---
name: unknown_workflow_video_lora_sampler_224
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.4367
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, GetImageRangeFromBatch, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan21_SCAIL2_5段扩展长视频_2065365595184521217.json, 视频生成/图生视频/Wan21_SCAIL2_FOR 循环长视频生成工作流_2065680641039093761.json, 视频生成/图生视频/Wan21_SCAIL2_expression_2064969130989670401.json, 视频生成/图生视频/Wan21_SCAIL2_kimoto_no_replace_2066352425379909633.json, 视频生成/图生视频/Wan21_SCAIL2_no_replace_2064637391054397441.json, 视频生成/图生视频/Wan21_SCAIL2_no_replace_two_person_2064981162845622273.json, 视频生成/图生视频/Wan21_SCAIL2_replace_2064994418565931010.json, 视频生成/图生视频/Wan21_SCAIL2_replace_two_person_2064998971084468225.json, 视频生成/图生视频/【尺素】Scail2人物替换-低配15秒畅跑简约版_2066063514803986434.json, 视频生成/图生视频/完美动作迁移-SCAIL2_多参考图_2071761838928384001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_224

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Wan21_SCAIL2_5段扩展长视频_2065365595184521217.json、视频生成/图生视频/Wan21_SCAIL2_FOR 循环长视频生成工作流_2065680641039093761.json、视频生成/图生视频/Wan21_SCAIL2_expression_2064969130989670401.json、视频生成/图生视频/Wan21_SCAIL2_kimoto_no_replace_2066352425379909633.json、视频生成/图生视频/Wan21_SCAIL2_no_replace_2064637391054397441.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 9/10 个有
- `ColorTransfer` —— 9/10 个有
- `GetNode` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `GetImageSize` —— 6/10 个有
- `ImageFromBatch` —— 6/10 个有
- `PrimitiveBoolean` —— 5/10 个有
- `MathExpression|pysssss` —— 3/10 个有
- `VHS_VideoInfoLoaded` —— 3/10 个有
- `WanChunkFeedForward` —— 3/10 个有
- `easy forLoopEnd` —— 2/10 个有
- `easy forLoopStart` —— 2/10 个有
- `easy imageRemBg` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageBatchMulti` —— 1/10 个有
- `ImpactConditionalBranch` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `easy batchAnything` —— 1/10 个有
- `easy int` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
