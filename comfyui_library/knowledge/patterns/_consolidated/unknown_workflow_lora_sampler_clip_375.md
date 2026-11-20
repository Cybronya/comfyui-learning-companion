---
name: unknown_workflow_lora_sampler_clip_375
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8795
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Image Input Switch, CR String To Number, CheckpointLoaderSimple, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, KSamplerSelect, Label (rgthree), LayerUtility: LoadVQAModel, LayerUtility: VQAPrompt, LoadImage, LoraLoader, MaskToSEGS, MiniCPM_VQA, ModelSamplingFlux, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SEGSPreview, SamplerCustomAdvanced, SaveImage, SeargeIntegerConstant, ShowText|pysssss, StringConstant, StyleModelApplyAdvanced, StyleModelLoader, Switch any [Crystools], TextCombinerTwo, VAEDecode]
problems: []
missing: []
members: [平台全量/新年专属红包封面_1882725063253282818.json, 平台全量/霍格沃兹圣诞夜限定人偶_1867511972588584961.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_375

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/新年专属红包封面_1882725063253282818.json、平台全量/霍格沃兹圣诞夜限定人偶_1867511972588584961.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Image Input Switch`
- `CR String To Number`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerUtility: LoadVQAModel`
- `LayerUtility: VQAPrompt`
- `LoadImage`
- `LoraLoader`
- `MaskToSEGS`
- `MiniCPM_VQA`
- `ModelSamplingFlux`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeargeIntegerConstant`
- `ShowText|pysssss`
- `StringConstant`
- `StyleModelApplyAdvanced`
- `StyleModelLoader`
- `Switch any [Crystools]`
- `TextCombinerTwo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ExpressionEditor` —— 1/2 个有
- `FluxResolutionNode` —— 1/2 个有
- `HfImageToRGB` —— 1/2 个有
- `Image Overlay` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LayerColor: Brightness & Contrast` —— 1/2 个有
- `SDXLAspectRatioSelector` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 832 | - | 2 | 100% |
| 高度 | 1216 | - | 2 | 100% |
| LoRA 模型强度 | 0.585 | - | 2 | 89% |
| LoRA 文本强度 | 0.825 | - | 2 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 832，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.585，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.825，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
