---
name: image_to_image_inpaint_sampler_clip_7
type: Image To Image
frequency: 2
level: weak
coverage: 0.975
common_nodes: [CLIPLoader, CLIPTextEncode, DifferentialDiffusion, GrowMaskWithBlur, InpaintModelConditioning, KSampler, LoadImage, ReferenceLatent, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/62.tonnie-Zimage局部重绘（效果不好，不能用）_2009416814379409410.json, 图片生成/图生图/63.tonnie-Zimage扩图_2009421950585671682.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/62.tonnie-Zimage局部重绘（效果不好，不能用）_2009416814379409410.json、图片生成/图生图/63.tonnie-Zimage扩图_2009421950585671682.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `GrowMaskWithBlur`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `INPAINT_InpaintWithModel` —— 1/2 个有
- `INPAINT_LoadInpaintModel` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewAny` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.5 | - | 2 | 95% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.825 | - | 2 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.5，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.825，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
