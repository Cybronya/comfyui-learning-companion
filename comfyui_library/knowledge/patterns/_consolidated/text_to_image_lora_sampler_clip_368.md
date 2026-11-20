---
name: text_to_image_lora_sampler_clip_368
type: Text To Image
frequency: 6
level: strong
coverage: 0.907167
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minimaxlora）ENG加速一站式工作流（文生视频图生视频首尾帧全能参考加速ENG_2087115789043331074.json, 视频生成/文生视频/加速lora一站式｜minimax文生图生视频首尾帧全能参考_2092878945308991490.json, 视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json, 视频生成/文生视频/多合一极简工作流｜那颗星星MinimaxH3视频生成_2093449231817330689.json, 视频生成/文生视频/多合一极简版｜那颗星星MinimaxH3三模工作流_2093782956832804866.json, 视频生成/文生视频/海螺Minimax H3开源版文生视频H3加速Lora6步直出1080P_2086443392405430273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_368

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/minimaxlora）ENG加速一站式工作流（文生视频图生视频首尾帧全能参考加速ENG_2087115789043331074.json、视频生成/文生视频/加速lora一站式｜minimax文生图生视频首尾帧全能参考_2092878945308991490.json、视频生成/文生视频/即梦写法MiniMax_H3_全能参考文生视频视频生视频图生视频_2086539152329371650.json、视频生成/文生视频/多合一极简工作流｜那颗星星MinimaxH3视频生成_2093449231817330689.json、视频生成/文生视频/多合一极简版｜那颗星星MinimaxH3三模工作流_2093782956832804866.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/6 个有
- `BasicScheduler` —— 4/6 个有
- `KSamplerSelect` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `SpectrumSDXL` —— 2/6 个有
- `AudioAdjustVolume` —— 1/6 个有
- `EasyCache` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
