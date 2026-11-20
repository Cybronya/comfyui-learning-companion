---
name: text_to_image_lora_sampler_clip_585
type: Text To Image
frequency: 3
level: strong
coverage: 0.856333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/多合一极简版工作流｜MinimaxH3配套优化提示词多模式视频生成_2097024456110723073.json, 视频生成/文生视频/多合一极简版｜那颗星星MinimaxH3三模工作流_2093782956832804866.json, 视频生成/文生视频/极简版多合一0830｜MinimaxH3文生视频生视频_2095591499948978177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_585

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/多合一极简版工作流｜MinimaxH3配套优化提示词多模式视频生成_2097024456110723073.json、视频生成/文生视频/多合一极简版｜那颗星星MinimaxH3三模工作流_2093782956832804866.json、视频生成/文生视频/极简版多合一0830｜MinimaxH3文生视频生视频_2095591499948978177.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
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
- `CreateVideo` —— 2/3 个有
- `LTXVConcatAVLatent` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `MiniMaxH3EasyMediaLoader` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `ModelPreviewOverrideKJ` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `workflow>声音` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
