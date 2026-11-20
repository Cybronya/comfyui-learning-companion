---
name: image_to_image_lora_sampler_unet_229
type: Image To Image
frequency: 3
level: strong
coverage: 0.880667
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, ConvertRGBNode, Fast Groups Bypasser (rgthree), GetImageSize+, Image Blank, ImageConcanate, ImpactSwitch, Int, KSampler, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/穿搭大师Pro OOTD 姿势控制26年3月_2037192247174766593.json, 图片生成/图生图/👾怪獸-换装王-可指定姿势与背景👾_2089965166074093570.json, 平台全量/穿搭大师Pro OOTD 姿势控制（完全开源）_1994708121975201794.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_229

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/穿搭大师Pro OOTD 姿势控制26年3月_2037192247174766593.json、图片生成/图生图/👾怪獸-换装王-可指定姿势与背景👾_2089965166074093570.json、平台全量/穿搭大师Pro OOTD 姿势控制（完全开源）_1994708121975201794.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
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
- `AIO_Preprocessor` —— 2/3 个有
- `Compare` —— 2/3 个有
- `InversionDemoLazySwitch` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `MaxNode` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `Multi Text Merge` —— 2/3 个有
- `Resolution` —— 2/3 个有
- `TextEncodeQwenImageEditPlusAdv` —— 2/3 个有
- `easy promptConcat` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `Image Crop Face` —— 1/3 个有
- `KSampler (Efficient)` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
