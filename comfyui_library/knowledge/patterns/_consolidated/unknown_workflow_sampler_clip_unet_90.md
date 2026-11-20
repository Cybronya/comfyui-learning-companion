---
name: unknown_workflow_sampler_clip_unet_90
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.887
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Bernini图片编辑+完美换装_2062428428065923073.json, 图片生成/图生图/F-2klein 9b无塑料感高清修复_2064209222493102082.json, 图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json, 图片生成/图生图/Klein 高清放大修复V2_2061130933612404737.json, 图片生成/图生图/Klein无塑料感高清修复_2061243781923557377.json, 图片生成/图生图/Klein调色_2055545779061829634.json, 图片生成/图生图/图像调色板-0偏移_2055573571447074818.json, 图片生成/图生图/模糊图片变清晰  图像清晰修复 高清放大_2061621095765204994.json, 图片生成/图生图/照片调色Color Master_ Multiple Photo Editing_2092443486053294081.json, 图片生成/图生图/调色大师 照片调色多风格-多种预设可选择_flux2+kelin_2084143743241900034.json, 图片生成/图生图/调色大师-多种预设选择_flux2 kelin_2064907302485975041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Bernini图片编辑+完美换装_2062428428065923073.json、图片生成/图生图/F-2klein 9b无塑料感高清修复_2064209222493102082.json、图片生成/图生图/F.2klein 9b无塑料感高清修复强烈推荐版_2062160878765694977.json、图片生成/图生图/Klein 高清放大修复V2_2061130933612404737.json、图片生成/图生图/Klein无塑料感高清修复_2061243781923557377.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `Image Comparer (rgthree)` —— 10/11 个有
- `ReferenceLatent` —— 10/11 个有
- `VAEEncode` —— 10/11 个有
- `ImageResizeKJv2` —— 9/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `LatentBlend` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `easy imageColorMatch` —— 5/11 个有
- `CR Text` —— 4/11 个有
- `Int` —— 4/11 个有
- `Anything Everywhere3` —— 3/11 个有
- `Float` —— 3/11 个有
- `ImpactSwitch` —— 3/11 个有
- `easy imageConcat` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `BerniniConditioning` —— 1/11 个有
- `ModelSamplingSD3` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 73% |
| Prompt 约束强度(CFG) | 4 | 4 - 12 | 11 | 51% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | sa_solver | - | 11 | 45% |
| 重绘幅度 | simple | - | 11 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 73%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 12，11 个样本
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，11 个样本，一致性 45%
- 重绘幅度 最常用 simple，11 个样本，一致性 55%
