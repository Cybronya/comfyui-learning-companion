---
name: unknown_workflow_sampler_unet_vae_174
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.890667
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图_2101861903931887617.json, 图片生成/文生图/Qwen Image 文生图_2102936313539416066.json, 图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json, 图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json, 图片生成/文生图/Qwen-Image-2.1 text -image_2108513111039893506.json, 图片生成/文生图/Qwen-Image-2.1 文生图标准版_2104450148830109698.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_174

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图_2101861903931887617.json、图片生成/文生图/Qwen Image 文生图_2102936313539416066.json、图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json、图片生成/文生图/Qwen image 2.1文生图_2103043092977905666.json、图片生成/文生图/Qwen-Image-2.1 text -image_2108513111039893506.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
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
- `QwenImage21Cache` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `CompressImages` —— 1/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 25 - 40 | 6 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 864 - 1024 | 6 | 94% |
| 高度 | 1024 | 1024 - 1536 | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 25 - 40，6 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 864 - 1024，6 个样本，取值集中（一致性 94%）
- 高度 中位数 1024，观测区间 1024 - 1536，6 个样本，取值集中（一致性 83%）
