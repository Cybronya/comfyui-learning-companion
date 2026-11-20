---
name: image_to_image_lora_sampler_clip_144
type: Image To Image
frequency: 3
level: moderate
coverage: 0.812333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/工作流基础系列01-Klein的单图编辑工作流-基础向讲解此工作流_2012461408067260418.json, 图片生成/图生图/模糊照片修复_2042277567725572098.json, 图片生成/文生图/Flux2Klein _ Z-Anime _ 4KUpscale 动漫角色生成工作流_2051879363389472769.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/工作流基础系列01-Klein的单图编辑工作流-基础向讲解此工作流_2012461408067260418.json、图片生成/图生图/模糊照片修复_2042277567725572098.json、图片生成/文生图/Flux2Klein _ Z-Anime _ 4KUpscale 动漫角色生成工作流_2051879363389472769.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `ResizeImagesByShorterEdge` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.35 | 0.07 - 1 | 3 | 18% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.07 - 1，3 个样本，取值分散，一致性仅 18%
- 风险：重绘幅度 观测到 0.07，低于常用下限 0.1（）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
