---
name: text_to_image_lora_sampler_clip_290
type: Text To Image
frequency: 6
level: strong
coverage: 0.878667
common_nodes: [CLIPLoader, CLIPTextEncode, CR String To Combo, EmptyLatentImage, JjkText, KSampler, LoadImagesFromURL, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Auto-Generate-Goods-Detail单图生成，API自动化出图_2110536704212946946.json, 图片生成/图生图/Auto-Generate-Goods-Detail单图生成，API自动化出图_2110894692589195266.json, 图片生成/图生图/Auto-Generate-Goods-Detail单图编辑，API调用图生图_2110533545289674753.json, 图片生成/图生图/Auto-Generate-Goods-Detail单图编辑，API调用图生图_2111268644561973250.json, 图片生成/图生图/单图编辑API调用工作流｜Auto-Generate-Goods-Detail生成_2097091421084938241.json, 图片生成/图生图/自动生成产品详情页单图版｜API调用图生图_2095274171667402753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_290

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Auto-Generate-Goods-Detail单图生成，API自动化出图_2110536704212946946.json、图片生成/图生图/Auto-Generate-Goods-Detail单图生成，API自动化出图_2110894692589195266.json、图片生成/图生图/Auto-Generate-Goods-Detail单图编辑，API调用图生图_2110533545289674753.json、图片生成/图生图/Auto-Generate-Goods-Detail单图编辑，API调用图生图_2111268644561973250.json、图片生成/图生图/单图编辑API调用工作流｜Auto-Generate-Goods-Detail生成_2097091421084938241.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR String To Combo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImagesFromURL`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/6 个有
- `LoadMultiImage` —— 3/6 个有
- `MUTOU_SmartAspectRatio` —— 3/6 个有
- `PrimitiveString` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `EmptyImage` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `RH_RhartImageG25SunburstImageToImage` —— 2/6 个有
- `RH_RhartImageNNb21ImageToImage` —— 2/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/6 个有
- `RH_RhartImageG2ImageToImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
