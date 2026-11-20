---
name: unknown_workflow_upscale_latent_upscale_lora_29
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.810727
common_nodes: [CFGGuider, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3图片转动态_2038192547784298497.json, 视频生成/图生视频/LTX2.3图生视频_2053740318763307010.json, 视频生成/图生视频/LTX2.3图生视频（官方流）_2087157401068851201.json, 视频生成/图生视频/LTX2.3图转视频（官方流）_2069645486457442306.json, 视频生成/图生视频/LTX2.3数字人V2—支持双人，自动计算帧数_2073315948735586306.json, 视频生成/图生视频/LTX2.3数字人V3 Prompt Relay提示词分段控制_2073319876273463297.json, 视频生成/图生视频/LTX2.3数字人—支持双人_2073313777977745410.json, 视频生成/图生视频/LTX2.3数字人精准对口型，类型：说话、唱歌_2062387729098428417.json, 视频生成/图生视频/LTX2.3数字人说话唱歌 精准对口型_2087214680174583809.json, 视频生成/图生视频/LTX2.3数字人说话唱歌高精准对口型_2101198595667095554.json, 视频生成/文生视频/LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_29

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX2.3图片转动态_2038192547784298497.json、视频生成/图生视频/LTX2.3图生视频_2053740318763307010.json、视频生成/图生视频/LTX2.3图生视频（官方流）_2087157401068851201.json、视频生成/图生视频/LTX2.3图转视频（官方流）_2069645486457442306.json、视频生成/图生视频/LTX2.3数字人V2—支持双人，自动计算帧数_2073315948735586306.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
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
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 10/11 个有
- `LTXVEmptyLatentAudio` —— 8/11 个有
- `LTXVAudioVAEEncode` —— 7/11 个有
- `LoadAudio` —— 7/11 个有
- `SaveVideo` —— 7/11 个有
- `SetLatentNoiseMask` —— 7/11 个有
- `SolidMask` —— 7/11 个有
- `TrimAudioDuration` —— 7/11 个有
- `Any Switch (rgthree)` —— 4/11 个有
- `CM_IntToFloat` —— 4/11 个有
- `RHHiddenNodes` —— 4/11 个有
- `SimpleMath+` —— 4/11 个有
- `VHS_VideoCombine` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `AudioInfo` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `easy mathInt` —— 2/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `LoraLoader` —— 1/11 个有
- `MelBandRoFormerModelLoader` —— 1/11 个有
- `MelBandRoFormerSampler` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `PromptRelaySmartEncode` —— 1/11 个有
- `Qwen3VL_Advanced` —— 1/11 个有
- `Qwen3VL_ExtraOptions` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有
- `StringFunction|pysssss` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
