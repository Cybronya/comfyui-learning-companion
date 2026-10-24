---
name: unknown_workflow_sampler_unet_vae_204
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8348
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/参考图一键调色_2112107742885404674.json, 图片生成/图生图/多参考图生成图片 1底图-5参考图_2112078134458806274.json, 图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json, 图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json, 图片生成/文生图/多图编辑工作流_2105329811446124546.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_204

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/参考图一键调色_2112107742885404674.json、图片生成/图生图/多参考图生成图片 1底图-5参考图_2112078134458806274.json、图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json、图片生成/文生图/image_qwen_image_2_1_background_removal_2109217853978271745.json、图片生成/文生图/多图编辑工作流_2105329811446124546.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 4/5 个有
- `EmptyLatentImage` —— 3/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1152 | 944 - 2048 | 3 | 65% |
| 高度 | 1536 | 1280 - 1672 | 3 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，观测区间 944 - 2048，3 个样本
- 高度 中位数 1536，观测区间 1280 - 1672，3 个样本，取值集中（一致性 89%）
