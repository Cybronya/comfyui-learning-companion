---
name: unknown_workflow_sampler_clip_checkpoint_38
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.836
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVScheduler, LTXVSeparateAVLatent, MathExpression|pysssss, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/直播生成祝福视频自动配音 Ltx2 文生视频_2013407856636207105.json, 视频生成/文生视频/🦖LTX2.0文生视频_2008714720701849601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_38

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/直播生成祝福视频自动配音 Ltx2 文生视频_2013407856636207105.json、视频生成/文生视频/🦖LTX2.0文生视频_2008714720701849601.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

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
