---
name: unknown_workflow_controlnet_upscale_sampler_3
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.773333
common_nodes: [Anything Everywhere, ApplyPulidFlux, BasicGuider, BasicScheduler, BiRefNet_Hugo, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, ExpressionEditor, Fast Groups Bypasser (rgthree), FluxGuidance, GridImageSplitter, GrowMask, Image Overlay, ImageFromBatch+, ImageResize+, ImageUpscaleWithModel, InvertMask, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, Prompts Everywhere, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SeargeIntegerConstant, ShowText|pysssss, TextCombinerTwo, UltimateSDUpscale, UnetLoaderGGUF, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageInsetCrop, easy positive, easy seed]
problems: []
missing: []
members: [图片生成/图生图/【AI由北】人物一致性（电商统一模特）_1917191770050854913.json, 图片生成/图生图/自定义人物【一致性】_1919046530878345217.json, 数字人/数字人/人物一致性(生成人物角色素材集)  训练Lora_1968573520374583297.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【AI由北】人物一致性（电商统一模特）_1917191770050854913.json、图片生成/图生图/自定义人物【一致性】_1919046530878345217.json、数字人/数字人/人物一致性(生成人物角色素材集)  训练Lora_1968573520374583297.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `BiRefNet_Hugo`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `ExpressionEditor`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GridImageSplitter`
- `GrowMask`
- `Image Overlay`
- `ImageFromBatch+`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `InvertMask`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `Prompts Everywhere`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeargeIntegerConstant`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `UltimateSDUpscale`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageInsetCrop`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有
- `Note _O` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.85 | 0.85 - 0.85 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.85，观测区间 0.85 - 0.85，3 个样本，取值集中（一致性 100%）
