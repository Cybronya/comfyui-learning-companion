---
name: unknown_workflow_sampler_unet_vae_252
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8896
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1万物移除工作流｜图生图一键抹除多余物体无痕迹_2108760305202458625.json, 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json, 图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json, 图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json, 图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_252

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1万物移除工作流｜图生图一键抹除多余物体无痕迹_2108760305202458625.json、图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json、图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json、图片生成/文生图/文生图-qwen image2.1_2101922635541213185.json、图片生成/文生图/文生图-qwen image2.1_2104155833666990081.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `DrawMaskOnImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `Mask Fill Holes` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
