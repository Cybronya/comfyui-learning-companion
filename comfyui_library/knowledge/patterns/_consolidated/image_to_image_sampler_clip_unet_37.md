---
name: image_to_image_sampler_clip_unet_37
type: Image To Image
frequency: 9
level: strong
coverage: 0.897889
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合017.图像高清放大_2035275904460525569.json, 图片生成/图生图/3D模型转写实写实效果图_2079501722829025281.json, 图片生成/图生图/F.2 klein9B工业级产品精修_2054118658212941825.json, 图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json, 图片生成/图生图/FLUX2高清_2027640980047925250.json, 图片生成/图生图/FLUX2高清修复人像_2086408949896671233.json, 图片生成/图生图/Flux 2-klein9B工业级产品精修_2015804302496899073.json, 图片生成/图生图/Flux+2-klein9B工业级产品精修_2040782267097812993.json, 图片生成/图生图/WH-AI-Studio（产品精修、旧变新）（人物服装提取、去皱褶）（人物、产品去AI感）电商三合一_2022679693748604930.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合017.图像高清放大_2035275904460525569.json、图片生成/图生图/3D模型转写实写实效果图_2079501722829025281.json、图片生成/图生图/F.2 klein9B工业级产品精修_2054118658212941825.json、图片生成/图生图/F.2 klein9B工业级产品精修_2056255888368955393.json、图片生成/图生图/FLUX2高清_2027640980047925250.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `CR Prompt Text` —— 5/9 个有
- `EmptyFlux2LatentImage` —— 5/9 个有
- `Int` —— 5/9 个有
- `ColorMatch` —— 2/9 个有
- `Float` —— 2/9 个有
- `LatentUpscaleBy` —— 1/9 个有
- `Switch` —— 1/9 个有
- `easy imageColorMatch` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有
- `ttN concat` —— 1/9 个有
- `ttN text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 9 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，9 个样本，取值集中（一致性 97%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
