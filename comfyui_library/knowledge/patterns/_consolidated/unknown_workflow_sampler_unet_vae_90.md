---
name: unknown_workflow_sampler_unet_vae_90
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8989
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json, 图片生成/图生图/Flux3 图片强化_2114538601471111169.json, 图片生成/图生图/Flux3-Klein-图像编辑_2111109110757412866.json, 图片生成/图生图/Moss-image-局部重绘_2112544404337676289.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2110648449984196609.json, 图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json, 图片生成/图生图/flux3_klein_image_edit图像编辑_2110972221408763906.json, 图片生成/图生图/flux3_klein_image_edit图像编辑_2112068355019599874.json, 图片生成/图生图/（9图）flux3_klein_image_edit图像编辑_2111089818842255361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_90

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Costume Changes and Face Swaps Flux3_klein 图像编辑_2113428085260513281.json、图片生成/图生图/Flux3 图片强化_2114538601471111169.json、图片生成/图生图/Flux3-Klein-图像编辑_2111109110757412866.json、图片生成/图生图/Moss-image-局部重绘_2112544404337676289.json、图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 9/10 个有
- `CLIPTextEncode` —— 7/10 个有
- `ReferenceMultiLatent` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `InpaintModelConditioning` —— 4/10 个有
- `Mask Fill Holes` —— 4/10 个有
- `TextGenerate` —— 4/10 个有
- `TextEncodeQwenImage21` —— 3/10 个有
- `Int` —— 2/10 个有
- `JjkText` —— 2/10 个有
- `ConditioningZeroOut` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 16 - 50 | 10 | 66% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 3.5 | 10 | 45% |
| 采样算法 | euler | - | 10 | 60% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 16 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 euler，10 个样本，一致性 60%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
