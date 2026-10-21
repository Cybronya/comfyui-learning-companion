---
name: image_to_image_sampler_clip_unet_14
type: Image To Image
frequency: 3
level: weak
coverage: 0.890667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2精修图片，自己用_2008078649689378817.json, 图片生成/文生图/Z image base文生图_图生图_2016418881513984002.json, 图片生成/文生图/瞬间成画：Z-Image-Turbo，8步生成的视觉革命_1994355773188739074.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Wan2.2精修图片，自己用_2008078649689378817.json、图片生成/文生图/Z image base文生图_图生图_2016418881513984002.json、图片生成/文生图/瞬间成画：Z-Image-Turbo，8步生成的视觉革命_1994355773188739074.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.7 | - | 1 | 100% |
| LoRA 文本强度 | 0.7 | - | 1 | 100% |
| 采样步数 | 10 | 10 - 40 | 3 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.8 | 0.3 - 1 | 3 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 40，3 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.8，观测区间 0.3 - 1，3 个样本
