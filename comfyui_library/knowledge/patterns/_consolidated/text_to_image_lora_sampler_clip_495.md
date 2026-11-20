---
name: text_to_image_lora_sampler_clip_495
type: Text To Image
frequency: 4
level: strong
coverage: 0.88775
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MJ v8.2批量图像生成，文生图反推提示词出图高效_2110530412689842177.json, 图片生成/文生图/MJ_v8.2批量图像生成，文生图反推提示词出图高效_2111271277263671297.json, 图片生成/文生图/z-image文生图工作流｜轻量出图响应快，日常配图随手就能出_2099545132960935937.json, 图片生成/文生图/全能图片G-image-2.5文生图高品质版｜一句话出好图，细节给足_2099479665718153217.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_495

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/MJ v8.2批量图像生成，文生图反推提示词出图高效_2110530412689842177.json、图片生成/文生图/MJ_v8.2批量图像生成，文生图反推提示词出图高效_2111271277263671297.json、图片生成/文生图/z-image文生图工作流｜轻量出图响应快，日常配图随手就能出_2099545132960935937.json、图片生成/文生图/全能图片G-image-2.5文生图高品质版｜一句话出好图，细节给足_2099479665718153217.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `RH_Captioner_Pro` —— 2/4 个有
- `RH_YouchuanTextToImageV82Fast` —— 2/4 个有
- `RebatchImages` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `YuanMultiImage` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
