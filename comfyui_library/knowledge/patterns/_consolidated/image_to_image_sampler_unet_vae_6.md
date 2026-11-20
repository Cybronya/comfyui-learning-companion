---
name: image_to_image_sampler_unet_vae_6
type: Image To Image
frequency: 18
level: moderate
coverage: 0.929556
common_nodes: [CFGNorm, CLIPLoader, CR Text, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物换发型_2037156801669505026.json, 图片生成/图生图/千问2511三图编辑_2004810240099053569.json, 图片生成/图生图/千问2511双图编辑_2004808317312663553.json, 图片生成/图生图/千问Edit-Plus双图编辑_1974067375094018050.json, 图片生成/图生图/千问Edit-Plus图片编辑_1974058449602482178.json, 图片生成/图生图/千问Edit2511三图编辑_2004489688587141122.json, 图片生成/图生图/千问Edit2511单图编辑_2003703669726035969.json, 图片生成/图生图/千问Edit2511双图编辑_2004435367468167169.json, 图片生成/图生图/千问Qwen2511图像编辑换装｜全节点注释喂饭级教程_2063477606913241090.json, 图片生成/图生图/千问edit-老照片修复_2079961641495650306.json, 图片生成/图生图/千问edit视角转换_1987460531059625986.json, 图片生成/图生图/千问最新图像编辑Plus八步加速_1975583252884885506.json, 图片生成/图生图/千问最新编辑模型Plus_1970422090648199170.json, 图片生成/图生图/千问编辑模型Plus三图版_1970743584494415874.json, 图片生成/图生图/去水印_去文字qwen2511_2071627982585810945.json, 图片生成/图生图/图片去水印_2038881204849610753.json, 图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2077676821130338306.json, 图片生成/图生图/少儿_迁移_换装_抠图_runninghub简化版本_2079437242732474369.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/人物换发型_2037156801669505026.json、图片生成/图生图/千问2511三图编辑_2004810240099053569.json、图片生成/图生图/千问2511双图编辑_2004808317312663553.json、图片生成/图生图/千问Edit-Plus双图编辑_1974067375094018050.json、图片生成/图生图/千问Edit-Plus图片编辑_1974058449602482178.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 18 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 15/18 个有
- `FluxKontextMultiReferenceLatentMethod` —— 12/18 个有
- `Image Comparer (rgthree)` —— 4/18 个有
- `PreviewImage` —— 4/18 个有
- `ImageConcanate` —— 3/18 个有
- `BackgroundEraseNetwork` —— 2/18 个有
- `ETN_LoadImageBase64` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `FillMaskedArea_UTK` —— 1/18 个有
- `GrowMask` —— 1/18 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `LoraLoader` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 18 | 28% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 18 | 60% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 67% |
| 重绘幅度 | 1 | 0.82 - 1 | 18 | 96% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，18 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，18 个样本
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.82 - 1，18 个样本，取值集中（一致性 96%）
- 高发问题（16/18 个样本）：Steps较低可能导致细节不足
