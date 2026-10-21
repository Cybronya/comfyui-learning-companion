---
name: text_to_image_lora_sampler_clip_240
type: Text To Image
frequency: 5
level: strong
coverage: 0.8696
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, EmptySD3LatentImage, JjkText, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100267474842378242.json, 数字人/数字人/krea_quadview_i2i 四视图生图｜人物角色数字人多视角_2096909828131213314.json, 数字人/数字人/krea_quadview_i2i四视图编辑｜人物角色数字人图生图_2096703736772128769.json, 数字人/数字人/四视图一站生成｜MiniMaxH3数字人辅助k2_2096597022622175233.json, 视频生成/图生视频/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100661143726542849.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_240

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100267474842378242.json、数字人/数字人/krea_quadview_i2i 四视图生图｜人物角色数字人多视角_2096909828131213314.json、数字人/数字人/krea_quadview_i2i四视图编辑｜人物角色数字人图生图_2096703736772128769.json、数字人/数字人/四视图一站生成｜MiniMaxH3数字人辅助k2_2096597022622175233.json、视频生成/图生视频/Krea2角色漫剧真人资产四视图一键生成4步加速版_2100661143726542849.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `PreviewImage` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `AddLabel` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `SetNode` —— 2/5 个有

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
