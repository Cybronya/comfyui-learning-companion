---
name: unknown_workflow_upscale_sampler_clip_55
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8975
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerAdvanced, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Krea2-turbo双采+seedVR2 4K放大_2080163310426746882.json, 图片生成/文生图/Z-image-base-双重采样+SEED VR2_2016492225408012290.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Krea2-turbo双采+seedVR2 4K放大_2080163310426746882.json、图片生成/文生图/Z-image-base-双重采样+SEED VR2_2016492225408012290.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | - | 2 | 97% |
| 高度 | 1728 | - | 2 | 89% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.5 | - | 2 | 46% |
| 采样算法 | 2 | - | 2 | 50% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1728，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
