---
name: unknown_workflow_upscale_latent_upscale_lora_31
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8691
common_nodes: [CFGGuider, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2031346405217935361.json, 视频生成/图生视频/2031368415541202945.json, 视频生成/图生视频/2037157386359672834.json, 视频生成/图生视频/2037707002851364865.json, 视频生成/图生视频/2073315948735586306.json, 视频生成/图生视频/2073319876273463297.json, 视频生成/图生视频/2073313777977745410.json, 视频生成/图生视频/2037742707522670593.json, 视频生成/图生视频/2034460297049677825.json, 视频生成/图生视频/2033785787984125953.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_31

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2031346405217935361.json、视频生成/图生视频/2031368415541202945.json、视频生成/图生视频/2037157386359672834.json、视频生成/图生视频/2037707002851364865.json、视频生成/图生视频/2073315948735586306.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
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
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 9/10 个有
- `CheckpointLoaderSimple` —— 7/10 个有
- `LTXAVTextEncoderLoader` —— 7/10 个有
- `LTXVAudioVAELoader` —— 7/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `Text` —— 6/10 个有
- `LTXVAudioVAEEncode` —— 5/10 个有
- `LTXVEmptyLatentAudio` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `PrimitiveStringMultiline` —— 5/10 个有
- `SetLatentNoiseMask` —— 5/10 个有
- `SimpleMath+` —— 5/10 个有
- `SolidMask` —— 5/10 个有
- `PrimitiveBoolean` —— 4/10 个有
- `ResizeImageMaskNode` —— 4/10 个有
- `ShowText|pysssss` —— 4/10 个有
- `TrimAudioDuration` —— 4/10 个有
- `DualCLIPLoader` —— 3/10 个有
- `LTXVAddGuideMulti` —— 3/10 个有
- `UNETLoader` —— 3/10 个有
- `VAELoaderKJ` —— 3/10 个有
- `AudioInfo` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `ImageSizeInfo` —— 2/10 个有
- `LTXVImgToVideoInplaceKJ` —— 2/10 个有
- `PlaySound|pysssss` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `Float` —— 1/10 个有
- `MelBandRoFormerModelLoader` —— 1/10 个有
- `MelBandRoFormerSampler` —— 1/10 个有
- `PromptRelaySmartEncode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
