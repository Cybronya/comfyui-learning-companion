---
name: unknown_workflow_sampler_unet_vae_130
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.695
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [PlaySound|pysssss, easy int]
members: [图片生成/图生图/2102301480060538882.json, 图片生成/图生图/2102585909454659586.json, 图片生成/图生图/2103753279908966401.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json, 图片生成/文生图/qwen image 2.1 编辑_2101987550209593345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_130

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102301480060538882.json、图片生成/图生图/2102585909454659586.json、图片生成/图生图/2103753279908966401.json、图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json、图片生成/文生图/qwen image 2.1 编辑_2101987550209593345.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 4/5 个有
- `TextGenerateLTX2Prompt` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `孤海注释` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 40 | 25 - 50 | 5 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：PlaySound|pysssss、easy int
