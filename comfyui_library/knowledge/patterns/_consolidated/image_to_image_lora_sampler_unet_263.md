---
name: image_to_image_lora_sampler_unet_263
type: Image To Image
frequency: 2
level: weak
coverage: 0.8755
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, Seed (rgthree), SimpleMath+, SimpleMathCondition+, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy getNode, easy setNode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/光照效果&镜头角度+编辑+qwen_edit_2509_2074078701213536257.json, 平台全量/人物姿势迁移+V1.0+Qwen_Imgae_Edit_2509+_2074059518778101761.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_263

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/光照效果&镜头角度+编辑+qwen_edit_2509_2074078701213536257.json、平台全量/人物姿势迁移+V1.0+Qwen_Imgae_Edit_2509+_2074059518778101761.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMath+`
- `SimpleMathCondition+`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Get resolution [Crystools]` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImpactCompare` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWStringConcat` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `QwenEditConfigPreparer` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy textIndexSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
