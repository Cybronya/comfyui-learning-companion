---
name: image_to_image_sampler_vae_11
type: Image To Image
frequency: 11
level: moderate
coverage: 0.937545
common_nodes: [AIO_Preprocessor, BlockifyMask, CFGNorm, CLIPLoader, ConditioningZeroOut, DrawMaskOnImage, ImageResizeKJ, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku极速人物场景迁移保持和参考姿势一致性V3_1992809205547724801.json, 图片生成/图生图/Qwen edit 2509：RoleScene Blend V2人物场景迁移，保持和参考姿势一致性_1991767204832309249.json, 图片生成/图生图/人物+场景一致性关键帧_2073714895434117122.json, 图片生成/图生图/人物场景迁移保持和参考姿势一致性V2_1991499524558503938.json, 图片生成/图生图/换姿势  动作 换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2079465205800726529.json, 图片生成/图生图/换姿势  换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2079972639212396546.json, 图片生成/图生图/换姿势  换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2083434058905907202.json, 图片生成/图生图/换姿势  换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2084322846502903810.json, 图片生成/图生图/换姿势  换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2085597554330390530.json, 图片生成/图生图/换姿势  换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2086825756851785730.json, 图片生成/图生图/换背景 换姿势 角色替换  人物替换 一键换背景 图生图  QwenEdit_2097187970817290242.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_11

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Nunchaku极速人物场景迁移保持和参考姿势一致性V3_1992809205547724801.json、图片生成/图生图/Qwen edit 2509：RoleScene Blend V2人物场景迁移，保持和参考姿势一致性_1991767204832309249.json、图片生成/图生图/人物+场景一致性关键帧_2073714895434117122.json、图片生成/图生图/人物场景迁移保持和参考姿势一致性V2_1991499524558503938.json、图片生成/图生图/换姿势  动作 换背景 角色替换  人物替换 一键换背景 图生图  QwenEdit_2079465205800726529.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 10/11 个有
- `ImageConcanate` —— 10/11 个有
- `LayerMask: BiRefNetUltraV2` —— 10/11 个有
- `LayerMask: LoadBiRefNetModelV2` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `PreviewImage` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `Image Comparer (rgthree)` —— 4/11 个有
- `ImageUpscaleWithModel` —— 4/11 个有
- `PathchSageAttentionKJ` —— 4/11 个有
- `QwenEditOutputExtractor` —— 4/11 个有
- `UpscaleModelLoader` —— 4/11 个有
- `ImageScaleBy` —— 3/11 个有
- `SeedVR2LoadDiTModel` —— 2/11 个有
- `LayerUtility: ImageReel` —— 1/11 个有
- `LayerUtility: ImageReelComposit` —— 1/11 个有
- `NunchakuQwenImageDiTLoader` —— 1/11 个有
- `NunchakuQwenImageLoraLoader` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `RMBG` —— 1/11 个有
- `SeedVR2LoadVAEModel` —— 1/11 个有
- `SeedVR2VideoUpscaler` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta57 | - | 11 | 91% |
| 重绘幅度 | 1 | 0.2 - 1 | 11 | 54% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta57，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，11 个样本
- 高发问题（14/11 个样本）：Steps较低可能导致细节不足
