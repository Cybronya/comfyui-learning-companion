---
name: text_to_image_sampler_clip_checkpoint_11
type: Text To Image
frequency: 6
level: moderate
coverage: 0.9625
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM, easy sleep]
members: [图片生成/文生图/1970130948895481857.json, 图片生成/文生图/1971226483622658049.json, 图片生成/文生图/1971569561394933761.json, 图片生成/文生图/1977361796124286978.json, 图片生成/文生图/1979133818235949058.json, 图片生成/文生图/251225001.014.Zimage-文生图破甲性能提升-NF_2004253893129371650.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1970130948895481857.json、图片生成/文生图/1971226483622658049.json、图片生成/文生图/1971569561394933761.json、图片生成/文生图/1977361796124286978.json、图片生成/文生图/1979133818235949058.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `easy sleep` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1280 | 6 | 66% |
| 高度 | 1152 | 512 - 1920 | 6 | 61% |
| 采样步数 | 17.5 | 4 - 20 | 6 | 59% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 6 | 22% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | beta | - | 6 | 17% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1280，6 个样本
- 高度 中位数 1152，观测区间 512 - 1920，6 个样本
- 采样步数 中位数 17.5，观测区间 4 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，6 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 beta，6 个样本，一致性 17%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、easy sleep
