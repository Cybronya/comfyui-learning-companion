---
name: unknown_workflow_sampler_unet_vae_148
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.68425
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline]
members: [图片生成/图生图/2102013171056857089.json, 图片生成/图生图/2105656720168148993.json, 图片生成/图生图/2106041136610635778.json, 图片生成/图生图/2106043418517524481.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_148

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2102013171056857089.json、图片生成/图生图/2105656720168148993.json、图片生成/图生图/2106041136610635778.json、图片生成/图生图/2106043418517524481.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `Int` —— 1/4 个有
- `QwenImage21Cache` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32.5 | 25 - 50 | 4 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 32.5，观测区间 25 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline
