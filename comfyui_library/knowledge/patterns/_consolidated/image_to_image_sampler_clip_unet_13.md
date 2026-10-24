---
name: image_to_image_sampler_clip_unet_13
type: Image To Image
frequency: 16
level: moderate
coverage: 0.949875
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein-9B-人像一致性写真_2012875333439070209.json, 图片生成/图生图/Flux2-klein-9B-电影分镜9宫格图_2015764587139833857.json, 图片生成/图生图/Flux2-klein-换脸重绘_2087958705047429121.json, 图片生成/图生图/Klein单图编辑_2013065668022767617.json, 图片生成/图生图/Z-Image-Turbo-洗图工作流_1994007499646894081.json, 图片生成/图生图/flux2-9B-人物三视图生成_2054512404091949058.json, 图片生成/图生图/flux2-klein-9b 局部重绘物品编辑_2058474638291857409.json, 图片生成/图生图/flux2-klein-局部重绘_2087961165291937793.json, 图片生成/图生图/flux2klein9b局部重绘物品编辑_2060700965187178498.json, 图片生成/图生图/flux2klein9b局部重绘物品编辑_2062115957249761281.json, 图片生成/图生图/单图---SD-PPP2.0专用 flux2klein9b局部重绘_2070335294397837313.json, 图片生成/图生图/单图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075093625981194242.json, 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2070327279720423425.json, 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075097575778250753.json, 图片生成/图生图/嘟嘟-Flux2多图编辑_1994409685237239809.json, 图片生成/图生图/移除物体章单图---SD-PPP2.0专用_flux2klein9b局部重绘_2093174966786285569.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Flux2-klein-9B-人像一致性写真_2012875333439070209.json、图片生成/图生图/Flux2-klein-9B-电影分镜9宫格图_2015764587139833857.json、图片生成/图生图/Flux2-klein-换脸重绘_2087958705047429121.json、图片生成/图生图/Klein单图编辑_2013065668022767617.json、图片生成/图生图/Z-Image-Turbo-洗图工作流_1994007499646894081.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `ReferenceLatent` —— 15/16 个有
- `Text Multiline` —— 12/16 个有
- `Kontext Inpainting Conditioning` —— 10/16 个有
- `GrowMaskWithBlur` —— 7/16 个有
- `Image Comparer (rgthree)` —— 7/16 个有
- `Int` —— 7/16 个有
- `PreviewImage` —— 5/16 个有
- `AILab_QwenVL` —— 3/16 个有
- `EmptyFlux2LatentImage` —— 3/16 个有
- `RMBG` —— 3/16 个有
- `easy showAnything` —— 3/16 个有
- `FluxGuidance` —— 2/16 个有
- `JDCN_StringToList` —— 2/16 个有
- `MaskFillHoles` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 16 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，16 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
