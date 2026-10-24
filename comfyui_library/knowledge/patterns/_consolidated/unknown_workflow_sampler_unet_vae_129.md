---
name: unknown_workflow_sampler_unet_vae_129
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.749375
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json, 图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json, 图片生成/图生图/QwenImage2.1图像编辑_2101863711043579906.json, 图片生成/图生图/qwen_image_2_1_图像编辑-换背景和姿态_2102207016054906881.json, 图片生成/图生图/qwen_image_2_1_图像编辑-换装_2101845419922903041.json, 图片生成/图生图/qwen_image_2_1_图像编辑-文本换装_2101852516261646337.json, 图片生成/图生图/qwen_image_2_1_手持指定物品_2102203525789995009.json, 图片生成/图生图/▶Qwen-image21-图像编辑（无位移）_2112039096406331394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_129

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json、图片生成/图生图/QwenImage2.1-角色三视图-bf16展开版_2106018495979941889.json、图片生成/图生图/QwenImage2.1图像编辑_2101863711043579906.json、图片生成/图生图/qwen_image_2_1_图像编辑-换背景和姿态_2102207016054906881.json、图片生成/图生图/qwen_image_2_1_图像编辑-换装_2101845419922903041.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `easy loraStack` —— 2/8 个有
- `easy loraStackApply` —— 2/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 8 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 8 | 71% |
| 高度 | 1024 | 1024 - 1536 | 8 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，8 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，8 个样本
- 高度 中位数 1024，观测区间 1024 - 1536，8 个样本，取值集中（一致性 85%）
