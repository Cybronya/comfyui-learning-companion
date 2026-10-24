---
name: text_to_image_lora_sampler_clip_14
type: Text To Image
frequency: 29
level: strong
coverage: 0.935931
common_nodes: [AIO_Preprocessor, BlockifyMask, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DrawMaskOnImage, EmptyLatentImage, ImageConcanate, ImageResizeKJ, ImageScaleToTotalPixels, JjkText, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveInt, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/PS双图人物动作迁移 指定姿势精准复刻图生图编辑_2098280387129733122.json, 图片生成/图生图/QwenEdit 一键换姿势换背景｜图生图换装出图省心省力_2097568848387072002.json, 图片生成/图生图/QwenEdit一键快背景 图生图搭配人物替换效率翻倍_2095803308794531841.json, 图片生成/图生图/QwenEdit一键快背景 图生图搭配人物替换效率翻倍_2107248174195892226.json, 图片生成/图生图/QwenEdit一键快背景_图生图搭配人物替换效率翻倍_2101091977491214338.json, 图片生成/图生图/QwenEdit一键换背景 人物替换图生图工作流实操_2097832944646840322.json, 图片生成/图生图/QwenEdit一键换背景 人物替换图生图工作流实操_2099649480781025282.json, 图片生成/图生图/QwenEdit一键换背景_人物替换图生图工作流实操_2108744207824416769.json, 图片生成/图生图/QwenEdit人物换背景换姿势替换｜图生图动作随心改_2111295737547018241.json, 图片生成/图生图/QwenEdit图片换人换背景V2｜主体场景一起改，出图干净不穿帮_2099440143022256129.json, 图片生成/图生图/QwenEdit图生图_一键换背景同时完成换姿势和角色替换_2109089746055155713.json, 图片生成/图生图/QwenEdit图生图换背景 可同步调整姿势完成角色人物替换_2095805907232976898.json, 图片生成/图生图/QwenEdit图生图换背景 可同步调整姿势完成角色人物替换_2107250684616855554.json, 图片生成/图生图/QwenEdit图生图换背景_可同步调整姿势完成角色人物替换_2101448095660863490.json, 图片生成/图生图/QwenEdit图生图换背景_可同步调整姿势完成角色人物替换_2101554331626598401.json, 图片生成/图生图/人物姿势生成迁移动作迁移｜姿势参考场景一致性人像写真_2086645409799299073.json, 图片生成/图生图/图生图QwenEdit 人物替换配合一键换背景操作简单_2097834263419899905.json, 图片生成/图生图/图生图QwenEdit 人物替换配合一键换背景操作简单_2099651517434388482.json, 图片生成/图生图/图生图QwenEdit_人物替换配合一键换背景操作简单_2108741446466629634.json, 图片生成/图生图/图生图QwenEdit快速换背景 人物替换一步搞定_2095804571183566849.json, 图片生成/图生图/图生图QwenEdit快速换背景 人物替换一步搞定_2107249399859605505.json, 图片生成/图生图/图生图QwenEdit快速换背景_人物替换一步搞定_2100565545732100098.json, 图片生成/图生图/场景一致性动作迁移姿势迁移姿势生成人物姿势姿势参考_2086639455955410946.json, 图片生成/图生图/姿势迁移生成器 参考图控制人物姿势保持场景一致性_2097829144682909697.json, 图片生成/图生图/姿势迁移生成器 参考图控制人物姿势保持场景一致性_2099642661551558657.json, 图片生成/图生图/姿势迁移生成器_参考图控制人物姿势保持场景一致性_2109095510987591681.json, 图片生成/图生图/怪獸人物姿势迁移｜风格化图生图高清放大_2090467050182504449.json, 图片生成/图生图/换姿势换背景一键生成｜QwenEdit图生图工作流_2095589512532545538.json, 图片生成/图生图/换姿势换背景一键生成｜QwenEdit图生图角色表演_2095839532896837633.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/PS双图人物动作迁移 指定姿势精准复刻图生图编辑_2098280387129733122.json、图片生成/图生图/QwenEdit 一键换姿势换背景｜图生图换装出图省心省力_2097568848387072002.json、图片生成/图生图/QwenEdit一键快背景 图生图搭配人物替换效率翻倍_2095803308794531841.json、图片生成/图生图/QwenEdit一键快背景 图生图搭配人物替换效率翻倍_2107248174195892226.json、图片生成/图生图/QwenEdit一键快背景_图生图搭配人物替换效率翻倍_2101091977491214338.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 29 个 workflow 都包含：
- `AIO_Preprocessor`
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 28/29 个有
- `GetImageSize+` —— 28/29 个有
- `ImageResize+` —— 28/29 个有
- `ImageScaleBy` —— 28/29 个有
- `KOOK_ImageCompression` —— 28/29 个有
- `SeedVR2LoadDiTModel` —— 28/29 个有
- `SeedVR2LoadVAEModel` —— 28/29 个有
- `SeedVR2VideoUpscaler` —— 28/29 个有
- `TTP_Image_Assy` —— 28/29 个有
- `TTP_Image_Tile_Batch` —— 28/29 个有
- `TTP_Tile_image_size` —— 28/29 个有
- `孤海注释` —— 20/29 个有
- `PreviewImage` —— 16/29 个有
- `LayerUtility: PurgeVRAM` —— 13/29 个有
- `EmptyImage` —— 9/29 个有
- `CR Text` —— 1/29 个有
- `PIP_图像联结` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 29 | 82% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 29 | 85% |
| 采样算法 | er_sde | - | 29 | 97% |
| 调度器 | beta | - | 29 | 97% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 58/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，29 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，29 个样本，取值集中（一致性 85%）
- 采样算法 最常用 er_sde，29 个样本，一致性 97%
- 调度器 最常用 beta，29 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高发问题（58/29 个样本）：Steps较低可能导致细节不足
