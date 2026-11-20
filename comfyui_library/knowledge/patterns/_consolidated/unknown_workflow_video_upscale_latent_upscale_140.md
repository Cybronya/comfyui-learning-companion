---
name: unknown_workflow_video_upscale_latent_upscale_140
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.488
common_nodes: [CFGGuider, CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, SimpleMath+, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3  自定义多帧高清工作流-KJ-PR-V1_2049466416235024385.json, 视频生成/图生视频/LTX2.3_多图参考_极致高清_工作流_2068715608803463169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_140

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3  自定义多帧高清工作流-KJ-PR-V1_2049466416235024385.json、视频生成/图生视频/LTX2.3_多图参考_极致高清_工作流_2068715608803463169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `LTXAddVideoICLoRAGuide` —— 1/2 个有
- `LTXICLoRALoaderModelOnly` —— 1/2 个有
- `LTXSequencer` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LiconMSR` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MultiImageLoader` —— 1/2 个有
- `PromptRelayEncodeTimeline` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | - | 2 | 100% |
| 高度 | 27 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 27，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
