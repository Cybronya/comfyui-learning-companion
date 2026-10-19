---
name: unknown_workflow_lora_sampler_clip_28
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.843429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio, CR Simple Prompt List, GlobalSeed //Inspire]
members: [图片生成/文生图/1955060284899692545.json, 图片生成/文生图/1955157274396430337.json, 图片生成/文生图/1968571302049140738.json, 图片生成/文生图/1981285976733638658.json, 图片生成/文生图/1984457132592480258.json, 图片生成/文生图/1985931273690591234.json, 图片生成/文生图/1987591657719836673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1955060284899692545.json、图片生成/文生图/1955157274396430337.json、图片生成/文生图/1968571302049140738.json、图片生成/文生图/1981285976733638658.json、图片生成/文生图/1984457132592480258.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/7 个有
- `TextInput_` —— 2/7 个有
- `CR Simple Prompt List` —— 1/7 个有
- `EmptyUnitGenerator_UTK` —— 1/7 个有
- `GlobalSeed //Inspire` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.52 | 7 | 83% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 0.1 - 1 | 7 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.52，7 个样本，取值集中（一致性 83%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，7 个样本
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio、CR Simple Prompt List、GlobalSeed //Inspire
