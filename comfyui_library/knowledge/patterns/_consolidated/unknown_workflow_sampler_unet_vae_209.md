---
name: unknown_workflow_sampler_unet_vae_209
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8692
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json, 图片生成/图生图/Qwen21_1底图5参考_带宽高_2112762005873582081.json, 图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json, 图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json, 图片生成/图生图/refMod 8视角视图生成_2111837385603510274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_209

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1角色多视图_2105648438640726018.json、图片生成/图生图/Qwen21_1底图5参考_带宽高_2112762005873582081.json、图片生成/图生图/image_qwen_image_2_1_character_sheet1_2108024739095728130.json、图片生成/图生图/image_qwen_image_2_1_character_sheet_with_clothes_2108035472189644801.json、图片生成/图生图/refMod 8视角视图生成_2111837385603510274.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `EmptyLatentImage` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `QwenImage21Cache` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `easy promptLine` —— 1/5 个有
- `easy setNode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 5 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
