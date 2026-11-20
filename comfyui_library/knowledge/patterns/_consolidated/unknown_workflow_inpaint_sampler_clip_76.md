---
name: unknown_workflow_inpaint_sampler_clip_76
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, EmptySD3LatentImage, Flux2Scheduler, GrowMaskWithBlur, ImageResize+, ImageScaleToTotalPixels, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSamplerSelect, LayerMask: MaskGrow, LayerMask: SegmentAnythingUltra V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, easy a1111Loader, easy fullkSampler, easy imageSize, easy instantIDApplyADV, easy pipeOut]
problems: []
missing: []
members: [图片生成/图生图/换衣换脸_2084979557567909890.json, 图片生成/图生图/换衣换脸换姿势背景-2_2084273098009964545.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换衣换脸_2084979557567909890.json、图片生成/图生图/换衣换脸换姿势背景-2_2084273098009964545.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptySD3LatentImage`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy a1111Loader`
- `easy fullkSampler`
- `easy imageSize`
- `easy instantIDApplyADV`
- `easy pipeOut`

**可变部分**（部分 workflow 才有）：
- `CR Seed` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `Qwen3VL_Chat` —— 1/2 个有
- `ttN concat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
