---
name: unknown_workflow_sampler_clip_unet_18
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.917636
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: PurgeVRAM, Seed Everywhere]
members: [图片生成/文生图/1953351554604695553.json, 图片生成/文生图/1953390443667095554.json, 图片生成/文生图/1953691322731429889.json, 图片生成/文生图/1953710081516994562.json, 图片生成/文生图/1953747187043848193.json, 图片生成/文生图/1954027659858890754.json, 图片生成/文生图/1954190525895196674.json, 图片生成/文生图/1954435913382281217.json, 图片生成/文生图/1954444879856332802.json, 图片生成/文生图/1954463793558515714.json, 图片生成/文生图/1954550112557121538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1953351554604695553.json、图片生成/文生图/1953390443667095554.json、图片生成/文生图/1953691322731429889.json、图片生成/文生图/1953710081516994562.json、图片生成/文生图/1953747187043848193.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `RH_LLMAPI_NODE` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `FluxResolutionNode` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `LoadImage` —— 1/11 个有
- `Seed Everywhere` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 11 | 80% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 11 | 45% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，11 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，11 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: PurgeVRAM、Seed Everywhere
