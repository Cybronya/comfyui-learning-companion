---
name: unknown_workflow_upscale_latent_upscale_sampler_11
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.743125
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2038192547784298497.json, 视频生成/图生视频/2053740318763307010.json, 视频生成/图生视频/LTX2.3图生视频（官方流）_2087157401068851201.json, 视频生成/图生视频/2069645486457442306.json, 视频生成/图生视频/2040052966710845441.json, 视频生成/图生视频/2076514549532024833.json, 视频生成/图生视频/2037940462845169665.json, 视频生成/图生视频/2039715377143353346.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2038192547784298497.json、视频生成/图生视频/2053740318763307010.json、视频生成/图生视频/LTX2.3图生视频（官方流）_2087157401068851201.json、视频生成/图生视频/2069645486457442306.json、视频生成/图生视频/2040052966710845441.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `PrimitiveBoolean` —— 6/8 个有
- `ResizeImageMaskNode` —— 6/8 个有
- `CreateVideo` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `CheckpointLoaderSimple` —— 4/8 个有
- `DualCLIPLoader` —— 4/8 个有
- `LTXAVTextEncoderLoader` —— 4/8 个有
- `LTXVAudioVAELoader` —— 4/8 个有
- `LoraLoader` —— 4/8 个有
- `UNETLoader` —— 4/8 个有
- `VAELoaderKJ` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `easy mathInt` —— 2/8 个有
- `LTXAddVideoICLoRAGuide` —— 1/8 个有
- `LTXICLoRALoaderModelOnly` —— 1/8 个有
- `Qwen3VL_Advanced` —— 1/8 个有
- `Qwen3VL_ExtraOptions` —— 1/8 个有
- `RebatchImages` —— 1/8 个有
- `SaveAudio` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `StringFunction|pysssss` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |
| LoRA 模型强度 | 1 | 0 - 1 | 4 | 42% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0 - 1，4 个样本，取值分散，一致性仅 42%
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
