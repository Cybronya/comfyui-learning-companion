---
name: unknown_workflow_sampler_clip_vae_10
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.889778
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [SDXLEmptyLatentSizePicker+, LayerUtility: PurgeVRAM, easy seed]
members: [图片生成/文生图/1960187196420599809.json, 图片生成/文生图/1960520624663949314.json, 图片生成/文生图/1961312747210346498.json, 图片生成/文生图/1963054435381522434.json, 图片生成/文生图/1963114884189884418.json, 图片生成/文生图/1964600749260947457.json, 图片生成/文生图/1965030044580069377.json, 图片生成/文生图/1965043199712612353.json, 图片生成/文生图/image_qwen_Image_2512_2018879224546856962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1960187196420599809.json、图片生成/文生图/1960520624663949314.json、图片生成/文生图/1961312747210346498.json、图片生成/文生图/1963054435381522434.json、图片生成/文生图/1963114884189884418.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `CFGNorm` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `NunchakuQwenImageLoraLoader1` —— 1/9 个有
- `NunchakuQwenImageLoraStackV3` —— 1/9 个有
- `ResizeAndPadImage` —— 1/9 个有
- `SDXLEmptyLatentSizePicker+` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 9 | 53% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 9 | 71% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1344x768 (1.75) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、LayerUtility: PurgeVRAM、easy seed
