---
name: unknown_workflow_video_upscale_latent_upscale_29
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.908
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2017262338130317313.json, 视频生成/图生视频/2009222188091576321.json, 视频生成/图生视频/2059994483848204290.json, 视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2012849703662129153.json, 视频生成/图生视频/2012865259995926529.json, 视频生成/图生视频/2013103822893228033.json, 视频生成/图生视频/2019048798655352834.json, 视频生成/图生视频/2008562582247972866.json, 视频生成/图生视频/2014632850875752450.json, 视频生成/图生视频/2022200790881931265.json, 视频生成/图生视频/2033431188710367233.json, 视频生成/图生视频/2012772374625652737.json, 视频生成/图生视频/2008714518439927810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_29

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2017262338130317313.json、视频生成/图生视频/2009222188091576321.json、视频生成/图生视频/2059994483848204290.json、视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2012849703662129153.json、视频生成/图生视频/2012865259995926529.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 12/13 个有
- `VAEDecode` —— 10/13 个有
- `CR Text` —— 9/13 个有
- `JWInteger` —— 9/13 个有
- `MathExpression|pysssss` —— 9/13 个有
- `PreviewImage` —— 7/13 个有
- `PrimitiveInt` —— 5/13 个有
- `ResizeImagesByLongerEdge` —— 3/13 个有
- `VAEDecodeTiled` —— 3/13 个有
- `CM_IntToFloat` —— 2/13 个有
- `GetNode` —— 2/13 个有
- `ImpactExecutionOrderController` —— 2/13 个有
- `Int` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `SimpleMath+` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `KepStringLiteral` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `MemoryCleaner` —— 1/13 个有
- `Primitive integer [Crystools]` —— 1/13 个有
- `PrimitiveFloat` —— 1/13 个有
- `ResizeLongestToNode` —— 1/13 个有
- `math_calculate` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
