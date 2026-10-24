---
name: unknown_workflow_upscale_lora_clip_3
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.695125
common_nodes: [CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScaleBy, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/图生图/Z-Image-图生图+文生图_2041891186994057217.json, 图片生成/图生图/Z-image-参考图生图4K放大_2044596969414332417.json, 图片生成/图生图/Z-image参考图生图4K放大（完美适用电商模特场景）_2047224124094816258.json, 图片生成/图生图/ZImage超写实人像V2_2065813680138313729.json, 图片生成/文生图/Z-Image-超写实人像V2-zip_2075615683794268161.json, 图片生成/文生图/Z-Image-超写实人像V2_2060965342553399297.json, 图片生成/文生图/Z-Image-超写实人像_2039159264505237506.json, 图片生成/文生图/Z-image-提示词润化4K直出_2042829918739898369.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_3

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-Image-图生图+文生图_2041891186994057217.json、图片生成/图生图/Z-image-参考图生图4K放大_2044596969414332417.json、图片生成/图生图/Z-image参考图生图4K放大（完美适用电商模特场景）_2047224124094816258.json、图片生成/图生图/ZImage超写实人像V2_2065813680138313729.json、图片生成/文生图/Z-Image-超写实人像V2-zip_2075615683794268161.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 5/8 个有
- `CR Text` —— 5/8 个有
- `EmptyLatentImage` —— 5/8 个有
- `Int` —— 5/8 个有
- `KSamplerAdvanced` —— 5/8 个有
- `RunningHub Deepcleaner` —— 5/8 个有
- `VAELoader` —— 5/8 个有
- `easy int` —— 5/8 个有
- `LayerUtility: PurgeVRAM V2` —— 4/8 个有
- `CLIPLoader` —— 3/8 个有
- `CheckpointLoaderSimple` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `KSampler` —— 3/8 个有
- `MuyeSizeSelector` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `TextInput_` —— 3/8 个有
- `easy getNode` —— 3/8 个有
- `easy seed` —— 3/8 个有
- `easy setNode` —— 3/8 个有
- `llama_cpp_parameters` —— 3/8 个有
- `CLIPLoaderGGUF` —— 2/8 个有
- `Text Concatenate (JPS)` —— 2/8 个有
- `HAIGC_SaveImagesToZip` —— 1/8 个有
- `easy saveText` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 62% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 8 | 57% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 8 | 62% |
| 重绘幅度 | simple | - | 8 | 62% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1536 | 1536 - 1536 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 62%
- 重绘幅度 最常用 simple，8 个样本，一致性 62%
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，5 个样本，取值集中（一致性 100%）
