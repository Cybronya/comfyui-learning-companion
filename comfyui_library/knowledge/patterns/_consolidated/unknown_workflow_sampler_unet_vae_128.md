---
name: unknown_workflow_sampler_unet_vae_128
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.866375
common_nodes: [CLIPLoader, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json, 图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json, 图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json, 图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json, 图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json, 图片生成/文生图/Qwen-Image-2.1-Turbo 汉服美学_2110739133755912194.json, 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_128

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1 抠图-(透明通道)_2105182900231696386.json、图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json、图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json、图片生成/图生图/Qwen-image2.1 图像编辑_2111261410541006850.json、图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104424127888187394.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `EmptyLatentImage` —— 6/8 个有
- `CR Prompt Text` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `QwenImage21Cache` —— 5/8 个有
- `ResolutionSelector` —— 5/8 个有
- `ComfySwitchNode` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `Color Grading JK` —— 1/8 个有
- `FastGroupsBypassSwitch` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `WujiUpscaler2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 6 - 45 | 8 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1560 | 6 | 82% |
| 高度 | 1024 | 904 - 1920 | 6 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 6 - 45，8 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1560，6 个样本，取值集中（一致性 82%）
- 高度 中位数 1024，观测区间 904 - 1920，6 个样本
