---
name: text_to_image_lora_sampler_clip_301
type: Text To Image
frequency: 2
level: weak
coverage: 0.893
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Easy, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, PlaySound|pysssss, SaveImage, SaveVideo, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy imageChooser, kkVideoFirstLastFrames, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 VDN加SelfLift采样直出1080P 图生视频工具_2099586843141562370.json, 视频生成/图生视频/数字人15秒直出1080P图生视频处理生成工具_2101408406874714114.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_301

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3 VDN加SelfLift采样直出1080P 图生视频工具_2099586843141562370.json、视频生成/图生视频/数字人15秒直出1080P图生视频处理生成工具_2101408406874714114.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyMediaLoader`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `PlaySound|pysssss`
- `SaveImage`
- `SaveVideo`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy imageChooser`
- `kkVideoFirstLastFrames`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `GetLatentSizeAndCount` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `MiniMaxH3EasyMediaSplitter` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `SelfLiftAvatarH3Sampler` —— 1/2 个有
- `SelfLiftH3Sampler` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
