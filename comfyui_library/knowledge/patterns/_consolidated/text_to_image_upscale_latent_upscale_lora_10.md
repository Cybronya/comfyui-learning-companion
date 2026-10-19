---
name: text_to_image_upscale_latent_upscale_lora_10
type: Text To Image
frequency: 3
level: strong
coverage: 0.846
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, DF_Text_Box, DualCLIPLoader, EmptyLatentImage, FluxLoraLoader, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSampler, LatentUpscaleBy, SUPIR_Upscale, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1985297339466326018.json, 图片生成/文生图/1989259967058374657.json, 图片生成/文生图/文生图后可选3种放大变清晰_2106549757798871041.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1985297339466326018.json、图片生成/文生图/1989259967058374657.json、图片生成/文生图/文生图后可选3种放大变清晰_2106549757798871041.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DF_Text_Box`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxLoraLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentUpscaleBy`
- `SUPIR_Upscale`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 3 | 86% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
