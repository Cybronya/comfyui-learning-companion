---
name: text_to_image_lora_sampler_clip_273
type: Text To Image
frequency: 4
level: strong
coverage: 0.806
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadVideo, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/数字人口型同步神器｜口型语音精准对齐不穿帮_2106622328892379137.json, 视频生成/图生视频/爆款短视频复刻｜一张图动作运镜节奏一键迁移MiniMax H3_2089825604421115906.json, 视频生成/文生视频/全能参考生视频2K版｜海螺MiniMaxH3官方多图音视频参考_2088745519744110594.json, 视频生成/文生视频/视频生成2KMiniMaxH3版ENG海螺_2087117391724634114.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_273

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/数字人口型同步神器｜口型语音精准对齐不穿帮_2106622328892379137.json、视频生成/图生视频/爆款短视频复刻｜一张图动作运镜节奏一键迁移MiniMax H3_2089825604421115906.json、视频生成/文生视频/全能参考生视频2K版｜海螺MiniMaxH3官方多图音视频参考_2088745519744110594.json、视频生成/文生视频/视频生成2KMiniMaxH3版ENG海螺_2087117391724634114.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 2/4 个有
- `FL_CosyVoice3_ModelLoader` —— 1/4 个有
- `FL_CosyVoice3_ZeroShot` —— 1/4 个有
- `GetVideoComponents` —— 1/4 个有
- `LatentSyncNode` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RHMiniMaxH3RefGen` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
