---
name: text_to_image_video_lora_sampler_46
type: Text To Image
frequency: 16
level: strong
coverage: 0.912438
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MinimaxH3多合一极简版｜配套优化提示词直接用｜数字人角色表演一步到位_2104765994072891393.json, 视频生成/图生视频/MINIMAX-H3去油精简流独立双采样｜角色一致性_2095589274757451777.json, 视频生成/图生视频/MINIMAX-H3开源最强去油全模式精简流｜双采样_2095579769827057666.json, 视频生成/图生视频/MINIMAXH3双采样V3全面升级｜文戏不油武戏不糊双模式_2110702226032386049.json, 视频生成/图生视频/Mnimaxh3极简流分块二采｜支持种子固定可复现｜图生视频稳定输出_2104772144688361474.json, 视频生成/图生视频/minimaxh3高质量数字人_口播视频生成省时省力_2106603151494303745.json, 视频生成/图生视频/高质量数字人MiniMax_H3工作流，数字人生成处理方案_2108732703087616001.json, 视频生成/图生视频/高质量数字人minimax h3 数字人视频生成方案_2105028607759446018.json, 视频生成/文生视频/MiniMax H3极简流分块二采，支持种子固定的文生视频图生视频方案_2103191478523752449.json, 视频生成/文生视频/Minimax H3多参单采优化兼顾速度质量与打斗 视频生成均衡版_2105413868599205889.json, 视频生成/文生视频/Minimax-H3多参单采优化｜速度质量打斗场面三兼顾_2105131373353848833.json, 视频生成/文生视频/MinimaxH3双采样V3文不油武不糊 全面升级视频生成工作流_2098694116875001857.json, 视频生成/文生视频/Mnimaxh3极简流分块二采｜种子固定方便复刻同款_2103076631169556482.json, 视频生成/文生视频/文戏提示词练习工作流 文生视频图生视频参数调试_2099202759265443842.json, 视频生成/文生视频/文戏提示词练习工作流 文生视频图生视频参数调试_2099584922162913282.json, 视频生成/文生视频/文戏提示词练习工作流｜文生视频图生视频两用，台词戏感慢慢磨_2099459096524181506.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（数字人/数字人/MinimaxH3多合一极简版｜配套优化提示词直接用｜数字人角色表演一步到位_2104765994072891393.json、视频生成/图生视频/MINIMAX-H3去油精简流独立双采样｜角色一致性_2095589274757451777.json、视频生成/图生视频/MINIMAX-H3开源最强去油全模式精简流｜双采样_2095579769827057666.json、视频生成/图生视频/MINIMAXH3双采样V3全面升级｜文戏不油武戏不糊双模式_2110702226032386049.json、视频生成/图生视频/Mnimaxh3极简流分块二采｜支持种子固定可复现｜图生视频稳定输出_2104772144688361474.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 16 个 workflow 都包含：
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
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 15/16 个有
- `H3SigmaRefiner` —— 15/16 个有
- `MiniMaxH3EasyModelAdapter` —— 15/16 个有
- `孤海注释` —— 15/16 个有
- `ModelAttentionBackend` —— 14/16 个有
- `LoadAudio` —— 13/16 个有
- `VAEDecodeAudio` —— 13/16 个有
- `LTXVConcatAVLatent` —— 11/16 个有
- `LTXVSeparateAVLatent` —— 11/16 个有
- `MinimaxH3LatentUpscaler3D` —— 11/16 个有
- `Seed (rgthree)` —— 11/16 个有
- `SplitSigmas` —— 11/16 个有
- `MiniMaxH3EasyMediaLoader` —— 10/16 个有
- `MiniMaxH3EasySecondPassConditioning` —— 10/16 个有
- `GoohaiMinimaxH3TiledSampler` —— 8/16 个有
- `SaveImage` —— 7/16 个有
- `VHS_LoadVideo` —— 7/16 个有
- `ModelPreviewOverrideKJ` —— 6/16 个有
- `ConditioningZeroOut` —— 5/16 个有
- `GetLatentSizeAndCount` —— 5/16 个有
- `LoadImage` —— 5/16 个有
- `MiniMaxChunkFeedForward` —— 5/16 个有
- `MiniMaxLowVRAMAttention` —— 5/16 个有
- `SelfLiftH3Sampler` —— 5/16 个有
- `LTXVAudioVAEEncode` —— 3/16 个有
- `SetLatentNoiseMask` —— 3/16 个有
- `SolidMask` —— 3/16 个有
- `TrimAudioDuration` —— 3/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/16 个有
- `EmptyImage` —— 1/16 个有
- `MiniMaxH3EasyLoader` —— 1/16 个有
- `PreviewImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
