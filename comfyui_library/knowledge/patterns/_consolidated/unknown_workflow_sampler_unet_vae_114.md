---
name: unknown_workflow_sampler_unet_vae_114
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.803571
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json, 图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2101968376938717186.json, 图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json, 图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json, 图片生成/文生图/qwen-image2.1-文生图_2105500926474801154.json, 图片生成/文生图/文生图_qwenimage2.1_2101826399211446273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_114

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json、图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json、图片生成/文生图/image_qwen_image_2_1_t2i_2101968376938717186.json、图片生成/文生图/qwen-image2.1-文生图_2101865085642825729.json、图片生成/文生图/qwen-image2.1-文生图_2105123427295252481.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImageAdvanced` —— 6/7 个有
- `PreviewAny` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `TextGenerateLTX2Prompt` —— 5/7 个有
- `QwenImage21Cache` —— 1/7 个有
- `TextGenerate` —— 1/7 个有
- `easy showAnything` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 40 | 25 - 50 | 7 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
