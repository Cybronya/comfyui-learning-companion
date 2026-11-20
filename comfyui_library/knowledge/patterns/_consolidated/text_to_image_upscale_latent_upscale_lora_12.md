---
name: text_to_image_upscale_latent_upscale_lora_12
type: Text To Image
frequency: 5
level: strong
coverage: 0.8904
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyOutput, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/二采潜空间放大极简版｜MinimaxH3文生图生视频_2091597395741204481.json, 视频生成/文生视频/去油全模式精简流｜MINIMAXH3独立双采样生成_2095128913096822786.json, 视频生成/文生视频/多合一极简版工作流｜MinimaxH3配套优化提示词多模式视频生成_2097024456110723073.json, 视频生成/文生视频/极简版多合一0830｜MinimaxH3文生视频生视频_2095591499948978177.json, 视频生成/文生视频/极简节点二采放大｜那颗星星MinimaxH3潜空间强化_2091769005567725569.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/二采潜空间放大极简版｜MinimaxH3文生图生视频_2091597395741204481.json、视频生成/文生视频/去油全模式精简流｜MINIMAXH3独立双采样生成_2095128913096822786.json、视频生成/文生视频/多合一极简版工作流｜MinimaxH3配套优化提示词多模式视频生成_2097024456110723073.json、视频生成/文生视频/极简版多合一0830｜MinimaxH3文生视频生视频_2095591499948978177.json、视频生成/文生视频/极简节点二采放大｜那颗星星MinimaxH3潜空间强化_2091769005567725569.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyOutput`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `H3SigmaRefiner` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `MiniMaxH3EasyModelAdapter` —— 3/5 个有
- `MiniMaxH3EasySecondPassConditioning` —— 3/5 个有
- `ModelAttentionBackend` —— 3/5 个有
- `ModelPreviewOverrideKJ` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `GetLatentSizeAndCount` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `LoadVideo` —— 2/5 个有
- `MiniMaxH3EasyLoader` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `SolAttnMiniMax` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `MiniMaxH3EasyMediaLoader` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `workflow>声音` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
