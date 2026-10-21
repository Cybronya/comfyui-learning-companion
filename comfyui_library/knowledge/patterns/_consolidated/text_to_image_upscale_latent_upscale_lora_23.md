---
name: text_to_image_upscale_latent_upscale_lora_23
type: Text To Image
frequency: 2
level: weak
coverage: 0.844
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, ImageSmartSharpen+, JoinImageWithAlpha, KSampler, KSamplerAdvanced, LatentUpscaleBy, LoadImage, PixaromaLoraLoader, PrimitiveFloat, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, ShowText|pysssss, SimpleMathDual+, SplitImageWithAlpha, StringFunction|pysssss, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2高精度双采+放大_2100486595328696322.json, 图片生成/文生图/krea2高精度双采加放大｜文生图反推提示词出图_2100844617087410177.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/krea2高精度双采+放大_2100486595328696322.json、图片生成/文生图/krea2高精度双采加放大｜文生图反推提示词出图_2100844617087410177.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `ImageSmartSharpen+`
- `JoinImageWithAlpha`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoadImage`
- `PixaromaLoraLoader`
- `PrimitiveFloat`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `ShowText|pysssss`
- `SimpleMathDual+`
- `SplitImageWithAlpha`
- `StringFunction|pysssss`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 6.25 | - | 2 | 72% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |
| 宽度 | 552 | - | 2 | 14% |
| 高度 | 552 | - | 2 | 14% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 6.25，样本不足，未给区间，2 个样本
- 调度器 最常用 euler，2 个样本，一致性 50%
- 宽度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
