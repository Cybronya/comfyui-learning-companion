---
name: image_to_image_lora_sampler_unet_120
type: Image To Image
frequency: 5
level: weak
coverage: 0.8818
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3d高斯泼溅可视化角度编辑 2511版_2014919803319885825.json, 图片生成/图生图/AA--图片编辑-Qwen- Edit-2511-单图_多图编辑+seedVR2超清放大_2006715586788724738.json, 图片生成/图生图/AA--完美换脸（换表情）BFS-lora -QwenEdit 2511+4K放大修复_2022650266755014657.json, 图片生成/图生图/AA--超强一致性！小红书FireRed-Image-edit1.1图像编辑+超清放大修复_2029824095113711618.json, 图片生成/图生图/【CQ808】Qwen-Image-Edit 2511 高斯泼溅3D摄像机移动_2046418764924723202.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_120

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/3d高斯泼溅可视化角度编辑 2511版_2014919803319885825.json、图片生成/图生图/AA--图片编辑-Qwen- Edit-2511-单图_多图编辑+seedVR2超清放大_2006715586788724738.json、图片生成/图生图/AA--完美换脸（换表情）BFS-lora -QwenEdit 2511+4K放大修复_2022650266755014657.json、图片生成/图生图/AA--超强一致性！小红书FireRed-Image-edit1.1图像编辑+超清放大修复_2029824095113711618.json、图片生成/图生图/【CQ808】Qwen-Image-Edit 2511 高斯泼溅3D摄像机移动_2046418764924723202.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `INTConstant` —— 3/5 个有
- `SeedVR2LoadDiTModel` —— 3/5 个有
- `SeedVR2LoadVAEModel` —— 3/5 个有
- `SeedVR2VideoUpscaler` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `FluxKontextImageScale` —— 2/5 个有
- `LoadSharpModel` —— 2/5 个有
- `SharpPredict` —— 2/5 个有
- `YCGaussianPreview` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `QwenImageIntegratedKSampler` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 6.51435e+14 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 6.51435e+14，5 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 6.51435e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
