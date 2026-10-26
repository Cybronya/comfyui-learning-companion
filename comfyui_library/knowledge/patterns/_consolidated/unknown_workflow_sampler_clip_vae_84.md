---
name: unknown_workflow_sampler_clip_vae_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9695
common_nodes: [BasicScheduler, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXSequencer, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, MultiImageLoader, PromptRelayEncodeTimeline, SamplerCustom, SaveVideo, SimpleMath+, VAEDecodeTiled, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX23-长视频 整合多分镜模式_2052007179212861442.json, 视频生成/图生视频/ltx2.3-多图分段控制生视频_2059804412331253761.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX23-长视频 整合多分镜模式_2052007179212861442.json、视频生成/图生视频/ltx2.3-多图分段控制生视频_2059804412331253761.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXSequencer`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `MultiImageLoader`
- `PromptRelayEncodeTimeline`
- `SamplerCustom`
- `SaveVideo`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
