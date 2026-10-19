---
name: unknown_workflow_video_sampler_clip_215
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.644
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, EmptyLTXVLatentVideo, GetImageSize, LTXVAddGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SamplerEulerAncestral, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.5首尾帧图生视频_2087801270798217218.json, 视频生成/文生视频/LTX2.5 首尾帧图生视频+全节点注释_2087729834381373441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_215

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX2.5首尾帧图生视频_2087801270798217218.json、视频生成/文生视频/LTX2.5 首尾帧图生视频+全节点注释_2087729834381373441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LTXVAddGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Dapao_LlamaCaption` —— 1/2 个有
- `Dapao_LlamaCaptionOptions` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `ReversalCaptionOptions` —— 1/2 个有
- `ReversalLlamaCaption` —— 1/2 个有
- `TrimVideoLatent` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
