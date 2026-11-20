---
name: unknown_workflow_upscale_sampler_clip_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8375
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, Label (rgthree), LoadImage, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Imagine_Only, RH_Upscale_Chooser, RandomNoise, SamplerCustomAdvanced, SaveImage, Textbox, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [平台全量/古风大头娃娃_1843625386205728770.json, 平台全量/民族风姑娘_1843902597555257345.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/古风大头娃娃_1843625386205728770.json、平台全量/民族风姑娘_1843902597555257345.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Imagine_Only`
- `RH_Upscale_Chooser`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Textbox`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Anything Everywhere` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `FeatherMask` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `ImpactGaussianBlurMask` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.65 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
