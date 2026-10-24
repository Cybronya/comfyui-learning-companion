---
name: text_to_image_upscale_lora_sampler_49
type: Text To Image
frequency: 5
level: strong
coverage: 0.7492
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoraLoader, SaveImage, Upscale Model Loader, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SDXL_SZ_文生图工作流_2043647733185126402.json, 图片生成/文生图/SDXL文生图工作流_1911978572158857217.json, 图片生成/文生图/SDXL文生图工作流_1989245330363387906.json, 图片生成/文生图/SDXL文生图工作流_2053466430389137410.json, 图片生成/文生图/SDXL文生图工作流高对比_2004022494623350786.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/SDXL_SZ_文生图工作流_2043647733185126402.json、图片生成/文生图/SDXL文生图工作流_1911978572158857217.json、图片生成/文生图/SDXL文生图工作流_1989245330363387906.json、图片生成/文生图/SDXL文生图工作流_2053466430389137410.json、图片生成/文生图/SDXL文生图工作流高对比_2004022494623350786.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ShowText|pysssss` —— 4/5 个有
- `String` —— 4/5 个有
- `TextInputBasic` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.6 - 0.8 | 5 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 30 | 20 - 30 | 5 | 85% |
| Prompt 约束强度(CFG) | 5 | 4 - 5 | 5 | 92% |
| 采样算法 | dpmpp_2m | - | 5 | 80% |
| 调度器 | sgm_uniform | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 768 - 1344 | 5 | 76% |
| 高度 | 1024 | 1024 - 1728 | 5 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 0.8，5 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 20 - 30，5 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 5，5 个样本，取值集中（一致性 92%）
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 80%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1344，5 个样本
- 高度 中位数 1024，观测区间 1024 - 1728，5 个样本
