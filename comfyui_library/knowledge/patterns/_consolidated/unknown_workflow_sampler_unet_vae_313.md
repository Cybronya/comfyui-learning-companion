---
name: unknown_workflow_sampler_unet_vae_313
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.832667
common_nodes: [CLIPLoader, EmptyLatentImage, ImageResizeKJv2, ImageScaleToTotalPixels, KSampler, LoadImage, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image 2.1 六_九宫格分镜图一键生成_2114274935857307650.json, 图片生成/图生图/Qwen-Image 2.1六九宫格分镜图｜一键生成组图分镜的工作流_2114723276877557761.json, 图片生成/图生图/真2K 白底图_1979202132073156610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_313

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Image 2.1 六_九宫格分镜图一键生成_2114274935857307650.json、图片生成/图生图/Qwen-Image 2.1六九宫格分镜图｜一键生成组图分镜的工作流_2114723276877557761.json、图片生成/图生图/真2K 白底图_1979202132073156610.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `ImageRemoveAlpha+` —— 2/3 个有
- `TTP_Image_Tile_Batch` —— 2/3 个有
- `VOSR2ModelLoader` —— 2/3 个有
- `VOSR2Upscale` —— 2/3 个有
- `easy boolean` —— 2/3 个有
- `easy imageSwitch` —— 2/3 个有
- `easy mathInt` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 8 - 25 | 3 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 8 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
