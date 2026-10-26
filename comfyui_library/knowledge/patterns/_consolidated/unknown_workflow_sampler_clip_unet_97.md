---
name: unknown_workflow_sampler_clip_unet_97
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.935455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/自己用：标题字设计_qwen-image-2.0_1971022262755332097.json, 图片生成/文生图/1 超清人像 Z-image turbo_2071175125273239553.json, 图片生成/文生图/2029905977360785409.json, 图片生成/文生图/Flux2.0-Dev _ 文生图_1993501652189642754.json, 图片生成/文生图/Flux2文生图_1993378851996844034.json, 图片生成/文生图/Flux2文生图官方版_1993503885006405633.json, 图片生成/文生图/Z-Image-Turbo 8步出图_2005643797847572481.json, 图片生成/文生图/Z-Image批量文生图_1993908239676932097.json, 图片生成/文生图/千问AI工作台_字体生成_2048680548826091521.json, 图片生成/文生图/字体设计_qwen-image-2.0_2023648217132441602.json, 图片生成/文生图/字体设计_qwen-image-2.0_2037759609598906370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_97

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/自己用：标题字设计_qwen-image-2.0_1971022262755332097.json、图片生成/文生图/1 超清人像 Z-image turbo_2071175125273239553.json、图片生成/文生图/2029905977360785409.json、图片生成/文生图/Flux2.0-Dev _ 文生图_1993501652189642754.json、图片生成/文生图/Flux2文生图_1993378851996844034.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `ModelSamplingAuraFlow` —— 8/11 个有
- `CR Text` —— 7/11 个有
- `easy promptList` —— 6/11 个有
- `PreviewImage` —— 5/11 个有
- `CR Text Input Switch (4 way)` —— 4/11 个有
- `CR Text Replace` —— 4/11 个有
- `LayerUtility: PurgeVRAM V2` —— 2/11 个有
- `Bookmark (rgthree)` —— 1/11 个有
- `FromListGet1Image` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 11 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 31% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（9/11 个样本）：Steps较低可能导致细节不足
