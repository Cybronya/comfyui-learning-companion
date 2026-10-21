---
name: text_to_image_sampler_clip_unet_163
type: Text To Image
frequency: 2
level: weak
coverage: 0.821
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image Turbo文生图_1993896217822380033.json, 图片生成/文生图/Z-image 文生图，反推，批量生图（最强合集）_1994221059754967042.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_163

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image Turbo文生图_1993896217822380033.json、图片生成/文生图/Z-image 文生图，反推，批量生图（最强合集）_1994221059754967042.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FSampler` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy promptList` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.775 | - | 2 | 71% |
| 宽度 | 924 | - | 2 | 83% |
| 高度 | 1728 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.775，样本不足，未给区间，2 个样本
- 宽度 中位数 924，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1728，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
