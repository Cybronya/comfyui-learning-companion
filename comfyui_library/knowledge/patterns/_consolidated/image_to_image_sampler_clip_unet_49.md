---
name: image_to_image_sampler_clip_unet_49
type: Image To Image
frequency: 8
level: moderate
coverage: 0.888
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-IMAGE 快速洗图PS版本_1980163824957427714.json, 图片生成/图生图/Z-Image-De洗图图生图_1997877980846260226.json, 图片生成/图生图/Z-Image-Trubo动漫转真人基础版_2033198187133014018.json, 图片生成/图生图/Z-Image-Turbo 图生图编辑 _ 极简 10 节点，8 步出片_2086644646930903041.json, 图片生成/图生图/Z-image+千问VL反推图生图洗图增强真实感_1993893012516306946.json, 图片生成/图生图/Z-image图生图-真实感洗图_1996077315346087937.json, 图片生成/图生图/Z-image图生图洗图_2015740669658144770.json, 图片生成/图生图/Z-image图生图洗图增加真实感_1996559760713457666.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-IMAGE 快速洗图PS版本_1980163824957427714.json、图片生成/图生图/Z-Image-De洗图图生图_1997877980846260226.json、图片生成/图生图/Z-Image-Trubo动漫转真人基础版_2033198187133014018.json、图片生成/图生图/Z-Image-Turbo 图生图编辑 _ 极简 10 节点，8 步出片_2086644646930903041.json、图片生成/图生图/Z-image+千问VL反推图生图洗图增强真实感_1993893012516306946.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `AILab_QwenVL` —— 4/8 个有
- `PrimitiveInt` —— 4/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `LayerUtility: TextJoin` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 8 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 8 | 71% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 0.45 | 0.3 - 0.75 | 8 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 0.45，观测区间 0.3 - 0.75，8 个样本
