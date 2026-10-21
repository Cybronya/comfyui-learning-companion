---
name: unknown_workflow_sampler_clip_unet_125
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.7068
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR SDXL Aspect Ratio]
members: [图片生成/文生图/1968001076735651842.json, 图片生成/文生图/Krea2_turbo_fp8文生图_2083589922623156226.json, 图片生成/文生图/Krea2文生图_2083457731943555073.json, 图片生成/文生图/Qwen-image 字体设计工作流_2091481144717041665.json, 图片生成/文生图/工作流基础系列34-Krea2文生图工作流_2069974370528874497.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1968001076735651842.json、图片生成/文生图/Krea2_turbo_fp8文生图_2083589922623156226.json、图片生成/文生图/Krea2文生图_2083457731943555073.json、图片生成/文生图/Qwen-image 字体设计工作流_2091481144717041665.json、图片生成/文生图/工作流基础系列34-Krea2文生图工作流_2069974370528874497.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `Seed (rgthree)` —— 3/5 个有
- `AddLabel` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 5 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.1 | 5 | 35% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，5 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.1，5 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio
