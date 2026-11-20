---
name: image_to_image_sampler_clip_unet_22
type: Image To Image
frequency: 12
level: strong
coverage: 0.944833
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein-换脸重绘_2087958705047429121.json, 图片生成/图生图/Flux2-klein-水印移除极速版_2015410628701196290.json, 图片生成/图生图/Klein-9B-自动人像动作九宫图_2049116824888942594.json, 图片生成/图生图/flux2-klein-9b 局部重绘物品编辑_2058474638291857409.json, 图片生成/图生图/flux2-klein-局部重绘_2087961165291937793.json, 图片生成/图生图/flux2klein9b局部重绘物品编辑_2060700965187178498.json, 图片生成/图生图/flux2klein9b局部重绘物品编辑_2062115957249761281.json, 图片生成/图生图/单图---SD-PPP2.0专用 flux2klein9b局部重绘_2070335294397837313.json, 图片生成/图生图/单图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075093625981194242.json, 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2070327279720423425.json, 图片生成/图生图/双图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075097575778250753.json, 图片生成/图生图/移除物体章单图---SD-PPP2.0专用_flux2klein9b局部重绘_2093174966786285569.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux2-klein-换脸重绘_2087958705047429121.json、图片生成/图生图/Flux2-klein-水印移除极速版_2015410628701196290.json、图片生成/图生图/Klein-9B-自动人像动作九宫图_2049116824888942594.json、图片生成/图生图/flux2-klein-9b 局部重绘物品编辑_2058474638291857409.json、图片生成/图生图/flux2-klein-局部重绘_2087961165291937793.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
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
- `Kontext Inpainting Conditioning` —— 10/12 个有
- `Text Multiline` —— 10/12 个有
- `Image Comparer (rgthree)` —— 8/12 个有
- `Int` —— 8/12 个有
- `GrowMaskWithBlur` —— 7/12 个有
- `PreviewImage` —— 5/12 个有
- `RMBG` —— 3/12 个有
- `MaskFillHoles` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `JDCN_StringToList` —— 1/12 个有
- `YC Color Match` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 12 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
