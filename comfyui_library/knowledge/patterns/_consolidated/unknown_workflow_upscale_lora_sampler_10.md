---
name: unknown_workflow_upscale_lora_sampler_10
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.770786
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageSharpen, KSamplerAdvanced, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z Image Extreme Asthetics ControlNet (极致人体CN版）_2075071970105970689.json, 图片生成/图生图/万能图像生成器_2029233719600484353.json, 图片生成/图生图/心然·寻源-Z-image双采图像生成器_2091343877964910593.json, 图片生成/文生图/2029783421530148865.json, 图片生成/文生图/2031542926039326722.json, 图片生成/文生图/Z Image #187 #123 （极致人体文生图）文生图 16_9_2111065680140398593.json, 图片生成/文生图/Z Image Air 空灵感 8K 直出_2075064355628081154.json, 图片生成/文生图/Z Image Air 空灵感 8K 直出_2076658759031681026.json, 图片生成/文生图/Z Image 极致人体文生图 Extreme Asthetics Text to Image_2075065299652669442.json, 图片生成/文生图/Z+Image+Air+空灵感+8K+直出_2080464179739324418.json, 图片生成/文生图/Z+Image+Air+空灵感_2081903340920852482.json, 图片生成/文生图/Z+Klein+放大自动文生图图像_2029138513035268097.json, 图片生成/文生图/Z-Image双采样+Fluax2-klein修复-高清直出_2036717396722978818.json, 图片生成/文生图/文生图 角色生成 仙侠 古风 现代（超清）_2100600038656405506.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Z Image Extreme Asthetics ControlNet (极致人体CN版）_2075071970105970689.json、图片生成/图生图/万能图像生成器_2029233719600484353.json、图片生成/图生图/心然·寻源-Z-image双采图像生成器_2091343877964910593.json、图片生成/文生图/2029783421530148865.json、图片生成/文生图/2031542926039326722.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 10/14 个有
- `LayerUtility: PurgeVRAM V2` —— 10/14 个有
- `PreviewImage` —— 9/14 个有
- `ShowText|pysssss` —— 9/14 个有
- `PrimitiveInt` —— 8/14 个有
- `PrimitiveStringMultiline` —— 8/14 个有
- `StringReplace` —— 7/14 个有
- `CR Text` —— 6/14 个有
- `INTConstant` —— 6/14 个有
- `Int` —— 6/14 个有
- `Label (rgthree)` —— 5/14 个有
- `LoadImage` —— 5/14 个有
- `AILab_QwenVL` —— 4/14 个有
- `llama_cpp_instruct_adv` —— 4/14 个有
- `llama_cpp_model_loader` —— 4/14 个有
- `CLIPLoaderGGUF` —— 3/14 个有
- `GetNode` —— 2/14 个有
- `RH_LLMAPI_Pro_Node` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `AIO_Preprocessor` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `ModelPatchLoader` —— 1/14 个有
- `PreviewAny` —— 1/14 个有
- `Reroute (rgthree)` —— 1/14 个有
- `Text Multiline` —— 1/14 个有
- `ZImageFunControlnet` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 57% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 14 | 100% |
| 采样算法 | 1 | 1 - 3 | 14 | 55% |
| 调度器 | euler | - | 14 | 100% |
| 重绘幅度 | simple | - | 14 | 100% |
| 宽度 | 1052 | 1024 - 1920 | 14 | 77% |
| 高度 | 1536 | 1024 - 2584 | 14 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，14 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 3，14 个样本
- 调度器 最常用 euler，14 个样本，一致性 100%
- 重绘幅度 最常用 simple，14 个样本，一致性 100%
- 宽度 中位数 1052，观测区间 1024 - 1920，14 个样本
- 高度 中位数 1536，观测区间 1024 - 2584，14 个样本
