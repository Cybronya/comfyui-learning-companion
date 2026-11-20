---
name: text_to_image_lora_sampler_clip_414
type: Text To Image
frequency: 5
level: strong
coverage: 0.8674
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json, 视频生成/图生视频/Minimax H3单图生视频｜极速15秒直出1080P高清成片_2108394651400105985.json, 视频生成/图生视频/唱歌对口型数字人｜Minimax H3含提示词模版视频_2092744057880666114.json, 视频生成/图生视频/电影感多参迅捷｜minimax H3防拉丝图生视频工作流_2093110076662968321.json, 视频生成/文生视频/MinimaxH3完美优化版 生视频质量与速度双优_2104296777661902850.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_414

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3一站式工作流｜文生参考生视频全都要_2111319112474521601.json、视频生成/图生视频/Minimax H3单图生视频｜极速15秒直出1080P高清成片_2108394651400105985.json、视频生成/图生视频/唱歌对口型数字人｜Minimax H3含提示词模版视频_2092744057880666114.json、视频生成/图生视频/电影感多参迅捷｜minimax H3防拉丝图生视频工作流_2093110076662968321.json、视频生成/文生视频/MinimaxH3完美优化版 生视频质量与速度双优_2104296777661902850.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 4/5 个有
- `LoadAudio` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `LoadVideo` —— 3/5 个有
- `MiniMaxH3EasyLoader` —— 3/5 个有
- `MiniMaxH3EasyModelAdapter` —— 3/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/5 个有
- `MiniMaxH3TurboLoRA` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `ModelAttentionBackend` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `SpectrumApplyMiniMaxH3` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `DuckHideNode` —— 1/5 个有
- `ExtendIntermediateSigmas` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `H3SigmaRefiner` —— 1/5 个有
- `MiniMaxH3SigmaShift` —— 1/5 个有
- `MiniMaxH3TurboSampler` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
