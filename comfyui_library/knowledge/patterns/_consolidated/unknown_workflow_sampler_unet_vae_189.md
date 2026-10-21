---
name: unknown_workflow_sampler_unet_vae_189
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.731333
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImage, SaveImageAdvanced, SeedNode, StringConcatenate, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json, 图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json, 图片生成/文生图/qwen_image_2_1_TI2I 二合一工作流（带提示词增强）_2102589892604813314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_189

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-image2.1-文生图+提示词增强_2103929675339886594.json、图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json、图片生成/文生图/qwen_image_2_1_TI2I 二合一工作流（带提示词增强）_2102589892604813314.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SaveImageAdvanced`
- `SeedNode`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `QwenImage21Cache` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `JsonExtractString` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `Textbox` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 3 | 97% |
| 高度 | 1536 | 1536 - 1920 | 3 | 89% |
| 采样步数 | 25 | 8 - 35 | 3 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，3 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1536 - 1920，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 25，观测区间 8 - 35，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
