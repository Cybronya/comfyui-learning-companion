---
name: image_to_image_lora_sampler_unet_182
type: Image To Image
frequency: 3
level: weak
coverage: 0.876333
common_nodes: [CLIPLoader, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen创成式移除神器_1963957595465728001.json, 图片生成/图生图/【电商产品背景融合】qwen+edit万物溶图融合_1982599790670299137.json, 图片生成/图生图/老照片修复高级版Old_photos_Qwen-Image-Edit-2509_2005849021950423042.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen创成式移除神器_1963957595465728001.json、图片生成/图生图/【电商产品背景融合】qwen+edit万物溶图融合_1982599790670299137.json、图片生成/图生图/老照片修复高级版Old_photos_Qwen-Image-Edit-2509_2005849021950423042.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `Anything Everywhere3` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `Image Overlay` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
