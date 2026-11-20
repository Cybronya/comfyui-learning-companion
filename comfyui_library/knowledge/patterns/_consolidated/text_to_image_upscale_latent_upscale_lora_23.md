---
name: text_to_image_upscale_latent_upscale_lora_23
type: Text To Image
frequency: 2
level: weak
coverage: 0.905
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Image Comparer (rgthree), KSampler, KSamplerAdvanced, LatentUpscaleBy, LoadImageOutput, LoraLoaderModelOnly, PrimitiveStringMultiline, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SkipLayerGuidanceDiTSimple, TextGenerate, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy showAnything, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/黑鹤001 MOSS-Image 文生图流整合移植RH版｜一键出图高清直出_2114161760012955650.json, 图片生成/文生图/黑鹤001 MOSS-Image-生图流（整合移植RH 版）_2114008445971161090.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/黑鹤001 MOSS-Image 文生图流整合移植RH版｜一键出图高清直出_2114161760012955650.json、图片生成/文生图/黑鹤001 MOSS-Image-生图流（整合移植RH 版）_2114008445971161090.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoadImageOutput`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SkipLayerGuidanceDiTSimple`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | - | 2 | 14% |
| 高度 | 552 | - | 2 | 14% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 14.75 | - | 2 | 31% |
| 采样算法 | 3 | - | 1 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- Prompt 约束强度(CFG) 中位数 14.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 31%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
