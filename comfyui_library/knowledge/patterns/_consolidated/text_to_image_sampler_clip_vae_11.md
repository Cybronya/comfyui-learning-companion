---
name: text_to_image_sampler_clip_vae_11
type: Text To Image
frequency: 11
level: strong
coverage: 0.946636
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json, 图片生成/文生图/FLUX GGUF Q4_1961449815852957697.json, 图片生成/文生图/FLUX文生图+2_LoRA_1912954209854259202.json, 图片生成/文生图/FLUX文生图+LoRA_1912954176630943746.json, 图片生成/文生图/FLUX文生图_1922920426165473282.json, 图片生成/文生图/Flux1.1pro-精炼人像lora_1910491843820253185.json, 图片生成/文生图/Flux人像写真最终版_1910503564932804610.json, 图片生成/文生图/flux 文生图3倍加速 基础款_1934106744388018178.json, 图片生成/文生图/flux-8_1930451421953691649.json, 图片生成/文生图/flux文生图-8步生图_1976848182871314434.json, 图片生成/文生图/z-image文生图_2094325413752426498.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_11

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json、图片生成/文生图/FLUX GGUF Q4_1961449815852957697.json、图片生成/文生图/FLUX文生图+2_LoRA_1912954209854259202.json、图片生成/文生图/FLUX文生图+LoRA_1912954176630943746.json、图片生成/文生图/FLUX文生图_1922920426165473282.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 10/11 个有
- `FluxGuidance` —— 10/11 个有
- `UNETLoader` —— 9/11 个有
- `LoraLoaderModelOnly` —— 6/11 个有
- `PreviewImage` —— 6/11 个有
- `TeaCache` —— 4/11 个有
- `LoraLoader` —— 2/11 个有
- `UnetLoaderGGUF` —— 2/11 个有
- `CLIPLoader` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 35 | 11 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 11 | 97% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 768 | 720 - 1080 | 11 | 88% |
| 高度 | 1200 | 1024 - 1960 | 11 | 78% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 35，11 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，11 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 720 - 1080，11 个样本，取值集中（一致性 88%）
- 高度 中位数 1200，观测区间 1024 - 1960，11 个样本
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
