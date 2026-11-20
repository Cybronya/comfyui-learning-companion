---
name: text_to_image_sampler_clip_checkpoint_4
type: Text To Image
frequency: 19
level: moderate
coverage: 0.919263
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ComfyUI system workflow_2072886879170686978.json, 图片生成/文生图/ComfyUI-文生图例子_1934059209472266242.json, 图片生成/文生图/ComfyUI基础文生图工作流_2083027862839447554.json, 图片生成/文生图/ComfyUI基础文生图工作流_2087084704964112385.json, 图片生成/文生图/ComfyUI官方介绍中的多LoRa模型使用工作流_1934958655928508418.json, 图片生成/文生图/ComfyUI官方示例1：文生图工作流详解 _ ComfyUI从入门到精通_1930949787460239362.json, 图片生成/文生图/ComfyUI极简入门教程#1_1961283334359990274.json, 图片生成/文生图/FLUX文生图+Checkpoint_1914963069880205314.json, 图片生成/文生图/FluxDev文生图工作流_1969281537156018177.json, 图片生成/文生图/RealRose LoRA生图工作流_1919938265468567553.json, 图片生成/文生图/SDXL 双阶段高清精修工作流_2083092060114079745.json, 图片生成/文生图/Text-to-Image + LoRA_1878782083018514433.json, 图片生成/文生图/mechaNeko_style打磨_1931623761387433985.json, 图片生成/文生图/【AI小王子】20.LCM lora八步生成_2046843881974665218.json, 图片生成/文生图/【遇见AI】基础放大方法之潜空间放大_2011365312960139265.json, 图片生成/文生图/小易第一课 工作流搭建【20260527】_2060680098830962690.json, 图片生成/文生图/文生图SD-XL基础工作流_2029187667841257473.json, 图片生成/文生图/文生图_2046755529770405889.json, 图片生成/文生图/文生图基础款_1990029530519793666.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/ComfyUI system workflow_2072886879170686978.json、图片生成/文生图/ComfyUI-文生图例子_1934059209472266242.json、图片生成/文生图/ComfyUI基础文生图工作流_2083027862839447554.json、图片生成/文生图/ComfyUI基础文生图工作流_2087084704964112385.json、图片生成/文生图/ComfyUI官方介绍中的多LoRa模型使用工作流_1934958655928508418.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 12/19 个有
- `LoraLoader` —— 5/19 个有
- `LatentUpscale` —— 4/19 个有
- `FluxGuidance` —— 2/19 个有
- `VAELoader` —— 2/19 个有
- `LatentUpscaleBy` —— 1/19 个有
- `Lora Loader` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 512 - 1024 | 19 | 71% |
| 高度 | 1024 | 512 - 1280 | 19 | 66% |
| 采样步数 | 20 | 8 - 35 | 19 | 72% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 19 | 60% |
| 采样算法 | euler | - | 19 | 63% |
| 调度器 | normal | - | 19 | 47% |
| 重绘幅度 | 1 | 0.35 - 1 | 19 | 77% |
| LoRA 模型强度 | 0.8 | 0.4 - 1 | 5 | 74% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 5 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 800，观测区间 512 - 1024，19 个样本
- 高度 中位数 1024，观测区间 512 - 1280，19 个样本
- 采样步数 中位数 20，观测区间 8 - 35，19 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，19 个样本
- 采样算法 最常用 euler，19 个样本，一致性 63%
- 调度器 最常用 normal，19 个样本，一致性 47%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，19 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.4 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
