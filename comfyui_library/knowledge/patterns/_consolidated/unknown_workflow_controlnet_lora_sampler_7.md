---
name: unknown_workflow_controlnet_lora_sampler_7
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9534
common_nodes: [AIO_Preprocessor, ApplyFBCacheOnModel, BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, FluxGuidance, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/FLUX ControlNet-Union-Pro-2.0_1912852228594462721.json, 图片生成/图生图/FLUX Kontext 9图编辑 应用ControlNet_2053760650077327362.json, 图片生成/图生图/FLUX_ControlNet-Union-Pro-2.0_2114312388890677250.json, 图片生成/图生图/Flux控制(FLUX ControlNet-Union-Pro-2.0 )_1992796300076969986.json, 图片生成/图生图/Flux控制加放大_2008451007621107713.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX ControlNet-Union-Pro-2.0_1912852228594462721.json、图片生成/图生图/FLUX Kontext 9图编辑 应用ControlNet_2053760650077327362.json、图片生成/图生图/FLUX_ControlNet-Union-Pro-2.0_2114312388890677250.json、图片生成/图生图/Flux控制(FLUX ControlNet-Union-Pro-2.0 )_1992796300076969986.json、图片生成/图生图/Flux控制加放大_2008451007621107713.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFBCacheOnModel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/5 个有
- `JjkShowText` —— 2/5 个有
- `LayerMask: LoadFlorence2Model` —— 2/5 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/5 个有
- `String` —— 2/5 个有
- `Text Concatenate` —— 2/5 个有
- `CLIPTextEncodeFlux` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `RHUploadZip` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| ControlNet 权重 | 0.8 | 0.8 - 1 | 5 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.8 - 1，5 个样本，取值集中（一致性 90%）
