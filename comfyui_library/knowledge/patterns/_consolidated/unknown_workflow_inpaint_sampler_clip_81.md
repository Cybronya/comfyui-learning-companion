---
name: unknown_workflow_inpaint_sampler_clip_81
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.836
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, LoadImage, LoadSAM3Model, MaskToImage, ModelSamplingAuraFlow, PreviewImage, SAM3Segmentation, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image CN2.0+自动遮罩重绘_2073291532668596225.json, 图片生成/文生图/z-image遮罩重绘_2073290166688641026.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/z-image CN2.0+自动遮罩重绘_2073291532668596225.json、图片生成/文生图/z-image遮罩重绘_2073290166688641026.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoadSAM3Model`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SAM3Segmentation`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `InpaintCropImproved` —— 1/2 个有
- `InpaintStitchImproved` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `QwenImageDiffsynthControlnet` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.825 | - | 2 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.825，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
