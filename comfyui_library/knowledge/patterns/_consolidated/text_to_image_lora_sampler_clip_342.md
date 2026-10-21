---
name: text_to_image_lora_sampler_clip_342
type: Text To Image
frequency: 2
level: weak
coverage: 0.8115
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageResizeKJv2, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RMBG, SAM3_Detect, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerMask: MaskGrow, LayerUtility: TextJoin, LayerMask: MaskPreview]
members: [图片生成/图生图/2092142218990669826.json, 图片生成/图生图/2102109884312543233.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_342

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2092142218990669826.json、图片生成/图生图/2102109884312543233.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RMBG`
- `SAM3_Detect`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `MaskFillHoles` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `Text` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1000 | - | 2 | 8% |
| 高度 | 580 | - | 2 | 14% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1000，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 高度 中位数 580，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高发问题（9/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerMask: MaskGrow、LayerUtility: TextJoin、LayerMask: MaskPreview
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
