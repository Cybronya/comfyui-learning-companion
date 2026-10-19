---
name: text_to_image_lora_sampler_clip_170
type: Text To Image
frequency: 5
level: strong
coverage: 0.8398
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [ImageCASharpening+, workflow>klein高清, workflow>人物皮肤高清, workflow>krea2高清]
members: [图片生成/图生图/2102177419565297665.json, 图片生成/图生图/2102212532319641601.json, 图片生成/图生图/2102577836518367234.json, 图片生成/图生图/2102599156345958401.json, 图片生成/图生图/2105813111113601026.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_170

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102177419565297665.json、图片生成/图生图/2102212532319641601.json、图片生成/图生图/2102577836518367234.json、图片生成/图生图/2102599156345958401.json、图片生成/图生图/2105813111113601026.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `Image Comparer (rgthree)` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `workflow>klein高清` —— 2/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_DLSS5Enhance` —— 1/5 个有
- `RH_RhartImageG2ImageToImage` —— 1/5 个有
- `TextEncodeQwenImage21` —— 1/5 个有
- `workflow>krea2高清` —— 1/5 个有
- `workflow>人物皮肤高清` —— 1/5 个有

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
- 这些节点还没有知识卡，系统对它们的理解有限：ImageCASharpening+、workflow>klein高清、workflow>人物皮肤高清、workflow>krea2高清
