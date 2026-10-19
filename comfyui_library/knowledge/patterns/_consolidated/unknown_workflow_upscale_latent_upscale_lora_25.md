---
name: unknown_workflow_upscale_latent_upscale_lora_25
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8168
common_nodes: [CFGGuider, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2041514210315735041.json, 视频生成/图生视频/2041734587340038146.json, 视频生成/图生视频/2030885319217782785.json, 视频生成/图生视频/2031213206097633281.json, 视频生成/图生视频/2082120324979716097.json, 视频生成/图生视频/2038207302813097986.json, 视频生成/图生视频/2073315948735586306.json, 视频生成/图生视频/2073319876273463297.json, 视频生成/图生视频/2073313777977745410.json, 视频生成/图生视频/2034460297049677825.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_25

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2041514210315735041.json、视频生成/图生视频/2041734587340038146.json、视频生成/图生视频/2030885319217782785.json、视频生成/图生视频/2031213206097633281.json、视频生成/图生视频/2082120324979716097.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
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
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `ResizeImageMaskNode` —— 9/10 个有
- `Int` —— 6/10 个有
- `LTXVAudioVAEEncode` —— 6/10 个有
- `LTXVEmptyLatentAudio` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/10 个有
- `LayerUtility: PurgeVRAM V2` —— 6/10 个有
- `LoadAudio` —— 6/10 个有
- `SetLatentNoiseMask` —— 6/10 个有
- `SolidMask` —— 6/10 个有
- `TrimAudioDuration` —— 6/10 个有
- `MelBandRoFormerModelLoader` —— 3/10 个有
- `MelBandRoFormerSampler` —— 3/10 个有
- `YC_textReplaceNode` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `AudioInfo` —— 2/10 个有
- `CM_FloatToInt` —— 2/10 个有
- `Float` —— 2/10 个有
- `LayerUtility: TextBox` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `SoundFlow_GetLength` —— 2/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `LTXVAddGuideMulti` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `PromptRelaySmartEncode` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `Text` —— 1/10 个有
- `YC_ShowText` —— 1/10 个有
- `YC_SingleTextNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
