---
name: image_to_image_upscale_lora_sampler_54
type: Image To Image
frequency: 3
level: strong
coverage: 0.711
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImpactInt, ImpactSwitch, KOOK_ImageCompression, KOOK_SaveJPGImage, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2020525873752969217.json, 图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2021371911606898689.json, 图片生成/图生图/Z-IMAGE 超精致自动反推洗图+SeedVR2放大-人像效果顶级-数毛-V2-8K极致压缩版_2010172695874379777.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2020525873752969217.json、图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2021371911606898689.json、图片生成/图生图/Z-IMAGE 超精致自动反推洗图+SeedVR2放大-人像效果顶级-数毛-V2-8K极致压缩版_2010172695874379777.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImpactInt`
- `ImpactSwitch`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
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
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `CombinationText` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 0.35 | 0.35 - 0.6 | 3 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.6，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
