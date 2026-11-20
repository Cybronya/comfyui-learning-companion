---
name: image_to_image_sampler_clip_unet_26
type: Image To Image
frequency: 13
level: moderate
coverage: 0.929846
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/25.tonnie-Qwen洗图（带中文）_1998065820255289345.json, 图片生成/图生图/251207-03.Z_image_turbo图生图_1997679619232960513.json, 图片生成/图生图/F2_klein单图改图_2056203791569039361.json, 图片生成/图生图/FLUX 2 图生图_1993556092405874690.json, 图片生成/图生图/FLUX 2 多图编辑_1993562616243093506.json, 图片生成/图生图/FLUX2洗图工作流_2000578105506922497.json, 图片生成/图生图/Flux2-Klein-单图编辑 （转真实lora）_2091149910098927618.json, 图片生成/图生图/Klein-9B-换头一键封神！_2034251935917805570.json, 图片生成/图生图/QY7-千像归一（kontext）单图版 一键融合打光，溶图kontext_1967603421962526721.json, 图片生成/图生图/flux2高清放大工作流_2060199591257133057.json, 图片生成/图生图/精修_产品直出电商摄影图_美工必备_2015801568494358530.json, 图片生成/图生图/精修白底不求人-手机随手拍高质量电商主图，扣图去背景_1993571394655109121.json, 平台全量/电商产品 白底图片生成 精修变白底 电商主图，扣图去背景 产品白底图 摄影产品精修_2010600711561678850.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/25.tonnie-Qwen洗图（带中文）_1998065820255289345.json、图片生成/图生图/251207-03.Z_image_turbo图生图_1997679619232960513.json、图片生成/图生图/F2_klein单图改图_2056203791569039361.json、图片生成/图生图/FLUX 2 图生图_1993556092405874690.json、图片生成/图生图/FLUX 2 多图编辑_1993562616243093506.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 12/13 个有
- `Image Comparer (rgthree)` —— 10/13 个有
- `ReferenceLatent` —— 10/13 个有
- `ConditioningZeroOut` —— 8/13 个有
- `FluxGuidance` —— 8/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/13 个有
- `LoraLoaderModelOnly` —— 7/13 个有
- `EmptyFlux2LatentImage` —— 5/13 个有
- `ImageScaleToTotalPixels` —— 5/13 个有
- `ModelSamplingAuraFlow` —— 5/13 个有
- `DualCLIPLoader` —— 4/13 个有
- `CFGNorm` —— 3/13 个有
- `EmptySD3LatentImage` —— 3/13 个有
- `GetImageSize+` —— 3/13 个有
- `TextEncodeQwenImageEdit` —— 3/13 个有
- `TextInput_` —— 3/13 个有
- `LayerMask: BiRefNetUltraV2` —— 2/13 个有
- `LayerMask: LoadBiRefNetModel` —— 2/13 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `PlaySound|pysssss` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `RH_Captioner` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 22 | 13 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 13 | 54% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 0.6 - 1 | 13 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 22，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，13 个样本，取值集中（一致性 81%）
- 高发问题（8/13 个样本）：Steps较低可能导致细节不足
