---
name: text_to_image_sampler_clip_unet_173
type: Text To Image
frequency: 4
level: moderate
coverage: 0.96675
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima_2085025424341561345.json, 图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2091791668021387265.json, 图片生成/文生图/红衣女子生成_2015933896071847938.json, 平台全量/文生图loRA外挂-双图对比_2117520610346754049.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_173

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/anima_2085025424341561345.json、图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2091791668021387265.json、图片生成/文生图/红衣女子生成_2015933896071847938.json、平台全量/文生图loRA外挂-双图对比_2117520610346754049.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `CLIPLoaderGGUF` —— 1/4 个有
- `KOOK_ImageCompression` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 912 | 512 - 1080 | 4 | 74% |
| 高度 | 1112 | 512 - 1920 | 4 | 57% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 27.5 | 20 - 49 | 4 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 4 | 44% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 912，观测区间 512 - 1080，4 个样本
- 高度 中位数 1112，观测区间 512 - 1920，4 个样本
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 27.5，观测区间 20 - 49，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
