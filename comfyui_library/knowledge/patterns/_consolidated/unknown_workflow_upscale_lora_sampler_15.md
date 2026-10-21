---
name: unknown_workflow_upscale_lora_sampler_15
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.81
common_nodes: [CFGGuider, CLIPLoader, CLIPLoaderGGUF, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, GetNode, INTConstant, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSamplerAdvanced, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize]
problems: []
missing: []
members: [图片生成/文生图/Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793.json, 图片生成/文生图/Zimage+Klein三采极致人像写真提示词扩写文生图工作流（4K高清出图）_2064280103672176641.json, 图片生成/文生图/Zimage+Klein三采极致人像写真文生图（4K高清出图）_2064248513470484481.json, 图片生成/文生图/Zimage双采+Flux2-Klein三采极致人像写真工作流，还原真实皮肤质感！_2060660673239150594.json, 图片生成/文生图/Zimage双采+Flux2-Klein三采极致人像写真工作流，还原真实皮肤质感！_2066864057151483906.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793.json、图片生成/文生图/Zimage+Klein三采极致人像写真提示词扩写文生图工作流（4K高清出图）_2064280103672176641.json、图片生成/文生图/Zimage+Klein三采极致人像写真文生图（4K高清出图）_2064248513470484481.json、图片生成/文生图/Zimage双采+Flux2-Klein三采极致人像写真工作流，还原真实皮肤质感！_2060660673239150594.json、图片生成/文生图/Zimage双采+Flux2-Klein三采极致人像写真工作流，还原真实皮肤质感！_2066864057151483906.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `KSamplerSelect`
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
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `LCSColorAnchor` —— 4/5 个有
- `LCSLoadData` —— 4/5 个有
- `LCSSharpnessCalibrate` —— 4/5 个有
- `LCSSharpnessIntervene` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `llama_cpp_instruct_adv` —— 4/5 个有
- `llama_cpp_model_loader` —— 4/5 个有
- `Any Switch (rgthree)` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `llama_cpp_parameters` —— 3/5 个有
- `Label (rgthree)` —— 2/5 个有
- `MemoryCleaner` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `CannyEdgePreprocessor` —— 1/5 个有
- `DWPreprocessor` —— 1/5 个有
- `DapaoImageCompressionNode` —— 1/5 个有
- `HEDPreprocessor` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `ModelPatchLoader` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `QwenImageDiffsynthControlnet` —— 1/5 个有
- `easy seed` —— 1/5 个有
- `图像缩放范围孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 1.15 | 1.15 - 3 | 5 | 51% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 80% |
| 重绘幅度 | beta | - | 5 | 80% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1536 | 1536 - 1536 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1.15，观测区间 1.15 - 3，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 80%
- 重绘幅度 最常用 beta，5 个样本，一致性 80%
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，5 个样本，取值集中（一致性 100%）
