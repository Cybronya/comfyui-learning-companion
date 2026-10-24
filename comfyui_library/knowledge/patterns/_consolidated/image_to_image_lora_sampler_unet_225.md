---
name: image_to_image_lora_sampler_unet_225
type: Image To Image
frequency: 2
level: weak
coverage: 0.89
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, ConvertRGBNode, Fast Groups Bypasser (rgthree), GetImageSize+, Image Blank, ImageConcanate, ImpactSwitch, Int, KSampler, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/穿搭大师Pro OOTD 姿势控制26年3月_2037192247174766593.json, 图片生成/图生图/👾怪獸-换装王-可指定姿势与背景👾_2089965166074093570.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_225

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/穿搭大师Pro OOTD 姿势控制26年3月_2037192247174766593.json、图片生成/图生图/👾怪獸-换装王-可指定姿势与背景👾_2089965166074093570.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ConvertRGBNode`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Blank`
- `ImageConcanate`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Compare` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `Image Crop Face` —— 1/2 个有
- `InversionDemoLazySwitch` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `KSampler (Efficient)` —— 1/2 个有
- `MaxNode` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `Multi Text Merge` —— 1/2 个有
- `Resolution` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `TextEncodeQwenImageEditPlusAdv` —— 1/2 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
