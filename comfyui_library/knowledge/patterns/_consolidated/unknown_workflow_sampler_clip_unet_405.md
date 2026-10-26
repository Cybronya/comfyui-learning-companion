---
name: unknown_workflow_sampler_clip_unet_405
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.731
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, PreviewAny, SaveImage, StringFormat, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/②Z-Image + 七维提示词_2101557585508917250.json, 图片生成/文生图/③Z-image_Krea2七维提示词工作流_2101558430195609601.json, 图片生成/文生图/③Z-image_Krea2七维提示词工作流_2104836223427764225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_405

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/②Z-Image + 七维提示词_2101557585508917250.json、图片生成/文生图/③Z-image_Krea2七维提示词工作流_2101558430195609601.json、图片生成/文生图/③Z-image_Krea2七维提示词工作流_2104836223427764225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `SaveImage`
- `StringFormat`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `MmuuaiGroupBypass` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 24 | 3 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 3 | 19% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 24，3 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，3 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
