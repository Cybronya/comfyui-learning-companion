---
name: text_to_image_lora_sampler_clip_193
type: Text To Image
frequency: 4
level: strong
coverage: 0.838
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, EmptySD3LatentImage, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [GetImageSize+, Seed (rgthree)]
members: [图片生成/图生图/2106100322811863041.json, 数字人/数字人/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100267474842378242.json, 视频生成/图生视频/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100661143726542849.json, 视频生成/文生视频/单图编辑完美一致性｜Krea2文生图图生视频生成_2090203681751912449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_193

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2106100322811863041.json、数字人/数字人/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100267474842378242.json、视频生成/图生视频/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100661143726542849.json、视频生成/文生视频/单图编辑完美一致性｜Krea2文生图图生视频生成_2090203681751912449.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `JjkText`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `GetImageSize+` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有

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
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：GetImageSize+、Seed (rgthree)
