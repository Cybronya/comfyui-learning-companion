---
name: text_to_image_sampler_clip_vae_4
type: Text To Image
frequency: 21
level: moderate
coverage: 0.946429
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ComfyUI system workflow_2072886879170686978.json, 图片生成/文生图/ComfyUI-文生图例子_1934059209472266242.json, 图片生成/文生图/ComfyUI基础文生图工作流_2083027862839447554.json, 图片生成/文生图/ComfyUI基础文生图工作流_2087084704964112385.json, 图片生成/文生图/ComfyUI官方介绍中的多LoRa模型使用工作流_1934958655928508418.json, 图片生成/文生图/ComfyUI官方示例1：文生图工作流详解 _ ComfyUI从入门到精通_1930949787460239362.json, 图片生成/文生图/ComfyUI极简入门教程#1_1961283334359990274.json, 图片生成/文生图/FLUX文生图+Checkpoint_1914963069880205314.json, 图片生成/文生图/FLUX文生图+LoRA_1912954176630943746.json, 图片生成/文生图/FLUX文生图_1922920426165473282.json, 图片生成/文生图/Flux1.1pro-精炼人像lora_1910491843820253185.json, 图片生成/文生图/Flux人像写真最终版_1910503564932804610.json, 图片生成/文生图/RealRose LoRA生图工作流_1919938265468567553.json, 图片生成/文生图/flux 文生图3倍加速 基础款_1934106744388018178.json, 图片生成/文生图/flux-8_1930451421953691649.json, 图片生成/文生图/flux文生图-8步生图_1976848182871314434.json, 图片生成/文生图/好玩的 文生图工作流_2098346126574444545.json, 图片生成/文生图/文生图kontext_1950688204880039937.json, 图片生成/文生图/模特选妃 2.0_1921302462970658818.json, 图片生成/文生图/简约风格婚礼留影区设计V1_1904463583671980033.json, 平台全量/蔚迦思重绘工作流_1935870014476251138.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_4

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/ComfyUI system workflow_2072886879170686978.json、图片生成/文生图/ComfyUI-文生图例子_1934059209472266242.json、图片生成/文生图/ComfyUI基础文生图工作流_2083027862839447554.json、图片生成/文生图/ComfyUI基础文生图工作流_2087084704964112385.json、图片生成/文生图/ComfyUI官方介绍中的多LoRa模型使用工作流_1934958655928508418.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 14/21 个有
- `DualCLIPLoader` —— 12/21 个有
- `UNETLoader` —— 12/21 个有
- `FluxGuidance` —— 11/21 个有
- `CheckpointLoaderSimple` —— 10/21 个有
- `LoraLoaderModelOnly` —— 9/21 个有
- `PreviewImage` —— 6/21 个有
- `LoraLoader` —— 4/21 个有
- `TeaCache` —— 4/21 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/21 个有
- `easy cleanGpuUsed` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 21 | 77% |
| 高度 | 1024 | 512 - 1536 | 21 | 68% |
| 采样步数 | 20 | 8 - 30 | 21 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 21 | 9% |
| 采样算法 | euler | - | 21 | 90% |
| 调度器 | simple | - | 21 | 52% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| LoRA 模型强度 | 0.95 | 0.8 - 1 | 4 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，21 个样本
- 高度 中位数 1024，观测区间 512 - 1536，21 个样本
- 采样步数 中位数 20，观测区间 8 - 30，21 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，21 个样本，取值分散，一致性仅 9%
- 采样算法 最常用 euler，21 个样本，一致性 90%
- 调度器 最常用 simple，21 个样本，一致性 52%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.95，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
