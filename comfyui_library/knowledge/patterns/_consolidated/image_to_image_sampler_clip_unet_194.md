---
name: image_to_image_sampler_clip_unet_194
type: Image To Image
frequency: 3
level: moderate
coverage: 0.808667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GrowMaskWithBlur, Image Comparer (rgthree), KSampler, LoadImage, MaskPreview+, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen千问-完美修手_1954054962278125570.json, 平台全量/Wan2.2 修手 自动版_1954187550112018434.json, 平台全量/修手-wan2.2低噪-手动版_2009196228432633858.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen千问-完美修手_1954054962278125570.json、平台全量/Wan2.2 修手 自动版_1954187550112018434.json、平台全量/修手-wan2.2低噪-手动版_2009196228432633858.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `ConstrainImage|pysssss` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | res_2s | - | 3 | 67% |
| 调度器 | bong_tangent | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 res_2s，3 个样本，一致性 67%
- 调度器 最常用 bong_tangent，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
