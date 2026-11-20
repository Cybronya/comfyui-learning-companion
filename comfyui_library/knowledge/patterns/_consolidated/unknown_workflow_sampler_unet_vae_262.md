---
name: unknown_workflow_sampler_unet_vae_262
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7088
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImageAdvanced, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json, 图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json, 图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json, 图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json, 图片生成/文生图/qwen_image_2_1_TI2I 二合一工作流（带提示词增强）_2102589892604813314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_262

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 文生图_2110596847675985921.json、图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json、图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json、图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json、图片生成/文生图/qwen_image_2_1_TI2I 二合一工作流（带提示词增强）_2102589892604813314.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `SeedNode` —— 3/5 个有
- `StringConcatenate` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `JjkText` —— 1/5 个有
- `JsonExtractString` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `SaveText` —— 1/5 个有
- `Textbox` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 5 | 98% |
| 高度 | 1536 | 1024 - 1920 | 5 | 76% |
| 采样步数 | 25 | 8 - 35 | 5 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1536，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 25，观测区间 8 - 35，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
