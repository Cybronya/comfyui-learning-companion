---
name: image_to_image_sampler_clip_unet_25
type: Image To Image
frequency: 11
level: moderate
coverage: 0.904727
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2015711272569937921.json, 图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2055150677059489793.json, 图片生成/图生图/FLUX.2-Klein_镜头角度编辑_2024306802296360961.json, 图片生成/图生图/FLUX.2-Klein图生图洗图工作流_2068593056466694146.json, 图片生成/图生图/FLUX2洗图工作流_2000578105506922497.json, 图片生成/图生图/FLUX3图像编辑_2110915403957497858.json, 图片生成/图生图/Kook_Flux_Klein_Realphoto 单图编辑_2022704610548391937.json, 图片生成/图生图/flux-2-klein-3个图编辑_2093270833983746050.json, 图片生成/图生图/flux-2-klein-4图编辑_2093275669819121666.json, 图片生成/图生图/flux-2-klein-9b超强老照片修复-高清放大_2038820603309854721.json, 图片生成/图生图/flux2高清放大工作流_2060199591257133057.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2015711272569937921.json、图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2055150677059489793.json、图片生成/图生图/FLUX.2-Klein_镜头角度编辑_2024306802296360961.json、图片生成/图生图/FLUX.2-Klein图生图洗图工作流_2068593056466694146.json、图片生成/图生图/FLUX2洗图工作流_2000578105506922497.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/11 个有
- `Image Comparer (rgthree)` —— 7/11 个有
- `ReferenceLatent` —— 7/11 个有
- `EmptyFlux2LatentImage` —— 5/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `FluxGuidance` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `CR Prompt List` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `ImageScaleBy` —— 1/11 个有
- `LayerUtility: NanoBananaImageScale` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 22 | 11 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 11 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 22，11 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，11 个样本
- 高发问题（10/11 个样本）：Steps较低可能导致细节不足
