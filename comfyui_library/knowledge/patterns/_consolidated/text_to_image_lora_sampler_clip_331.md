---
name: text_to_image_lora_sampler_clip_331
type: Text To Image
frequency: 6
level: strong
coverage: 0.859833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/minmax生图工作流｜多人姿势迁移视频制作_2097811139928354818.json, 视频生成/文生视频/上下文文生视频扩写2K｜MiniMax H3一句话生成工作流_2096737308723728385.json, 视频生成/文生视频/上下文竖屏极速文生｜MiniMax H3一句话短视频生成_2096738714239197185.json, 视频生成/文生视频/低价批量视频生成｜文生图生视频生视频模型直出_2093139939205668866.json, 音频生成/音频生成/AI配音神器｜MiniMax音色设计一句话出成片配音｜音频生成创意玩法_2099111925031464962.json, 音频生成/音频生成/文生音乐工作流｜MiniMax Music 2.6一句话生成专属配乐｜音频生成_2099151761704579073.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_331

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/minmax生图工作流｜多人姿势迁移视频制作_2097811139928354818.json、视频生成/文生视频/上下文文生视频扩写2K｜MiniMax H3一句话生成工作流_2096737308723728385.json、视频生成/文生视频/上下文竖屏极速文生｜MiniMax H3一句话短视频生成_2096738714239197185.json、视频生成/文生视频/低价批量视频生成｜文生图生视频生视频模型直出_2093139939205668866.json、音频生成/音频生成/AI配音神器｜MiniMax音色设计一句话出成片配音｜音频生成创意玩法_2099111925031464962.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `RH_MinimaxHailuoH3ContextIrText` —— 2/6 个有
- `RH_MinimaxHailuoH3TextToVideo` —— 2/6 个有
- `SaveAudio` —— 2/6 个有
- `LoadImage` —— 1/6 个有
- `RH_BytedanceSeedance25TokenTextToVideo` —— 1/6 个有
- `RH_MinimaxMusic26` —— 1/6 个有
- `RH_MinimaxVoiceDesign` —— 1/6 个有
- `RelayGrokImagineVideo` —— 1/6 个有

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
