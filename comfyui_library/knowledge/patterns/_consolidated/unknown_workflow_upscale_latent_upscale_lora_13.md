---
name: unknown_workflow_upscale_latent_upscale_lora_13
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.8245
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3图片转动态_2038192547784298497.json, 视频生成/图生视频/LTX2.3图生视频_2053740318763307010.json, 视频生成/图生视频/LTX2.3图生视频（官方流）_2087157401068851201.json, 视频生成/图生视频/LTX2.3图转视频（官方流）_2069645486457442306.json, 视频生成/图生视频/LTX2.3真人短剧_2033403811573800961.json, 视频生成/图生视频/LTX2.3自动首中尾三帧视频_2031361873404239873.json, 视频生成/图生视频/LTX2.3自动首中尾三帧视频（自用）_2036273219824521217.json, 视频生成/图生视频/LTX2.3自动首尾帧流_2073405314405322753.json, 视频生成/图生视频/LTX_2_3_I2V_Basic_2081391586033889281.json, 视频生成/图生视频/ltx2.3图生视频-官方版_2057789192654123010.json, 视频生成/图生视频/🐱video_ITX2.3_I2V图像首尾帧生视频_2031942296714878977.json, 视频生成/文生视频/LTX-文生视频-官方标准版-必收藏_2069062124302852097.json, 视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json, 视频生成/文生视频/LTX2.3文生视频_2071411094870126593.json, 视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json, 视频生成/文生视频/LTX2.3文生视频_2072160114223697921.json, 视频生成/文生视频/LTX2.3文生视频_2072165023333576705.json, 视频生成/文生视频/LTX2.3文生视频_2083869701729509377.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_13

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/LTX2.3图片转动态_2038192547784298497.json、视频生成/图生视频/LTX2.3图生视频_2053740318763307010.json、视频生成/图生视频/LTX2.3图生视频（官方流）_2087157401068851201.json、视频生成/图生视频/LTX2.3图转视频（官方流）_2069645486457442306.json、视频生成/图生视频/LTX2.3真人短剧_2033403811573800961.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 17/18 个有
- `ResizeImageMaskNode` —— 17/18 个有
- `PrimitiveBoolean` —— 15/18 个有
- `LoadImage` —— 11/18 个有
- `LoraLoader` —— 11/18 个有
- `PreviewAny` —— 10/18 个有
- `TextGenerateLTX2Prompt` —— 10/18 个有
- `ComfySwitchNode` —— 9/18 个有
- `EmptyImage` —— 8/18 个有
- `RH_LLMAPI_Pro_Node` —— 5/18 个有
- `LTXVImgToVideoInplaceKJ` —— 4/18 个有
- `easy showAnything` —— 4/18 个有
- `easy mathInt` —— 3/18 个有
- `FloatConstant` —— 2/18 个有
- `GetNode` —— 2/18 个有
- `Resize` —— 2/18 个有
- `SetNode` —— 2/18 个有
- `ImageSizeInfo` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `PrimitiveFloat` —— 1/18 个有
- `Qwen3VL_Advanced` —— 1/18 个有
- `Qwen3VL_ExtraOptions` —— 1/18 个有
- `SaveImage` —— 1/18 个有
- `ShowText|pysssss` —— 1/18 个有
- `SimpleMath+` —— 1/18 个有
- `StringFunction|pysssss` —— 1/18 个有
- `Text` —— 1/18 个有
- `Text Concatenate` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 18 | 100% |
| 高度 | 25 | 25 - 25 | 18 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，18 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，18 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
