---
name: text_to_image_upscale_lora_sampler_85
type: Text To Image
frequency: 3
level: strong
coverage: 0.890667
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, ComfyUI-Krea2T-Enhancer, EmptyLatentImage, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JjkText, JoinStringMulti, KOOK_SaveJPGImage, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RunningHub Deepcleaner, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy positive, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/K2-90SuYing图生图洗图｜小红书抖音通用 人像写真美少女出片_2104078434745020417.json, 图片生成/图生图/K2-90SuYing网络图洗图 小红书抖音美女人像写真化_2104458649627348994.json, 图片生成/文生图/K2超现实感文生图，手机拍摄风格90SuYing写实网感图生成方案_2103886432678010881.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/K2-90SuYing图生图洗图｜小红书抖音通用 人像写真美少女出片_2104078434745020417.json、图片生成/图生图/K2-90SuYing网络图洗图 小红书抖音美女人像写真化_2104458649627348994.json、图片生成/文生图/K2超现实感文生图，手机拍摄风格90SuYing写实网感图生成方案_2103886432678010881.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyUI-Krea2T-Enhancer`
- `EmptyLatentImage`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `JoinStringMulti`
- `KOOK_SaveJPGImage`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RunningHub Deepcleaner`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy positive`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AddNoise` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LatentUpscaleBy` —— 2/3 个有
- `LayerColor: AutoAdjustV2` —— 2/3 个有
- `LayerColor: Exposure` —— 2/3 个有
- `LayerFilter: SoftLight` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `easy imageColorMatch` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
