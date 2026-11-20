---
name: image_to_image_lora_sampler_clip_72
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9086
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.1图生图车身修复_2079052568524845058.json, 图片生成/图生图/【査老师制作】一键老照片修复_1956924520524124162.json, 图片生成/图生图/产品精修2.0-金属类_2016066176866062337.json, 图片生成/图生图/人像日系调色-Kontext_1955302228431179778.json, 平台全量/全能j金属产品精修丨3C电商产品精修V3_2007101040767803394.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/F.1图生图车身修复_2079052568524845058.json、图片生成/图生图/【査老师制作】一键老照片修复_1956924520524124162.json、图片生成/图生图/产品精修2.0-金属类_2016066176866062337.json、图片生成/图生图/人像日系调色-Kontext_1955302228431179778.json、平台全量/全能j金属产品精修丨3C电商产品精修V3_2007101040767803394.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `Int` —— 2/5 个有
- `RebatchLatents` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `RepeatLatentBatch` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `图像缩放V2_孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.59 - 1 | 5 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.59 - 1，5 个样本，取值集中（一致性 82%）
