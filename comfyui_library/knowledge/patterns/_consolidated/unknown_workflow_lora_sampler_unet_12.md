---
name: unknown_workflow_lora_sampler_unet_12
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.8095
common_nodes: [CLIPLoader, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, String Literal, Seed (rgthree)]
members: [图片生成/文生图/1963214327899721729.json, 图片生成/文生图/1970739735536824321.json, 图片生成/文生图/1971395682378661889.json, 图片生成/文生图/1977995730776379394.json, 图片生成/文生图/1980164055954526209.json, 图片生成/文生图/1981265802265616385.json, 图片生成/文生图/1983097610955333634.json, 图片生成/文生图/1983138603914174466.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1963214327899721729.json、图片生成/文生图/1970739735536824321.json、图片生成/文生图/1971395682378661889.json、图片生成/文生图/1977995730776379394.json、图片生成/文生图/1980164055954526209.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `EmptySD3LatentImage` —— 7/8 个有
- `LoadImage` —— 3/8 个有
- `TextEncodeQwenImageEdit` —— 3/8 个有
- `CFGNorm` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `String Literal` —— 2/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 8 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 60% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，8 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM V2、String Literal、Seed (rgthree)
