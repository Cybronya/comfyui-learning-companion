---
name: image_to_image_sampler_unet_vae_14
type: Image To Image
frequency: 11
level: moderate
coverage: 0.880818
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen image edit-动漫转真人_1977415066834358274.json, 图片生成/图生图/qwen-edit-衣服提取_1965096403301224450.json, 图片生成/图生图/qwen-image-edit 千问图像编辑_1959582504913154050.json, 图片生成/图生图/qwen-image-edit-lora4步-加文字和纹身+换背景-媲美-全能图片V1_1963412197550567426.json, 图片生成/图生图/qwen-image-edit-lora4步-手办媲美-全能图片V1_1963410711668043778.json, 图片生成/图生图/qwen_edit图生图手办_1970682029845213186.json, 图片生成/图生图/一键提取服装-电商服装精准提取工作流_2053701024937984002.json, 图片生成/图生图/从模特身上提取衣服_1979103601475883009.json, 图片生成/图生图/小红书8步加速换装FireRed-Image-edit1.1_2030823318718259202.json, 图片生成/图生图/电商服装精准提取_2051582242283114498.json, 图片生成/图生图/老照片高保真修复_2060622665689427970.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/qwen image edit-动漫转真人_1977415066834358274.json、图片生成/图生图/qwen-edit-衣服提取_1965096403301224450.json、图片生成/图生图/qwen-image-edit 千问图像编辑_1959582504913154050.json、图片生成/图生图/qwen-image-edit-lora4步-加文字和纹身+换背景-媲美-全能图片V1_1963412197550567426.json、图片生成/图生图/qwen-image-edit-lora4步-手办媲美-全能图片V1_1963410711668043778.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `ModelSamplingAuraFlow` —— 10/11 个有
- `TextEncodeQwenImageEdit` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 6/11 个有
- `Anything Everywhere` —— 5/11 个有
- `FluxKontextImageScale` —— 5/11 个有
- `CLIPTextEncode` —— 4/11 个有
- `Image Comparer (rgthree)` —— 4/11 个有
- `TextEncodeQwenImageEditPlus` —— 4/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `Anything Everywhere3` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `ImagePadKJ` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 11 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 56% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，11 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（6/11 个样本）：Steps较低可能导致细节不足
