---
name: unknown_workflow_lora_sampler_unet_164
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.634
common_nodes: [CLIPLoader, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json, 图片生成/图生图/一键换头-qwen image2.1最新迁移_2107910635219668994.json, 图片生成/图生图/多角度转换-Qwen image2.1图像编辑_2108180448810725378.json, 图片生成/图生图/服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_164

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 _身体替换_2108413083428417538.json、图片生成/图生图/一键换头-qwen image2.1最新迁移_2107910635219668994.json、图片生成/图生图/多角度转换-Qwen image2.1图像编辑_2108180448810725378.json、图片生成/图生图/服装迁移-Qwen image2.1最新迁移工作流_2108227439682998273.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `InvertMask` —— 2/4 个有
- `JoinImageWithAlpha` —— 2/4 个有
- `LoadBackgroundRemovalModel` —— 2/4 个有
- `RemoveBackground` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 8 | 8 - 40 | 4 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | deis_2m | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 40，4 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis_2m，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
