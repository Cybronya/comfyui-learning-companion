---
name: text_to_image_sampler_clip_unet_138
type: Text To Image
frequency: 3
level: moderate
coverage: 0.976333
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/anima_2085025424341561345.json, 图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2091791668021387265.json, 图片生成/文生图/红衣女子生成_2015933896071847938.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_138

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/anima_2085025424341561345.json、图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2091791668021387265.json、图片生成/文生图/红衣女子生成_2015933896071847938.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `KOOK_ImageCompression` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 512 - 1024 | 3 | 73% |
| 高度 | 1024 | 512 - 1200 | 3 | 68% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 5 | 4 - 8 | 3 | 70% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1200，3 个样本
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 8，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
