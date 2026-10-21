---
name: unknown_workflow_sampler_clip_unet_99
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.980143
common_nodes: [CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-base造相完全体模型_2016501183799631873.json, 图片生成/文生图/Z-image文生图_2016334900588191745.json, 图片生成/文生图/Z-image最新文生图，超细腻画面_2018208815497351170.json, 图片生成/文生图/Z-image模型 文生图_2068898439915728897.json, 图片生成/文生图/Z-image真实文生图_2020214420164583425.json, 图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json, 图片生成/文生图/qwen-image2512-8步-BF16+Z-image去AII感一体流_2008885693623308290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_99

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z-image-base造相完全体模型_2016501183799631873.json、图片生成/文生图/Z-image文生图_2016334900588191745.json、图片生成/文生图/Z-image最新文生图，超细腻画面_2018208815497351170.json、图片生成/文生图/Z-image模型 文生图_2068898439915728897.json、图片生成/文生图/Z-image真实文生图_2020214420164583425.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 6/7 个有
- `EmptySD3LatentImage` —— 6/7 个有
- `CR Text` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `ClipLoaderGGUF` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `MemoryCleaner` —— 1/7 个有
- `SDXLEmptyLatentSizePicker+` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 50 | 7 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 7 | 31% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.19 - 1 | 7 | 68% |
| 宽度 | 768x1344 (0.57) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 33% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 50，7 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，7 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.19 - 1，7 个样本
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
