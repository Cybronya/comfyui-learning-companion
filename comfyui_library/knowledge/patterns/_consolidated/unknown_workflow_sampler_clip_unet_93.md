---
name: unknown_workflow_sampler_clip_unet_93
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.88575
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Bernini图片编辑+完美换装_2062428428065923073.json, 图片生成/图生图/F-2klein 9b无塑料感高清修复_2064209222493102082.json, 图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json, 图片生成/图生图/Klein 高清放大修复V2_2061130933612404737.json, 图片生成/图生图/Klein无塑料感高清修复_2061243781923557377.json, 图片生成/图生图/Klein调色_2055545779061829634.json, 图片生成/图生图/图像调色板-0偏移_2055573571447074818.json, 图片生成/图生图/模糊图片变清晰  图像清晰修复 高清放大_2061621095765204994.json, 图片生成/图生图/照片调色Color Master_ Multiple Photo Editing_2092443486053294081.json, 图片生成/图生图/调色大师 照片调色多风格-多种预设可选择_flux2+kelin_2084143743241900034.json, 图片生成/图生图/调色大师-多种预设选择_flux2 kelin_2064907302485975041.json, 平台全量/图片调色 图片滤镜 氛围感_2066539042715553794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Bernini图片编辑+完美换装_2062428428065923073.json、图片生成/图生图/F-2klein 9b无塑料感高清修复_2064209222493102082.json、图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json、图片生成/图生图/Klein 高清放大修复V2_2061130933612404737.json、图片生成/图生图/Klein无塑料感高清修复_2061243781923557377.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `Image Comparer (rgthree)` —— 11/12 个有
- `ReferenceLatent` —— 11/12 个有
- `VAEEncode` —— 11/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `LoraLoaderModelOnly` —— 10/12 个有
- `LatentBlend` —— 6/12 个有
- `PreviewImage` —— 6/12 个有
- `CR Text` —— 5/12 个有
- `Int` —— 5/12 个有
- `easy imageColorMatch` —— 5/12 个有
- `Anything Everywhere3` —— 4/12 个有
- `Float` —— 4/12 个有
- `ImpactSwitch` —— 4/12 个有
- `easy imageConcat` —— 4/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `BerniniConditioning` —— 1/12 个有
- `ModelSamplingSD3` —— 1/12 个有
- `PrimitiveFloat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 12 | 12 | 53% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 12 | 50% |
| 重绘幅度 | simple | - | 12 | 58% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 12，12 个样本
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，12 个样本，一致性 50%
- 重绘幅度 最常用 simple，12 个样本，一致性 58%
