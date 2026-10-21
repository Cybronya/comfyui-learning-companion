---
name: text_to_image_upscale_lora_sampler_35
type: Text To Image
frequency: 3
level: strong
coverage: 0.766667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoraLoader, SaveImage, Upscale Model Loader, VAEDecode]
problems: []
missing: [Upscale Model Loader]
members: [图片生成/文生图/1911978572158857217.json, 图片生成/文生图/1989245330363387906.json, 图片生成/文生图/SDXL文生图工作流高对比_2004022494623350786.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1911978572158857217.json、图片生成/文生图/1989245330363387906.json、图片生成/文生图/SDXL文生图工作流高对比_2004022494623350786.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `Upscale Model Loader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 2/3 个有
- `String` —— 2/3 个有
- `TextInputBasic` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 5 | 4 - 5 | 3 | 90% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 768 - 1344 | 3 | 77% |
| 高度 | 1024 | 1024 - 1728 | 3 | 74% |
| LoRA 模型强度 | 0.8 | 0.6 - 0.8 | 3 | 87% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 5，3 个样本，取值集中（一致性 90%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1344，3 个样本
- 高度 中位数 1024，观测区间 1024 - 1728，3 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 0.8，3 个样本，取值集中（一致性 87%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Upscale Model Loader
