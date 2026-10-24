---
name: text_to_image_lora_sampler_clip_174
type: Text To Image
frequency: 10
level: strong
coverage: 0.8691
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/h3 r2v runninghub tts v2｜图生视频音频驱动生成_2091306513502654466.json, 视频生成/图生视频/h3参考生视频方案，图生视频多参考精准还原_2110861891965902849.json, 视频生成/图生视频/i2v加速版直出｜Minimax H3文生图生视频场景特效_2092740361742536706.json, 视频生成/图生视频/lightx2v正式版参考模式｜minimax_h3视频生视频图生视频工作流_2088211325951504385.json, 视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json, 视频生成/图生视频/minimax_h3_turbo_v4_step600_ema图生视频加速模型_2105146341893693442.json, 视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json, 视频生成/图生视频/参考生视频玩法升级｜MiniMax H3 视频生视频双通道_2096253067581812737.json, 视频生成/图生视频/多图参考直出｜MiniMax H3图生视频一致性生成_2090271687425220609.json, 视频生成/文生视频/4步8步加速稳定MAX｜MiniMaxH3多合一自用版_2092748173281423361.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_174

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/h3 r2v runninghub tts v2｜图生视频音频驱动生成_2091306513502654466.json、视频生成/图生视频/h3参考生视频方案，图生视频多参考精准还原_2110861891965902849.json、视频生成/图生视频/i2v加速版直出｜Minimax H3文生图生视频场景特效_2092740361742536706.json、视频生成/图生视频/lightx2v正式版参考模式｜minimax_h3视频生视频图生视频工作流_2088211325951504385.json、视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `LoadAudio` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `PrimitiveBoolean` —— 5/10 个有
- `ComfySwitchNode` —— 4/10 个有
- `PrimitiveInt` —— 4/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `Fast Bypasser (rgthree)` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `LazySwitchKJ` —— 1/10 个有
- `MiniMaxH3AddGuide` —— 1/10 个有
- `MiniMaxH3AudioLatentControlT8` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `VHS_VideoCombine` —— 1/10 个有
- `VideoCombineV2` —— 1/10 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/10 个有
- `easy indexTTSAudioMerge` —— 1/10 个有
- `easy indexTTSGenerate` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
