---
name: unknown_workflow_upscale_latent_upscale_lora_70
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8675
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3参考图+参考音色_2041020461265457154.json, 视频生成/图生视频/sulphur_i2v_distilled_2052201685388406786.json, 视频生成/文生视频/AI真人短剧工作流+文生_图生视频_2035632455331356674.json, 视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_70

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/ltx2.3参考图+参考音色_2041020461265457154.json、视频生成/图生视频/sulphur_i2v_distilled_2052201685388406786.json、视频生成/文生视频/AI真人短剧工作流+文生_图生视频_2035632455331356674.json、视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `ImageSharpen` —— 2/4 个有
- `LTX2SamplingPreviewOverride` —— 2/4 个有
- `LTXVEnhanceAVideoKJ` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `FastFilmGrain` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `ImageScaleDownBy` —— 1/4 个有
- `LTX2_NAG` —— 1/4 个有
- `LTXVReferenceAudio` —— 1/4 个有
- `LTXVScheduler` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PromptRelayEncode` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `VAEDecode` —— 1/4 个有
- `VHS_LoadAudioUpload` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
