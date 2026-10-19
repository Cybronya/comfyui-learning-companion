---
name: text_to_image_lora_sampler_clip_88
type: Text To Image
frequency: 10
level: strong
coverage: 0.6619
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax-H3疯狂测试工作流｜文生视频视频生视频_2095216174060630017.json, 视频生成/文生视频/Ref2VA多参考全能生成｜MiniMax H3文生图生视频工作流_2093072782388187137.json, 视频生成/文生视频/Ref2VA多参考｜MiniMax H3全能视频生成直出_2090570005984407553.json, 视频生成/文生视频/多参考全能生成｜MiniMax H3 Ref2VA视频处理_2093230903848947714.json, 视频生成/文生视频/多合一生视频V3.0｜Minimax H3文生首尾图参二采高清放大_2090209607414276097.json, 视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json, 视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json, 视频生成/文生视频/疯狂测试全通过｜MiniMax H3三模输入全能出片_2096527562737541121.json, 视频生成/文生视频/疯狂测试工作流｜Aiden MiniMax-H3文生视频视频生视频_2095553065045807106.json, 视频生成/文生视频/疯狂测试工作流｜MiniMax H3文生视频图生视频多模式_2096295220886466562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3疯狂测试工作流｜文生视频视频生视频_2095216174060630017.json、视频生成/文生视频/Ref2VA多参考全能生成｜MiniMax H3文生图生视频工作流_2093072782388187137.json、视频生成/文生视频/Ref2VA多参考｜MiniMax H3全能视频生成直出_2090570005984407553.json、视频生成/文生视频/多参考全能生成｜MiniMax H3 Ref2VA视频处理_2093230903848947714.json、视频生成/文生视频/多合一生视频V3.0｜Minimax H3文生首尾图参二采高清放大_2090209607414276097.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：66%

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
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
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
- `LoadAudio` —— 9/10 个有
- `VHS_LoadVideo` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `MinimaxH3LatentUpscaler3D` —— 8/10 个有
- `ModelPreviewOverrideKJ` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `AudioCrop` —— 7/10 个有
- `GetNode` —— 7/10 个有
- `ModelAttentionBackend` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `MiniMaxChunkFeedForward` —— 6/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/10 个有
- `MiniMaxLowVRAMAttention` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `SplitSigmas` —— 6/10 个有
- `忽略多组孤海` —— 6/10 个有
- `easy boolean` —— 5/10 个有
- `ComfySwitchNode` —— 4/10 个有
- `H3SigmaRefiner` —— 4/10 个有
- `easy positive` —— 4/10 个有
- `Any Switch (rgthree)` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `PathchSageAttentionKJ` —— 3/10 个有
- `SolAttnPatch` —— 3/10 个有
- `StringFunction|pysssss` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `H3AudioRefineSampler` —— 2/10 个有
- `H3FrozenVideoCache` —— 2/10 个有
- `Int` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `ManualSigmas` —— 2/10 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `MiniMaxH3HybridLoader` —— 1/10 个有
- `easy ifElse` —— 1/10 个有

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
