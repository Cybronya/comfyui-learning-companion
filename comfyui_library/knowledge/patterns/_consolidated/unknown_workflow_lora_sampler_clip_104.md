---
name: unknown_workflow_lora_sampler_clip_104
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8675
common_nodes: [Bounded Image Crop, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DF_Integer, EmptyFlux2LatentImage, Flux2Scheduler, Get Image Size, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, RandomNoise, ReferenceLatent, ResizeAndPadImage, ResizeImageMixlab, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/Flux2修图打光_2070444065451233281.json, 图片生成/图生图/产品修图打光_2077941587761524737.json, 图片生成/图生图/动感模糊编辑_2117067500327358466.json, 图片生成/图生图/电商产品修图打光无损无偏移工作流2.0_2067061200311119873.json, 图片生成/图生图/电商产品修图打光无损无偏移工作流2.0_2067170694919704578.json, 平台全量/电商产品修图打光无损无偏移工作流2.0_2053678654785376258.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2修图打光_2070444065451233281.json、图片生成/图生图/产品修图打光_2077941587761524737.json、图片生成/图生图/动感模糊编辑_2117067500327358466.json、图片生成/图生图/电商产品修图打光无损无偏移工作流2.0_2067061200311119873.json、图片生成/图生图/电商产品修图打光无损无偏移工作流2.0_2067170694919704578.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `Bounded Image Crop`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DF_Integer`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Get Image Size`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `RandomNoise`
- `ReferenceLatent`
- `ResizeAndPadImage`
- `ResizeImageMixlab`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch (4 way)` —— 5/6 个有
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `llama_cpp_parameters` —— 5/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `GrowMask` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `JoinImageWithAlpha` —— 1/6 个有
- `LayerMask: BiRefNetUltraV2` —— 1/6 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/6 个有
- `Upscale Model Loader` —— 1/6 个有
- `YUAN_TXTConvertAny` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
