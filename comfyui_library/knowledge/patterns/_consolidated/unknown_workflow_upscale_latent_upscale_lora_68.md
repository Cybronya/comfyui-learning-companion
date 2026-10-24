---
name: unknown_workflow_upscale_latent_upscale_lora_68
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.810667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/Sulphur-2 ID-lora语音参考视频_2056584675753287682.json, 视频生成/图生视频/sulphur_i2v_distilled_2052201685388406786.json, 视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_68

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Sulphur-2 ID-lora语音参考视频_2056584675753287682.json、视频生成/图生视频/sulphur_i2v_distilled_2052201685388406786.json、视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
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
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `ImageScaleDownBy` —— 2/3 个有
- `LTXVScheduler` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `VAEDecodeTiled` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `Context (rgthree)` —— 1/3 个有
- `Context Switch (rgthree)` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LTXVImgToVideoConditionOnly` —— 1/3 个有
- `LTXVReferenceAudio` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PromptRelayEncode` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TextGenerateLTX2Prompt` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `easy ckptNames` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
