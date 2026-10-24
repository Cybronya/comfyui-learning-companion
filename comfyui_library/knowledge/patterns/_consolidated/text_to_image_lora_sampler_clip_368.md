---
name: text_to_image_lora_sampler_clip_368
type: Text To Image
frequency: 5
level: strong
coverage: 0.8344
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, RH_YouchuanTextToImageV82Fast, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MJ v8.2批量图像生成，文生图反推提示词出图高效_2110530412689842177.json, 图片生成/文生图/MJ_v8.2批量图像生成，文生图反推提示词出图高效_2111271277263671297.json, 图片生成/文生图/MJ悠船V8.2美学艺术图像模型 文生图图生图创作_2099916811176341505.json, 图片生成/文生图/美学艺术图像V8.2｜MJ悠船文生图+图生图赛博朋克_2094046651701874690.json, 图片生成/文生图/美学艺术图像模型｜MJ悠船V8.2文生图+图生图_2093840807345348609.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_368

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/MJ v8.2批量图像生成，文生图反推提示词出图高效_2110530412689842177.json、图片生成/文生图/MJ_v8.2批量图像生成，文生图反推提示词出图高效_2111271277263671297.json、图片生成/文生图/MJ悠船V8.2美学艺术图像模型 文生图图生图创作_2099916811176341505.json、图片生成/文生图/美学艺术图像V8.2｜MJ悠船文生图+图生图赛博朋克_2094046651701874690.json、图片生成/文生图/美学艺术图像模型｜MJ悠船V8.2文生图+图生图_2093840807345348609.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `RH_YouchuanTextToImageV82Fast`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `PlaySound|pysssss` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `RH_Captioner_Pro` —— 2/5 个有
- `RebatchImages` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `YuanMultiImage` —— 2/5 个有
- `EmptyImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
