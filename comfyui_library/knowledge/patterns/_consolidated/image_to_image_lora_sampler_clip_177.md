---
name: image_to_image_lora_sampler_clip_177
type: Image To Image
frequency: 2
level: weak
coverage: 0.8545
common_nodes: [CLIPLoader, CLIPTextEncode, Checkpoint Loader (Simple), ConditioningZeroOut, GetImageSize, HAIGC_LoadImagesFromZip, Image Comparer (rgthree), ImageFromBatch, ImageListToBatch+, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/106：动漫转真人_2049523612280950785.json, 数字人/数字人/666：动漫转真人_2049121146951442434.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_177

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/106：动漫转真人_2049523612280950785.json、数字人/数字人/666：动漫转真人_2049121146951442434.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Checkpoint Loader (Simple)`
- `ConditioningZeroOut`
- `GetImageSize`
- `HAIGC_LoadImagesFromZip`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageListToBatch+`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 0.44 | - | 2 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 0.44，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
