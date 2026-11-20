---
name: image_to_image_inpaint_lora_sampler_20
type: Image To Image
frequency: 2
level: weak
coverage: 0.576
common_nodes: [AnimaBoosterLoader, AnimaLLLiteApply, AnimaTeaCache, CLIPLoader, CLIPTextEncode, CR Text, Fast Groups Bypasser (rgthree), GetNode, GoogleTranslateTextNode, INTConstant, InpaintPreprocessor, KSampler, LayerUtility: ImageScaleByAspectRatio V2, Load Lora, LoadImage, Mask Fill Holes, Mask Gaussian Region, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, SetLatentNoiseMask, SetNode, Text Concatenate, VAEDecode, VAEEncode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/图生图/anima动漫图-局部重绘_2112342212968280066.json, 平台全量/anima动漫图-局部重绘_2076987946913329153.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/anima动漫图-局部重绘_2112342212968280066.json、平台全量/anima动漫图-局部重绘_2076987946913329153.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 2 个 workflow 都包含：
- `AnimaBoosterLoader`
- `AnimaLLLiteApply`
- `AnimaTeaCache`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GoogleTranslateTextNode`
- `INTConstant`
- `InpaintPreprocessor`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Load Lora`
- `LoadImage`
- `Mask Fill Holes`
- `Mask Gaussian Region`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetNode`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
