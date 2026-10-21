---
name: text_to_image_upscale_latent_upscale_lora_20
type: Text To Image
frequency: 2
level: weak
coverage: 0.763
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ColorMatchV2, ConditioningZeroOut, EmptyLatentImage, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), KSampler, KSamplerAdvanced, LatentUpscaleBy, LayerFilter: GaussianBlur, LazySwitch2way, LoaderGGUF, LoraLoaderModelOnly, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, ResolutionStdSelector, SaveImage, Seed (rgthree), SimpleMathDual+, TTResolutionSelector, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageSizeByLongerSide, 孤海注释, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-w高清生图整合流 双放大方案画质优化_2104362550707187713.json, 图片生成/文生图/黑鹤 Krea2-w高清生图优化流(整合)_2077069059501420545.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2-w高清生图整合流 双放大方案画质优化_2104362550707187713.json、图片生成/文生图/黑鹤 Krea2-w高清生图优化流(整合)_2077069059501420545.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatchV2`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LayerFilter: GaussianBlur`
- `LazySwitch2way`
- `LoaderGGUF`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ResolutionStdSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMathDual+`
- `TTResolutionSelector`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageSizeByLongerSide`
- `孤海注释`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 7.25 | - | 2 | 62% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |
| 宽度 | 400 | - | 2 | 20% |
| 高度 | 680 | - | 2 | 12% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 7.25，样本不足，未给区间，2 个样本
- 调度器 最常用 beta，2 个样本，一致性 50%
- 宽度 中位数 400，样本不足，未给区间，2 个样本，取值分散，一致性仅 20%
- 高度 中位数 680，样本不足，未给区间，2 个样本，取值分散，一致性仅 12%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
