---
name: unknown_workflow_sampler_clip_vae_5
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.896875
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [SDXLEmptyLatentSizePicker+, LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1960187196420599809.json, 图片生成/文生图/1960520624663949314.json, 图片生成/文生图/1961312747210346498.json, 图片生成/文生图/1963054435381522434.json, 图片生成/文生图/1963114884189884418.json, 图片生成/文生图/1964600749260947457.json, 图片生成/文生图/1964993982478602241.json, 图片生成/文生图/1968150332159197185.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1960187196420599809.json、图片生成/文生图/1960520624663949314.json、图片生成/文生图/1961312747210346498.json、图片生成/文生图/1963054435381522434.json、图片生成/文生图/1963114884189884418.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 7/8 个有
- `NunchakuQwenImageDiTLoader` —— 7/8 个有
- `UNETLoader` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `NunchakuQwenImageLoraLoader1` —— 1/8 个有
- `ResizeAndPadImage` —— 1/8 个有
- `SDXLEmptyLatentSizePicker+` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | 8 - 20 | 8 | 63% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 3.5 | 8 | 64% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1344x768 (1.75) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17.5，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 3.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、LayerUtility: PurgeVRAM
