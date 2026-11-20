---
name: unknown_workflow_upscale_lora_sampler_103
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8715
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSamplerAdvanced, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809.json, 图片生成/文生图/Z双采+klein，V1_2041770513898409985.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_103

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809.json、图片生成/文生图/Z双采+klein，V1_2041770513898409985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CannyEdgePreprocessor` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `llama_cpp_unload_model` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 2 | 80% |
| 采样算法 | 1.25 | - | 2 | 80% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | beta57 | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 beta57，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
