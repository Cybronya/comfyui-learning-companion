---
name: image_to_image_sampler_vae_29
type: Image To Image
frequency: 3
level: weak
coverage: 0.913667
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, TextEncodeQwenImageEdit, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/nunchaku-qwen-image-edit-单图_1966064311875571713.json, 图片生成/图生图/nunchaku-qwen-image-edit-双图_1966064348844167170.json, 图片生成/图生图/nunchaku加速千问图像编辑-qwen-image-edit_1967197942203473922.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/nunchaku-qwen-image-edit-单图_1966064311875571713.json、图片生成/图生图/nunchaku-qwen-image-edit-双图_1966064348844167170.json、图片生成/图生图/nunchaku加速千问图像编辑-qwen-image-edit_1967197942203473922.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `AILab_ImageCompare` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `Preview from image [Crystools]` —— 1/3 个有
- `RBGImageStitchPlus` —— 1/3 个有
- `RMBG` —— 1/3 个有

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
