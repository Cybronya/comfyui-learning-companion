---
name: unknown_workflow_sampler_unet_vae_207
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8026
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json, 图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json, 图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json, 图片生成/图生图/QwenImage2.1图像编辑_2101863711043579906.json, 图片生成/图生图/▶Qwen-image21-图像编辑（无位移）_2112039096406331394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_207

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1图片编辑+角色定妆照_2103068698557902850.json、图片生成/图生图/Qwen image 2.1图片编辑-1_2112506837907099650.json、图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json、图片生成/图生图/QwenImage2.1图像编辑_2101863711043579906.json、图片生成/图生图/▶Qwen-image21-图像编辑（无位移）_2112039096406331394.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ResolutionSelector` —— 3/5 个有
- `Seed (rgthree)` —— 3/5 个有
- `Label (rgthree)` —— 2/5 个有
- `easy loraStack` —— 2/5 个有
- `easy loraStackApply` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 16 - 1536 | 5 | 46% |
| 高度 | 1024 | 1024 - 2048 | 5 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 16 - 1536，5 个样本，取值分散，一致性仅 46%
- 高度 中位数 1024，观测区间 1024 - 2048，5 个样本
