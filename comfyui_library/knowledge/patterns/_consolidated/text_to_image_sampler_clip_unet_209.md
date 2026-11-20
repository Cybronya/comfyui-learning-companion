---
name: text_to_image_sampler_clip_unet_209
type: Text To Image
frequency: 2
level: weak
coverage: 0.767
common_nodes: [CLIPTextEncode, CR Text Concatenate, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LayerUtility: ImageTaggerSave, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, Load Image Batch, LoadImage, RH_Translator, SaveImage, String, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/图片（批量）打标-JoyCaption（5月最新版）_1928496136284413953.json, 图片生成/图生图/图片（批量）打标-JoyCaption 3_1961797492553748482.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_209

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/图片（批量）打标-JoyCaption（5月最新版）_1928496136284413953.json、图片生成/图生图/图片（批量）打标-JoyCaption 3_1961797492553748482.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageTaggerSave`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `Load Image Batch`
- `LoadImage`
- `RH_Translator`
- `SaveImage`
- `String`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
