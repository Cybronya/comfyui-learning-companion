---
name: image_to_image_lora_sampler_unet_22
type: Image To Image
frequency: 19
level: weak
coverage: 0.766895
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed Edit艺术字风格迁移设计_2052228410910486530.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059096605923565569.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059435718690304002.json, 图片生成/图生图/FireRed Edit艺术字风格迁移设计_2061660098623262721.json, 图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json, 图片生成/图生图/FireRed Image-Edit 1.1_2032008809652166657.json, 图片生成/图生图/FireRed-Image-Edit-1.1 图像编辑_2027773296359514113.json, 图片生成/图生图/FireRed-Image-EditV1.1单图编辑_2029504867747766274.json, 图片生成/图生图/FireRed_Edit艺术字风格迁移设计_2069077798647586817.json, 图片生成/图生图/Qwen Image Edit 2511 3张参考图生图_2078472969151668226.json, 图片生成/图生图/firered-image-edit-1.1官方发布版_2030518527010021378.json, 图片生成/图生图/image_firered_image_edit1_图生图_2032289203324723201.json, 图片生成/图生图/一键生成多角度（八角度）+全节点注释_2053298166606376961.json, 图片生成/图生图/九宫格_2114550968254820353.json, 图片生成/图生图/九宫格拼版_Qwen图像编辑双参考_2114889131951222786.json, 图片生成/图生图/九宫格拼版_Qwen图像编辑双参考_2115621709540847617.json, 图片生成/图生图/九宫格拼版_Qwen图像编辑双参考_2115668932546883585.json, 图片生成/图生图/人像换发工作流_8hair_2085998735972192257.json, 图片生成/图生图/四图工作流_2078025777152610306.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_22

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/FireRed Edit艺术字风格迁移设计_2052228410910486530.json、图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059096605923565569.json、图片生成/图生图/FireRed Edit艺术字风格迁移设计_2059435718690304002.json、图片生成/图生图/FireRed Edit艺术字风格迁移设计_2061660098623262721.json、图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 19 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 18/19 个有
- `PrimitiveBoolean` —— 14/19 个有
- `PrimitiveFloat` —— 14/19 个有
- `PrimitiveInt` —— 14/19 个有
- `ComfySwitchNode` —— 13/19 个有
- `FluxKontextMultiReferenceLatentMethod` —— 7/19 个有
- `CR Text` —— 5/19 个有
- `easy imageConcat` —— 5/19 个有
- `ImageScale` —— 2/19 个有
- `PreviewAny` —— 2/19 个有
- `CustomCombo` —— 1/19 个有
- `DF_Get_image_size` —— 1/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `ImageBatch` —— 1/19 个有
- `JsonExtractString` —— 1/19 个有
- `PrimitiveStringMultiline` —— 1/19 个有
- `StringConcatenate` —— 1/19 个有
- `Switch any [Crystools]` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 40 | 19 | 43% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 19 | 33% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 40，19 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，19 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
