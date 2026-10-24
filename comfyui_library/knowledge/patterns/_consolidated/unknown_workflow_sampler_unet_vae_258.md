---
name: unknown_workflow_sampler_unet_vae_258
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888667
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json, 图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json, 图片生成/图生图/image_qwen_image_2_1_ref2i_2102667025813426177.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_258

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1深度图-线稿-转图片_2112646802997596161.json、图片生成/图生图/Qwen2.1图像编辑_2101937813171302401.json、图片生成/图生图/image_qwen_image_2_1_ref2i_2102667025813426177.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 2/3 个有
- `StringToInt` —— 2/3 个有
- `Text` —— 2/3 个有
- `PrimitiveString` —— 1/3 个有
- `QwenImage21UnionApply` —— 1/3 个有
- `QwenImage21UnionLoader` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 30 | 3 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 16 - 1024 | 3 | 31% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 16 - 1024，3 个样本，取值分散，一致性仅 31%
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
