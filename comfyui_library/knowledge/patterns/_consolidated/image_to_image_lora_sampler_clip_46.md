---
name: image_to_image_lora_sampler_clip_46
type: Image To Image
frequency: 8
level: moderate
coverage: 0.918625
common_nodes: [CLIPTextEncode, GrowMaskWithBlur, KSampler, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, PreviewImage, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Krea 局部重绘_1884922306718846978.json, 平台全量/Wan2.2 局部重绘  八步快速重绘_2008406041188376578.json, 平台全量/Wan2.2 局部重绘_1954192513697497090.json, 平台全量/千问-局部重绘_Qwen-Image-Instantx-ControlNet-Inpainting_1944919482163978242.json, 平台全量/手部修复 完美修手 修手 wan2.2 万相低噪模型修复_2001192188497326081.json, 平台全量/绝美古风 _ 局部修复_1904739925982646273.json, 平台全量/超级完美 _ 修手_1890355890833510401.json, 平台全量/超级完美 _ 修脸_1875800402527477762.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Krea 局部重绘_1884922306718846978.json、平台全量/Wan2.2 局部重绘  八步快速重绘_2008406041188376578.json、平台全量/Wan2.2 局部重绘_1954192513697497090.json、平台全量/千问-局部重绘_Qwen-Image-Instantx-ControlNet-Inpainting_1944919482163978242.json、平台全量/手部修复 完美修手 修手 wan2.2 万相低噪模型修复_2001192188497326081.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `GrowMaskWithBlur`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `ConditioningZeroOut` —— 7/8 个有
- `ImpactInt` —— 7/8 个有
- `SetLatentNoiseMask` —— 7/8 个有
- `ModelSamplingSD3` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `JjkText` —— 4/8 个有
- `easy float` —— 4/8 个有
- `DualCLIPLoader` —— 3/8 个有
- `FluxGuidance` —— 3/8 个有
- `DifferentialDiffusion` —— 2/8 个有
- `InpaintModelConditioning` —— 2/8 个有
- `ControlNetInpaintingAliMamaApply` —— 1/8 个有
- `ControlNetLoader` —— 1/8 个有
- `Int` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `RH_Translator` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 8 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 0.44 | 0.35 - 1 | 8 | 54% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 0.44，观测区间 0.35 - 1，8 个样本
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
