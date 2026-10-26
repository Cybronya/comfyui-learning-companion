---
name: unknown_workflow_sampler_unet_vae_274
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.920333
common_nodes: [CLIPLoader, CR Prompt Text, KSampler, LoadImage, PreviewImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json, 图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json, 图片生成/图生图/Qwen-image2.1 VS Flux3-klein_2111256094176800770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_274

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-image-2.1-单图编辑_2101839855062966274.json、图片生成/图生图/Qwen-image-2.1-多图编辑_2101845005257236482.json、图片生成/图生图/Qwen-image2.1 VS Flux3-klein_2111256094176800770.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `ReferenceMultiLatent` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 16 - 40 | 3 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 16 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
