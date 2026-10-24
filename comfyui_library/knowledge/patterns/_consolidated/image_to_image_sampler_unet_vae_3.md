---
name: image_to_image_sampler_unet_vae_3
type: Image To Image
frequency: 18
level: moderate
coverage: 0.927778
common_nodes: [AIO_Preprocessor, BlockifyMask, CFGNorm, CLIPLoader, ConditioningZeroOut, DrawMaskOnImage, ImageResizeKJ, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1991033301660049410.json, 图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1998599231973810177.json, 图片生成/图生图/Qwen-Edit一键角色替换(场景迁移，姿势保持)_1988939767981150210.json, 图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json, 图片生成/图生图/Qwen人物迁移（换场景与姿势）_2020760675198443521.json, 图片生成/图生图/Qwen人物迁移（换场景与姿势）_2084548675845574657.json, 图片生成/图生图/人物场景动作变换_2001919928741556226.json, 图片生成/图生图/人物场景迁移保持和参考姿势一致性_1988288063292006401.json, 图片生成/图生图/人物场景迁移保持和参考姿势一致性_1989226111236190209.json, 图片生成/图生图/人物场景迁移保持和参考姿势一致性_2002761035213860866.json, 图片生成/图生图/人物迁移换场景与姿势_1992928354124890113.json, 图片生成/图生图/人物迁移换背景与姿势_1991141914875637761.json, 图片生成/图生图/人物迁移（换场景与姿势）-Qwen_2020677536333697026.json, 图片生成/图生图/人物迁移（换场景与姿势）-Qwen_edit_1989169746773938177.json, 图片生成/图生图/图片换脸人物迁移，换场景与姿势_1998269364778467330.json, 图片生成/图生图/图生图-人物迁移（换场景与姿势）-Qwen_edit_2064152772584497154.json, 图片生成/图生图/改变场景_1998274546052554753.json, 图片生成/图生图/用这个，想去哪儿就去哪儿，随心所欲！人物迁移（换场景与姿势）-Qwen_edit_2021108652312109057.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1991033301660049410.json、图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1998599231973810177.json、图片生成/图生图/Qwen-Edit一键角色替换(场景迁移，姿势保持)_1988939767981150210.json、图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json、图片生成/图生图/Qwen人物迁移（换场景与姿势）_2020760675198443521.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 18 个 workflow 都包含：
- `AIO_Preprocessor`
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 17/18 个有
- `ImageScaleBy` —— 17/18 个有
- `ImageUpscaleWithModel` —— 17/18 个有
- `PathchSageAttentionKJ` —— 17/18 个有
- `TextEncodeQwenImageEditPlus` —— 17/18 个有
- `UpscaleModelLoader` —— 17/18 个有
- `FlexLoraLoaderModelOnly` —— 13/18 个有
- `LoraLoaderModelOnly` —— 5/18 个有
- `Image Comparer (rgthree)` —— 4/18 个有
- `Anything Everywhere3` —— 1/18 个有
- `CropWithPadInfo` —— 1/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `QwenEditConfigPreparer` —— 1/18 个有
- `QwenEditOutputExtractor` —— 1/18 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | beta57 | - | 18 | 100% |
| 重绘幅度 | 0.1 | 0.1 - 1 | 18 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 beta57，18 个样本，一致性 100%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 1，18 个样本，取值分散，一致性仅 0%
- 高发问题（35/18 个样本）：Steps较低可能导致细节不足
