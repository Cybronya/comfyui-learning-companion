---
name: text_to_image_lora_sampler_clip_257
type: Text To Image
frequency: 4
level: weak
coverage: 0.8935
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext一键去水印带前后对比｜图生图无痕修复，老照片旧图拯救_2107311794724364289.json, 图片生成/文生图/1942404910103080961.json, 图片生成/文生图/1942874687296704513.json, 图片生成/文生图/Kontext一键去水印前后对比工作流，文生图图生图去水印处理工具_2107559098299535361.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_257

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/kontext一键去水印带前后对比｜图生图无痕修复，老照片旧图拯救_2107311794724364289.json、图片生成/文生图/1942404910103080961.json、图片生成/文生图/1942874687296704513.json、图片生成/文生图/Kontext一键去水印前后对比工作流，文生图图生图去水印处理工具_2107559098299535361.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `ImageStitch` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 25 | 4 | 29% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 424 | 80 - 1536 | 4 | 2% |
| 高度 | 424 | 80 - 1208 | 4 | 10% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 25，4 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 424，观测区间 80 - 1536，4 个样本，取值分散，一致性仅 2%
- 高度 中位数 424，观测区间 80 - 1208，4 个样本，取值分散，一致性仅 10%
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
