---
name: unknown_workflow_upscale_latent_upscale_lora_56
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8776
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2041020461265457154.json, 视频生成/图生视频/2052201685388406786.json, 视频生成/图生视频/2067639353119174658.json, 视频生成/图生视频/2031942296714878977.json, 视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_56

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2041020461265457154.json、视频生成/图生视频/2052201685388406786.json、视频生成/图生视频/2067639353119174658.json、视频生成/图生视频/2031942296714878977.json、视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ResizeImageMaskNode` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `ImageSharpen` —— 2/5 个有
- `LTX2SamplingPreviewOverride` —— 2/5 个有
- `LTXVEnhanceAVideoKJ` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `TextGenerateLTX2Prompt` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `FastFilmGrain` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImageScaleDownBy` —— 1/5 个有
- `LTX2_NAG` —— 1/5 个有
- `LTXVImgToVideoInplaceKJ` —— 1/5 个有
- `LTXVReferenceAudio` —— 1/5 个有
- `LTXVScheduler` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `PromptRelayEncode` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `VAEDecode` —— 1/5 个有
- `VHS_LoadAudioUpload` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
