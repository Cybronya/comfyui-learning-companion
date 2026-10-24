---
name: image_to_image_sampler_clip_unet_180
type: Image To Image
frequency: 2
level: weak
coverage: 0.63
common_nodes: [CLIPLoader, CLIPTextEncode, Image Filter Adjustments, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveFloat, SaveImage, ShowText|pysssss, SomethingToString, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image-Base 文图生图 自动反推洗图+全节点注释_2055587271084134401.json, 图片生成/文生图/🐱Z-image-base 文生图 图生图工作流合集 @言灵ru_2017219132005031938.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_180

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base 文图生图 自动反推洗图+全节点注释_2055587271084134401.json、图片生成/文生图/🐱Z-image-base 文生图 图生图工作流合集 @言灵ru_2017219132005031938.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Filter Adjustments`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveFloat`
- `SaveImage`
- `ShowText|pysssss`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.95 | - | 2 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
