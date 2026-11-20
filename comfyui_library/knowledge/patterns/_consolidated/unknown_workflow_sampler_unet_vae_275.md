---
name: unknown_workflow_sampler_unet_vae_275
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.83
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1万物移除工作流｜图生图一键抹除多余物体无痕迹_2108760305202458625.json, 图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json, 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_275

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1万物移除工作流｜图生图一键抹除多余物体无痕迹_2108760305202458625.json、图片生成/文生图/OWEN IMAGE 2.1 文生图_2103073574478245890.json、图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `SaveImageAdvanced` —— 2/3 个有
- `DrawMaskOnImage` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `PixaromaRunTimer` —— 1/3 个有
- `PixaromaSeed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 3 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
