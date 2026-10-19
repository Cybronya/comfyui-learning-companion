---
name: text_to_image_upscale_lora_sampler_27
type: Text To Image
frequency: 2
level: weak
coverage: 0.6835
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoraLoader, SaveImage, ShowText|pysssss, String, TextInputBasic, Upscale Model Loader, VAEDecode]
problems: []
missing: [Upscale Model Loader]
members: [图片生成/文生图/1911978572158857217.json, 图片生成/文生图/1989245330363387906.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1911978572158857217.json、图片生成/文生图/1989245330363387906.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `ShowText|pysssss`
- `String`
- `TextInputBasic`
- `Upscale Model Loader`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Upscale Model Loader
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
