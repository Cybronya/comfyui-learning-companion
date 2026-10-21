---
name: unknown_workflow_upscale_latent_upscale_lora_74
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6955
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RH_LLMAPI_NODE, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, Text Multiline, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2035357780827185153.json, 视频生成/图生视频/2042630779330633730.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_74

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2035357780827185153.json、视频生成/图生视频/2042630779330633730.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text Multiline`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `MaxNode` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `Qwen3VL_Chat` —— 1/2 个有
- `RIFEInterpolation` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `Text` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 169 | - | 2 | 57% |
| 高度 | 24.5 | - | 2 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 169，样本不足，未给区间，2 个样本
- 高度 中位数 24.5，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
