---
name: text_to_image_upscale_sampler_clip_32
type: Text To Image
frequency: 3
level: strong
coverage: 0.803
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Float, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE+ERNIE国风双采样文生图_2050516029037658113.json, 图片生成/文生图/四格美女欲望图片（百度ERNIE+千问混合双采）_2045732738967281666.json, 图片生成/文生图/百度ERNIE+千问混合双采_2045015614472851458.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE+ERNIE国风双采样文生图_2050516029037658113.json、图片生成/文生图/四格美女欲望图片（百度ERNIE+千问混合双采）_2045732738967281666.json、图片生成/文生图/百度ERNIE+千问混合双采_2045015614472851458.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
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
- `easy int`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RunningHub Deepcleaner` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 720 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |
| 采样步数 | 9 | 8 - 9 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 3 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，观测区间 8 - 9，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，3 个样本
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
