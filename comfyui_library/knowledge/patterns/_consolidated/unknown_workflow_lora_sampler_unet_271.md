---
name: unknown_workflow_lora_sampler_unet_271
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.939
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超级便宜的双图编辑，用自然语言就能P图了2511_2003698926928707585.json, 图片生成/文生图/qwen image 2512 文生图_2091417972459008001.json, 平台全量/Qwen Edit 2511三图编辑_2004177267125305346.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_271

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/超级便宜的双图编辑，用自然语言就能P图了2511_2003698926928707585.json、图片生成/文生图/qwen image 2512 文生图_2091417972459008001.json、平台全量/Qwen Edit 2511三图编辑_2004177267125305346.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 768 - 2648 | 3 | 44% |
| 高度 | 1704 | 1280 - 3528 | 3 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 2648，3 个样本，取值分散，一致性仅 44%
- 高度 中位数 1704，观测区间 1280 - 3528，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
