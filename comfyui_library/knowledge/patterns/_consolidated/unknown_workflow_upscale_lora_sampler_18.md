---
name: unknown_workflow_upscale_lora_sampler_18
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.872818
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, GetImageSize, ImageResize+, ImageScaleBy, KSamplerSelect, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux图像放大+细节修复（全景图专用）_2083021178624634882.json, 图片生成/图生图/Klein 角色设定表（四分视图）_2083580028809469953.json, 图片生成/图生图/Klein 资产库角色三视图 双人三视图合并一次性高清生成_2086308751707033602.json, 图片生成/图生图/Klein 资产库角色三视图_2083549208208039938.json, 图片生成/图生图/Klein 资产库角色三视图_2083814112735354882.json, 图片生成/图生图/Klein_资产库角色三视图_2097167088514326529.json, 图片生成/图生图/Klein_资产库角色三视图_2097506450976366593.json, 图片生成/图生图/RH  ComfyUI × Flux-2-Klein-9B：一键无缝扩展图像边界_2077592494979772417.json, 图片生成/图生图/Zimage+Klein三采极致人像写真图生图工作流（4K高清出图）_2064257524517400578.json, 图片生成/文生图/Z-IMAGE 双采高质量出图 +CONTRALNET控制 +kelin复制修复+seedvr2放大_2077403190911393793.json, 图片生成/文生图/Zimage+Klein三采极致人像写真提示词扩写文生图工作流（4K高清出图）_2064280103672176641.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux图像放大+细节修复（全景图专用）_2083021178624634882.json、图片生成/图生图/Klein 角色设定表（四分视图）_2083580028809469953.json、图片生成/图生图/Klein 资产库角色三视图 双人三视图合并一次性高清生成_2086308751707033602.json、图片生成/图生图/Klein 资产库角色三视图_2083549208208039938.json、图片生成/图生图/Klein 资产库角色三视图_2083814112735354882.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
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
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `LayerUtility: PurgeVRAM` —— 8/11 个有
- `BasicScheduler` —— 6/11 个有
- `JWImageResizeByLongerSide` —— 6/11 个有
- `ColorMatch` —— 5/11 个有
- `ConditioningZeroOut` —— 5/11 个有
- `Flux2Scheduler` —— 5/11 个有
- `ImageConcatMulti` —— 5/11 个有
- `ImageScaleToTotalPixels` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `GetNode` —— 4/11 个有
- `SetNode` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `CLIPLoaderGGUF` —— 3/11 个有
- `EmptyLatentImage` —— 3/11 个有
- `INTConstant` —— 3/11 个有
- `KSamplerAdvanced` —— 3/11 个有
- `LCSColorAnchor` —— 3/11 个有
- `LCSLoadData` —— 3/11 个有
- `LCSSharpnessCalibrate` —— 3/11 个有
- `LCSSharpnessIntervene` —— 3/11 个有
- `ModelSamplingAuraFlow` —— 3/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `TTResolutionSelector` —— 3/11 个有
- `llama_cpp_instruct_adv` —— 3/11 个有
- `llama_cpp_model_loader` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `easy seed` —— 2/11 个有
- `llama_cpp_parameters` —— 2/11 个有
- `AIO_Preprocessor` —— 1/11 个有
- `Any Switch (rgthree)` —— 1/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `CannyEdgePreprocessor` —— 1/11 个有
- `DWPreprocessor` —— 1/11 个有
- `DapaoImageCompressionNode` —— 1/11 个有
- `DrawMaskOnImage` —— 1/11 个有
- `HEDPreprocessor` —— 1/11 个有
- `ImageConcanate` —— 1/11 个有
- `ImagePadForOutpaint` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `LayerUtility: ImageReel` —— 1/11 个有
- `LayerUtility: ImageReelComposit` —— 1/11 个有
- `MemoryCleaner` —— 1/11 个有
- `ModelPatchLoader` —— 1/11 个有
- `PlaySound|pysssss` —— 1/11 个有
- `QwenImageDiffsynthControlnet` —— 1/11 个有
- `图像缩放范围孤海` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 1.15 | 1.15 - 3 | 3 | 51% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 67% |
| 重绘幅度 | beta | - | 3 | 67% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1.15，观测区间 1.15 - 3，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 67%
- 重绘幅度 最常用 beta，3 个样本，一致性 67%
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
