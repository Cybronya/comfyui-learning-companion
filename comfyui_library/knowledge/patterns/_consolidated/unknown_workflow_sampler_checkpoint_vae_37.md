---
name: unknown_workflow_sampler_checkpoint_vae_37
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.703333
common_nodes: [CR Text, CheckpointLoaderSimple, ImageResize+, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen 2511(多图编辑)_2016095857417920514.json, 图片生成/图生图/qwen文生图（单图编辑）_1996263680994066434.json, 图片生成/图生图/指定更换人物姿势_1996623433322610689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_37

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen 2511(多图编辑)_2016095857417920514.json、图片生成/图生图/qwen文生图（单图编辑）_1996263680994066434.json、图片生成/图生图/指定更换人物姿势_1996623433322610689.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | lcm | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
