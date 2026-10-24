---
name: image_to_image_sampler_clip_unet_165
type: Image To Image
frequency: 2
level: weak
coverage: 0.6335
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveFloat, Qwen3_VQA, SaveImage, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-Image+Qwen3-VL反推洗图_2021597347607748610.json, 图片生成/图生图/Z-image 自动洗图 · 图生图 1.0_1994238581453553666.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_165

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-Image+Qwen3-VL反推洗图_2021597347607748610.json、图片生成/图生图/Z-image 自动洗图 · 图生图 1.0_1994238581453553666.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SomethingToString` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 42.5 | - | 2 | 59% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.95 | - | 2 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 42.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
