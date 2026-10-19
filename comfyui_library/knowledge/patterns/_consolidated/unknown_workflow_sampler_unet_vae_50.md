---
name: unknown_workflow_sampler_unet_vae_50
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.834727
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json, 图片生成/文生图/Qwen Image 文生图_2102936313539416066.json, 图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json, 图片生成/文生图/Qwen image 2.1 文生图_2102236635739017218.json, 图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json, 图片生成/文生图/Qwen image 2.1文生图_2102591785762639873.json, 图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json, 图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json, 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105104996953059329.json, 图片生成/文生图/Qwen_image_2.1_文生图提示词增强_2105485714585636866.json, 图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_50

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json、图片生成/文生图/Qwen Image 文生图_2102936313539416066.json、图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json、图片生成/文生图/Qwen image 2.1 文生图_2102236635739017218.json、图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `SaveImageAdvanced` —— 6/11 个有
- `TextGenerateLTX2Prompt` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `PreviewAny` —— 1/11 个有
- `StringToInt` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `TextGenerate` —— 1/11 个有
- `忽略多组孤海` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 11 | 100% |
| 高度 | 1024 | 1024 - 1024 | 11 | 100% |
| 采样步数 | 40 | 25 - 50 | 11 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，11 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
