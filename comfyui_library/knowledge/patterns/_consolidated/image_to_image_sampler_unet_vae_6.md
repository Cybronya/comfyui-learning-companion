---
name: image_to_image_sampler_unet_vae_6
type: Image To Image
frequency: 22
level: moderate
coverage: 0.931136
common_nodes: [AIO_Preprocessor, BlockifyMask, CFGNorm, CLIPLoader, ConditioningZeroOut, DrawMaskOnImage, ImageResizeKJ, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1991033301660049410.json, 图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1998599231973810177.json, 图片生成/图生图/Qwen-Edit一键角色替换(场景迁移，姿势保持)_1988939767981150210.json, 图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json, 图片生成/图生图/Qwen人物迁移（换场景与姿势）_2020760675198443521.json, 图片生成/图生图/Qwen人物迁移（换场景与姿势）_2084548675845574657.json, 图片生成/图生图/人物场景动作变换_2001919928741556226.json, 图片生成/图生图/人物场景迁移保持和参考姿势一致性_1988288063292006401.json, 图片生成/图生图/人物场景迁移保持和参考姿势一致性_1989226111236190209.json, 图片生成/图生图/人物场景迁移保持和参考姿势一致性_2002761035213860866.json, 图片生成/图生图/人物迁移换场景与姿势_1992928354124890113.json, 图片生成/图生图/人物迁移换背景与姿势_1991141914875637761.json, 图片生成/图生图/人物迁移（换场景与姿势）-Qwen_2020677536333697026.json, 图片生成/图生图/人物迁移（换场景与姿势）-Qwen_edit_1989169746773938177.json, 图片生成/图生图/图片换脸人物迁移，换场景与姿势_1998269364778467330.json, 图片生成/图生图/图生图-人物迁移（换场景与姿势）-Qwen_edit_2064152772584497154.json, 图片生成/图生图/改变场景_1998274546052554753.json, 图片生成/图生图/用这个，想去哪儿就去哪儿，随心所欲！人物迁移（换场景与姿势）-Qwen_edit_2021108652312109057.json, 平台全量/Qwen 场景姿势迁移 人物模特动作迁移 人物换场景与姿势_2029022373592178690.json, 平台全量/Qwen人物迁移换场景与姿势_2084852341169287170.json, 平台全量/Qwen人物迁移换场景与姿势_2084903816029360130.json, 平台全量/人物迁移（换场景与姿势)-邻家AI大女孩_2042763965108850690.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1991033301660049410.json、图片生成/图生图/Qwen Edit 人物迁移 替换场景与姿势 替换人物_1998599231973810177.json、图片生成/图生图/Qwen-Edit一键角色替换(场景迁移，姿势保持)_1988939767981150210.json、图片生成/图生图/Qwen_edit + roleScene Blend角色场景融合_1991710780020174849.json、图片生成/图生图/Qwen人物迁移（换场景与姿势）_2020760675198443521.json…）

- **类型**：Image To Image
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 22 个 workflow 都包含：
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
- `ImageConcanate` —— 21/22 个有
- `ImageScaleBy` —— 21/22 个有
- `ImageUpscaleWithModel` —— 21/22 个有
- `PathchSageAttentionKJ` —— 21/22 个有
- `TextEncodeQwenImageEditPlus` —— 21/22 个有
- `UpscaleModelLoader` —— 21/22 个有
- `FlexLoraLoaderModelOnly` —— 17/22 个有
- `LoraLoaderModelOnly` —— 5/22 个有
- `Image Comparer (rgthree)` —— 4/22 个有
- `Anything Everywhere3` —— 1/22 个有
- `BiRefNet_Hugo` —— 1/22 个有
- `CropWithPadInfo` —— 1/22 个有
- `Fast Groups Bypasser (rgthree)` —— 1/22 个有
- `PrimitiveStringMultiline` —— 1/22 个有
- `QwenEditConfigPreparer` —— 1/22 个有
- `QwenEditOutputExtractor` —— 1/22 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | beta57 | - | 22 | 100% |
| 重绘幅度 | 0.1 | 0.1 - 1 | 22 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 43/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 beta57，22 个样本，一致性 100%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 1，22 个样本，取值分散，一致性仅 0%
- 高发问题（43/22 个样本）：Steps较低可能导致细节不足
