---
name: image_to_image_lora_sampler_unet_237
type: Image To Image
frequency: 3
level: strong
coverage: 0.915333
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, GetImageSize, Image Blank, ImageCompositeMasked, JoinImageWithAlpha, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/Qwen2511_单图无限扩图_2010198231388524545.json, 平台全量/qwen edit 2511 换脸换装  风格转绘 升级版 真实无痕换脸 万物迁移_2014168549014642690.json, 平台全量/qwen-edit-2511-换脸(升级版)_2005804727491325953.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_237

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen2511_单图无限扩图_2010198231388524545.json、平台全量/qwen edit 2511 换脸换装  风格转绘 升级版 真实无痕换脸 万物迁移_2014168549014642690.json、平台全量/qwen-edit-2511-换脸(升级版)_2005804727491325953.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropFace` —— 2/3 个有
- `Mask Fill Holes` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `ImageScaleToMaxDimension` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `easy getNode` —— 1/3 个有
- `easy setNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
