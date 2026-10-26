---
name: unknown_workflow_upscale_latent_upscale_lora_14
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.9145
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/图生视频LTX-2_I2V_2017262338130317313.json, 视频生成/图生视频/图生视频（解禁模型）：LTX2.3 Sulphur_2059994483848204290.json, 视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2012849703662129153.json, 视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2012865259995926529.json, 视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2013103822893228033.json, 视频生成/图生视频/最新 音画同步_ASMR LTX2图生视频_2019048798655352834.json, 视频生成/图生视频/短剧对白视频LTX2.0 图生视频LTX2.0 图生视频_2013531899406323713.json, 视频生成/图生视频/短剧对白视频LTX2.0 图生视频LTX2.0 图生视频_2021998636346904578.json, 视频生成/图生视频/音画同处LTX2.0！【又快又好】_2015590078243938306.json, 视频生成/图生视频/音画同步 LTX2.0 图生视频_2008562582247972866.json, 视频生成/图生视频/音画同步_ASMR LTX2图生视频_2014632850875752450.json, 视频生成/图生视频/音画同步_ASMR LTX2图生视频_2022200790881931265.json, 视频生成/图生视频/音画同步_ASMR+LTX2图生视频_2033431188710367233.json, 视频生成/图生视频/🥗开源视频新秀LTX2.0！【图生视频】工作流🥗_2008822192066269185.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_14

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/图生视频LTX-2_I2V_2017262338130317313.json、视频生成/图生视频/图生视频（解禁模型）：LTX2.3 Sulphur_2059994483848204290.json、视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2012849703662129153.json、视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2012865259995926529.json、视频生成/图生视频/基于ltx-2模型：火爆猫咪吃播ASMR解压视频生成音画同步图生视频asmr视频快速生成_2013103822893228033.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
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

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 12/14 个有
- `VHS_VideoCombine` —— 12/14 个有
- `CR Text` —— 7/14 个有
- `JWInteger` —— 7/14 个有
- `MathExpression|pysssss` —— 7/14 个有
- `PreviewImage` —— 7/14 个有
- `PrimitiveInt` —— 7/14 个有
- `ResizeImagesByLongerEdge` —— 5/14 个有
- `SimpleMath+` —— 3/14 个有
- `CM_IntToFloat` —— 2/14 个有
- `CreateVideo` —— 2/14 个有
- `ImpactExecutionOrderController` —— 2/14 个有
- `ImpactInt` —— 2/14 个有
- `SaveVideo` —— 2/14 个有
- `VAEDecodeTiled` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `ImpactSwitch` —— 1/14 个有
- `Int` —— 1/14 个有
- `KepStringLiteral` —— 1/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `Primitive integer [Crystools]` —— 1/14 个有
- `math_calculate` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
