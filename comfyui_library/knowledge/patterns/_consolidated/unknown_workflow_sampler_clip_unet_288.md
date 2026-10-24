---
name: unknown_workflow_sampler_clip_unet_288
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.90775
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen imgae edit图像编辑模型 8步极速版-StarAI_1957694342792146946.json, 图片生成/图生图/千问 批量生成同一人物不同场景图片_1960644814964424706.json, 图片生成/图生图/千问 改图 极速版_2068917331832696833.json, 图片生成/文生图/Qwen-Image-文生图批量_1953016614931337218.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_288

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen imgae edit图像编辑模型 8步极速版-StarAI_1957694342792146946.json、图片生成/图生图/千问 批量生成同一人物不同场景图片_1960644814964424706.json、图片生成/图生图/千问 改图 极速版_2068917331832696833.json、图片生成/文生图/Qwen-Image-文生图批量_1953016614931337218.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Int` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `TextEncodeQwenImageEdit` —— 3/4 个有
- `CR Prompt List` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Text` —— 2/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
