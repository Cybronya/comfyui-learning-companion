---
name: unknown_workflow_upscale_lora_sampler_3
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.88065
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/krea2 image to image_+flux2 klein三采极_James008##_2100007875061051393.json, 图片生成/图生图/krea2_image_to_image_+flux2_klein三采极_James008##_2100515839752626177.json, 图片生成/图生图/万能无损4K高清放大，场景物体细节，人像增加皮肤细节真实感_2086011194258841602.json, 图片生成/图生图/万能无损4K高清放大，场景物体细节，人像增加皮肤细节真实感_2086271978704560130.json, 图片生成/图生图/产品精修，增加细节，高清细节_2067213726100578306.json, 图片生成/图生图/产品精修，增加细节，高清细节_2085916570555080706.json, 图片生成/图生图/产品精修，增加细节，高清细节_2085930638724648962.json, 图片生成/图生图/人像增加皮肤细节真实感场景物体细节万能无损4K高清放大_2085921211795722242.json, 图片生成/图生图/人像增加皮肤细节真实感场景物体细节万能无损4K高清放大_2085932013500059650.json, 图片生成/图生图/高清发大工作流_2078415743611396097.json, 图片生成/图生图/高清放大修复2-8K_2084837240974430210.json, 图片生成/图生图/高清放大修复2-8K_2084900430831771650.json, 图片生成/图生图/高清放大修复2-8K_2088523441623355394.json, 图片生成/图生图/高清放大，无损增加细节_2081647850538229762.json, 图片生成/图生图/高清放大，无损增加细节_2094235046789083137.json, 图片生成/图生图/高清细节增加细节产品精修图生图模特产品展示_2085918579534417921.json, 图片生成/图生图/高清细节增加细节产品精修图生图模特产品展示_2085931972576235522.json, 图片生成/文生图/Zimage+Klein三采极致人像写真文生图（4K高清出图）_2064248513470484481.json, 图片生成/文生图/Zimage双采+Flux2-Klein三采极致人像写真工作流，还原真实皮肤质感！_2060660673239150594.json, 图片生成/文生图/Zimage双采+Flux2-Klein三采极致人像写真工作流，还原真实皮肤质感！_2066864057151483906.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/krea2 image to image_+flux2 klein三采极_James008##_2100007875061051393.json、图片生成/图生图/krea2_image_to_image_+flux2_klein三采极_James008##_2100515839752626177.json、图片生成/图生图/万能无损4K高清放大，场景物体细节，人像增加皮肤细节真实感_2086011194258841602.json、图片生成/图生图/万能无损4K高清放大，场景物体细节，人像增加皮肤细节真实感_2086271978704560130.json、图片生成/图生图/产品精修，增加细节，高清细节_2067213726100578306.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
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
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 19/20 个有
- `LCSColorAnchor` —— 18/20 个有
- `LCSLoadData` —— 18/20 个有
- `LCSSharpnessCalibrate` —— 18/20 个有
- `LCSSharpnessIntervene` —— 18/20 个有
- `PrimitiveFloat` —— 8/20 个有
- `Fast Groups Bypasser (rgthree)` —— 5/20 个有
- `KSamplerAdvanced` —— 5/20 个有
- `PreviewImage` —— 5/20 个有
- `Label (rgthree)` —— 4/20 个有
- `CLIPLoaderGGUF` —— 3/20 个有
- `CR Text` —— 3/20 个有
- `EmptyLatentImage` —— 3/20 个有
- `INTConstant` —— 3/20 个有
- `ModelSamplingAuraFlow` —— 3/20 个有
- `TTResolutionSelector` —— 3/20 个有
- `AILab_QwenVL` —— 2/20 个有
- `Any Switch (rgthree)` —— 2/20 个有
- `BasicGuider` —— 2/20 个有
- `BasicScheduler` —— 2/20 个有
- `ImageUpscaleWithModel` —— 2/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/20 个有
- `LoraLoader` —— 2/20 个有
- `PrimitiveInt` —— 2/20 个有
- `ShowText|pysssss` —— 2/20 个有
- `UpscaleModelLoader` —— 2/20 个有
- `VAEDecodeTiled` —— 2/20 个有
- `VAEEncodeTiled` —— 2/20 个有
- `easy imageColorMatch` —— 2/20 个有
- `llama_cpp_instruct_adv` —— 2/20 个有
- `llama_cpp_model_loader` —— 2/20 个有
- `llama_cpp_parameters` —— 2/20 个有
- `EmptyImage` —— 1/20 个有
- `MemoryCleaner` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 1.15 | 1.15 - 10 | 5 | 8% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 100% |
| 重绘幅度 | beta | - | 5 | 60% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 1.15，观测区间 1.15 - 10，5 个样本，取值分散，一致性仅 8%
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 100%
- 重绘幅度 最常用 beta，5 个样本，一致性 60%
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
