---
name: text_to_image_sampler_clip_unet_31
type: Text To Image
frequency: 11
level: moderate
coverage: 0.885091
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy positive]
members: [图片生成/文生图/1980482521886576641.json, 图片生成/文生图/1980484330449453058.json, 图片生成/文生图/1984195134919163905.json, 图片生成/文生图/1984209491019317249.json, 图片生成/文生图/1984613779646398466.json, 图片生成/文生图/1985297339466326018.json, 图片生成/文生图/1989259967058374657.json, 图片生成/文生图/FLUX文生图+三种图片高清放大组_2075176156214677505.json, 图片生成/文生图/Flux文生图+三种图片高清放大（Supir放大+图像通过模型放大+Latent放大）_2002988961075195905.json, 图片生成/文生图/工作流基础篇-8-FLUX文生图+三种图片高清放大组_2016402394782900226.json, 图片生成/文生图/文生图后可选3种放大变清晰_2106549757798871041.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1980482521886576641.json、图片生成/文生图/1980484330449453058.json、图片生成/文生图/1984195134919163905.json、图片生成/文生图/1984209491019317249.json、图片生成/文生图/1984613779646398466.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Text_Box` —— 10/11 个有
- `Image Comparer (rgthree)` —— 9/11 个有
- `FluxLoraLoader` —— 8/11 个有
- `ImageScaleBy` —— 6/11 个有
- `ImageUpscaleWithModel` —— 6/11 个有
- `LatentUpscaleBy` —— 6/11 个有
- `SUPIR_Upscale` —— 6/11 个有
- `UpscaleModelLoader` —— 6/11 个有
- `VAEEncode` —— 6/11 个有
- `LoraLoader` —— 3/11 个有
- `easy positive` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 11 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 11 | 0% |
| 采样算法 | dpmpp_2m | - | 11 | 91% |
| 调度器 | sgm_uniform | - | 11 | 91% |
| 重绘幅度 | 1 | 0.5 - 1 | 11 | 71% |
| 宽度 | 768 | 768 - 1024 | 11 | 88% |
| 高度 | 1024 | 1024 - 1536 | 11 | 86% |
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 3 | 80% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，11 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m，11 个样本，一致性 91%
- 调度器 最常用 sgm_uniform，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，11 个样本
- 宽度 中位数 768，观测区间 768 - 1024，11 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1536，11 个样本，取值集中（一致性 86%）
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy positive
