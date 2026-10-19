---
name: text_to_image_lora_sampler_clip_219
type: Text To Image
frequency: 3
level: weak
coverage: 0.903333
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext一键去水印带前后对比｜图生图无痕修复，老照片旧图拯救_2107311794724364289.json, 图片生成/文生图/1942404910103080961.json, 图片生成/文生图/1942874687296704513.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_219

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/kontext一键去水印带前后对比｜图生图无痕修复，老照片旧图拯救_2107311794724364289.json、图片生成/文生图/1942404910103080961.json、图片生成/文生图/1942874687296704513.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 3 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | 80 - 1536 | 3 | 25% |
| 高度 | 768 | 80 - 1208 | 3 | 32% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，3 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 25%
- 高度 中位数 768，观测区间 80 - 1208，3 个样本，取值分散，一致性仅 32%
