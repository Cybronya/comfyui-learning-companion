---
name: text_to_image_lora_sampler_clip_244
type: Text To Image
frequency: 8
level: strong
coverage: 0.8865
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext人像修图调色 清新色调图生图精修处理_2099220069216776194.json, 图片生成/图生图/kontext一键去水印带前后对比｜图生图无痕修复，老照片旧图拯救_2107311794724364289.json, 图片生成/图生图/qwen_image_edit_2511三视图｜角色一致性设计图生成_2093135891593256962.json, 图片生成/图生图/人像光影融合｜MAGIC-K-V1打光换背景生成_2093877817636376577.json, 图片生成/图生图/人像光影融合｜MAGIC-K-V1打光换背景生成_2093901151463890945.json, 图片生成/图生图/图生图图片编辑多图编辑 多张输入精准改图_2109786356653322241.json, 图片生成/图生图/开源玩法大全｜FLUX_Kontext商品换背景角色一致性_2091226009478717441.json, 图片生成/文生图/Kontext一键去水印前后对比工作流，文生图图生图去水印处理工具_2107559098299535361.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_244

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Kontext人像修图调色 清新色调图生图精修处理_2099220069216776194.json、图片生成/图生图/kontext一键去水印带前后对比｜图生图无痕修复，老照片旧图拯救_2107311794724364289.json、图片生成/图生图/qwen_image_edit_2511三视图｜角色一致性设计图生成_2093135891593256962.json、图片生成/图生图/人像光影融合｜MAGIC-K-V1打光换背景生成_2093877817636376577.json、图片生成/图生图/人像光影融合｜MAGIC-K-V1打光换背景生成_2093901151463890945.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 7/8 个有
- `VAEEncode` —— 7/8 个有
- `DualCLIPLoader` —— 6/8 个有
- `FluxGuidance` —— 6/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `孤海注释` —— 6/8 个有
- `PreviewImage` —— 5/8 个有
- `FluxKontextImageScale` —— 4/8 个有
- `CFGNorm` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `TextEncodeQwenImageEditPlus` —— 2/8 个有
- `easy positive` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `ConstrainImage|pysssss` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `Image Levels Adjustment` —— 1/8 个有
- `ImageStitch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（12/8 个样本）：Steps较低可能导致细节不足
