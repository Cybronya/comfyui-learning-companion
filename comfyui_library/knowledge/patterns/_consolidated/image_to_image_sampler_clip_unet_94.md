---
name: image_to_image_sampler_clip_unet_94
type: Image To Image
frequency: 5
level: weak
coverage: 0.9732
common_nodes: [CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2真人转动漫工作流_2074098918060814337.json, 图片生成/图生图/LABUBU图生图_1936650163987337217.json, 图片生成/图生图/Qwen-Image图生图玄学祈福壁纸可修改_1954030906807865345.json, 图片生成/图生图/Z IMAGE 增加皮肤细节 图生图 单张_2099267046755360769.json, 图片生成/图生图/动漫真人转CG风格_2074082230468694017.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Krea2真人转动漫工作流_2074098918060814337.json、图片生成/图生图/LABUBU图生图_1936650163987337217.json、图片生成/图生图/Qwen-Image图生图玄学祈福壁纸可修改_1954030906807865345.json、图片生成/图生图/Z IMAGE 增加皮肤细节 图生图 单张_2099267046755360769.json、图片生成/图生图/动漫真人转CG风格_2074082230468694017.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CLIPLoader` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `WD14Tagger|pysssss` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `StringConcatenate` —— 2/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 5 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 33% |
| 采样算法 | er_sde | - | 5 | 40% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.6 | 0.3 - 1 | 5 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，5 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 er_sde，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.3 - 1，5 个样本
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
