---
name: unknown_workflow_sampler_unet_vae_92
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.858
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text Concatenate, easy boolean, easy float, CR Prompt Text]
members: [图片生成/图生图/2102180346572922881.json, 图片生成/图生图/2102282925260759042.json, 图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json, 图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json, 图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json, 图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json, 图片生成/文生图/Qwen_image_2_1_多图编辑_2101885250807877634.json, 图片生成/文生图/qwen image  edit 2.1_2101931566393024514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_92

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/2102180346572922881.json、图片生成/图生图/2102282925260759042.json、图片生成/文生图/BF16小字不崩-Qwen image 2.1图片编辑_2102769559072763906.json、图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json、图片生成/文生图/QWEN-IMAGE-2.1_2104540875895431170.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `QwenImage21Cache` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `SaveImageAdvanced` —— 6/8 个有
- `CR Prompt Text` —— 4/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `easy boolean` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 42.5 | 25 - 50 | 8 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1080 | 8 | 98% |
| 高度 | 1024 | 1024 - 1624 | 8 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 42.5，观测区间 25 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1080，8 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1624，8 个样本，取值集中（一致性 82%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、easy boolean、easy float、CR Prompt Text
