---
name: unknown_workflow_lora_sampler_clip_248
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.937
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, Image Batch, LTX2SamplingPreviewOverride, LTXVAddGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoader, ManualSigmas, Power Lora Loader (rgthree), PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SamplerEulerAncestral, SaveVideo, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/图生图/ltx2.3首尾帧人物高一致流_2045519229465661441.json, 视频生成/图生视频/新LTX2.3首尾帧视频教学版_2045873770665086977.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_248

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ltx2.3首尾帧人物高一致流_2045519229465661441.json、视频生成/图生视频/新LTX2.3首尾帧视频教学版_2045873770665086977.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `Image Batch`
- `LTX2SamplingPreviewOverride`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoader`
- `ManualSigmas`
- `Power Lora Loader (rgthree)`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveVideo`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
