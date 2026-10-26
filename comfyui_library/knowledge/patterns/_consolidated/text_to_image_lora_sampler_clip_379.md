---
name: text_to_image_lora_sampler_clip_379
type: Text To Image
frequency: 5
level: weak
coverage: 0.938
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2511-角色全身背面站立图_2082277163000229890.json, 图片生成/图生图/局部重绘+扩图_2013139159199784961.json, 图片生成/图生图/局部重绘加扩图二合一｜图生图画面修补扩展神器_2107005580991885313.json, 图片生成/图生图/局部重绘加扩图二合一｜图生图画面修补扩展神器_2110205787585990657.json, 图片生成/图生图/局部重绘加扩图工作流，图生图局部处理图像扩展工具_2107188537446715393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_379

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen 2511-角色全身背面站立图_2082277163000229890.json、图片生成/图生图/局部重绘+扩图_2013139159199784961.json、图片生成/图生图/局部重绘加扩图二合一｜图生图画面修补扩展神器_2107005580991885313.json、图片生成/图生图/局部重绘加扩图二合一｜图生图画面修补扩展神器_2110205787585990657.json、图片生成/图生图/局部重绘加扩图工作流，图生图局部处理图像扩展工具_2107188537446715393.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SavePSD` —— 4/5 个有
- `ImagePadForOutpaint` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `InpaintCropImproved` —— 4/5 个有
- `InpaintModelConditioning` —— 4/5 个有
- `InpaintStitchImproved` —— 4/5 个有
- `ModelPatchTorchSettings` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `solarL_SaveImagesToZip` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `LayerUtility: TextJoin` —— 1/5 个有
- `ResizeImageMaskNode` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 5 | 82% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 45% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 512 | 5 | 16% |
| 高度 | 80 | 80 - 512 | 5 | 16% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 高度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 高发问题（20/5 个样本）：Steps较低可能导致细节不足
