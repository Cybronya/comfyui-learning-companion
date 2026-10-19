---
name: image_to_image_sampler_vae_2
type: Image To Image
frequency: 3
level: weak
coverage: 0.849667
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1988835436825022465.json, 视频生成/图生视频/1988836664481026049.json, 视频生成/文生视频/Nunchaku-Qwen Editor_2072999582260568064.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1988835436825022465.json、视频生成/图生视频/1988836664481026049.json、视频生成/文生视频/Nunchaku-Qwen Editor_2072999582260568064.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `NunchakuQwenImageLoraLoader` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `StringConcatenate` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 3 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，3 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
