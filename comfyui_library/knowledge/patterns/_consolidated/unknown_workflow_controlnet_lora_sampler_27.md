---
name: unknown_workflow_controlnet_lora_sampler_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.903
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, Bjornulf_TextToStringAndSeed, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, ImpactSwitch, JWInteger, KSampler, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, OpenposePreprocessor, PDIMAGE_LongerSize, PathchSageAttentionKJ, PreviewImage, PulidFluxEvaClipLoader, PulidFluxFaceDetector, PulidFluxInsightFaceLoader, PulidFluxModelLoader, PulidFluxOptions, RHHiddenNodes, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, ShowText, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/【电商】Krea+Wan2.2模特洗图 v2_1953961104475246594.json, 图片生成/图生图/【电商】Krea+Wan2.2模特洗图_1953381507912138753.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【电商】Krea+Wan2.2模特洗图 v2_1953961104475246594.json、图片生成/图生图/【电商】Krea+Wan2.2模特洗图_1953381507912138753.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_TextToStringAndSeed`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImpactSwitch`
- `JWInteger`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `OpenposePreprocessor`
- `PDIMAGE_LongerSize`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxFaceDetector`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `PulidFluxOptions`
- `RHHiddenNodes`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `TeaCache` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 50% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
