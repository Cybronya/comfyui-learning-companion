---
name: text_to_image_upscale_lora_sampler_63
type: Text To Image
frequency: 2
level: weak
coverage: 0.732
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageCASharpening+, ImageScaleBy, ImageScaleToTotalPixels, KSampler, KSamplerAdvanced, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, PhotoShakeNode, PreviewImage, PrimitiveFloat, ReferenceLatent, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMathDual+, TTResolutionSelector, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage超广角（清新多彩+MJ+肤若凝脂）双采+三采+双放大V3_2047969396240424962.json, 图片生成/文生图/▶▶Zimage双采+三采+双放大V7（带模型和lora下载链接）_2047478230738800641.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Zimage超广角（清新多彩+MJ+肤若凝脂）双采+三采+双放大V3_2047969396240424962.json、图片生成/文生图/▶▶Zimage双采+三采+双放大V7（带模型和lora下载链接）_2047478230738800641.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PhotoShakeNode`
- `PreviewImage`
- `PrimitiveFloat`
- `ReferenceLatent`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMathDual+`
- `TTResolutionSelector`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `INTConstant` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 12 | - | 2 | 100% |
| 采样算法 | 1.25 | - | 2 | 80% |
| 调度器 | res_multistep | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 928 | - | 2 | 100% |
| 高度 | 1664 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 调度器 最常用 res_multistep，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 928，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1664，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
