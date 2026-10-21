---
name: text_to_image_sampler_clip_checkpoint_14
type: Text To Image
frequency: 5
level: moderate
coverage: 0.98
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1979490298709577729.json, 图片生成/文生图/1989688004904185857.json, 图片生成/文生图/Anima最新动漫文生图模型_2018993897048903682.json, 视频生成/图生视频/2053664172625408002.json, 视频生成/图生视频/2053673513051013121.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1979490298709577729.json、图片生成/文生图/1989688004904185857.json、图片生成/文生图/Anima最新动漫文生图模型_2018993897048903682.json、视频生成/图生视频/2053664172625408002.json、视频生成/图生视频/2053673513051013121.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `IPAdapterUnifiedLoader` —— 3/5 个有
- `IPAdapterAdvanced` —— 2/5 个有
- `IPAdapterStyleComposition` —— 1/5 个有
- `WD14Tagger|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 40 | 5 | 72% |
| Prompt 约束强度(CFG) | 7 | 4.5 - 8 | 5 | 81% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 512 - 1280 | 5 | 71% |
| 高度 | 720 | 512 - 1536 | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 4.5 - 8，5 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1280，5 个样本
- 高度 中位数 720，观测区间 512 - 1536，5 个样本
