---
name: unknown_workflow_controlnet_lora_sampler_30
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8695
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, Image Comparer (rgthree), KSampler (Efficient), LayerFilter: HDREffects, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAELoader, ZImageFunControlnet]
problems: []
missing: []
members: [图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json, 图片生成/图生图/一键运行：z-image 局部重绘 图像控制最新CN_2002260940475252737.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键运行：z-image cn 2.1 ，图像控制，图形对比，图生图_2002258478611722241.json、图片生成/图生图/一键运行：z-image 局部重绘 图像控制最新CN_2002260940475252737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `KSampler (Efficient)`
- `LayerFilter: HDREffects`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAELoader`
- `ZImageFunControlnet`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
