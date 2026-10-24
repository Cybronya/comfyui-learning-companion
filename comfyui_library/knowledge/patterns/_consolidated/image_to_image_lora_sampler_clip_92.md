---
name: image_to_image_lora_sampler_clip_92
type: Image To Image
frequency: 3
level: moderate
coverage: 0.858
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein摄影风格复刻（高清修复+风格转换）_1999788800622686210.json, 图片生成/图生图/Klein高清溶图（参考图片先Flux生成再替换）_2015404957125582849.json, 图片生成/图生图/Kontext去水印史上最强去除水印——水印移除_Flux2-Klein_james001###_2085022409823965185.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Klein摄影风格复刻（高清修复+风格转换）_1999788800622686210.json、图片生成/图生图/Klein高清溶图（参考图片先Flux生成再替换）_2015404957125582849.json、图片生成/图生图/Kontext去水印史上最强去除水印——水印移除_Flux2-Klein_james001###_2085022409823965185.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `EmptyFlux2LatentImage` —— 2/3 个有
- `Flux2Scheduler` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `LatentUpscaleBy` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `RunningHub Deepcleaner` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text` —— 1/3 个有
- `TextCombinerTwo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 3 | 42% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | beta57 | - | 3 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，3 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 beta57，3 个样本，一致性 67%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
