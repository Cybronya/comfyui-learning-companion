---
name: image_to_image_sampler_clip_unet_162
type: Image To Image
frequency: 4
level: moderate
coverage: 0.88775
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Flux2-klein-9B 人像一致性写真 写实摄影 去除AI塑料感 增加真实细节_2014154236057100290.json, 平台全量/Klein 图像编辑_2015686192544616449.json, 平台全量/flux2-klein-摄影滤镜-色调及光线迁移_2030094809662234626.json, 平台全量/摄影滤镜 Flux2-Klein9b  色调及光线迁移 艺术光影 蝴蝶光_2031197859596476417.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_162

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Flux2-klein-9B 人像一致性写真 写实摄影 去除AI塑料感 增加真实细节_2014154236057100290.json、平台全量/Klein 图像编辑_2015686192544616449.json、平台全量/flux2-klein-摄影滤镜-色调及光线迁移_2030094809662234626.json、平台全量/摄影滤镜 Flux2-Klein9b  色调及光线迁移 艺术光影 蝴蝶光_2031197859596476417.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `ImitationHueNode` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `JDCN_StringToList` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | 4 - 8 | 4 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.875 | 0.75 - 1 | 4 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.875，观测区间 0.75 - 1，4 个样本，取值集中（一致性 86%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
