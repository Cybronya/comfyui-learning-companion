---
name: image_to_image_upscale_sampler_unet_5
type: Image To Image
frequency: 2
level: weak
coverage: 0.658
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, ConditioningZeroOut, GetNode, ImageConcatMulti, ImageResizeKJ, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerUtility: ImageBlend, LoadImage, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物替换 · 姿势参考 · 还原质感 【1.0 】_1990609749903368194.json, 图片生成/图生图/图像 人物替换 + 动作迁移 【 2.0 】_2002941592669437953.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物替换 · 姿势参考 · 还原质感 【1.0 】_1990609749903368194.json、图片生成/图生图/图像 人物替换 + 动作迁移 【 2.0 】_2002941592669437953.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `QwenEditConfigPreparer` —— 1/2 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/2 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/2 个有
- `easy imagePixelPerfect` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有
- `孤海图像缩放按像素` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
