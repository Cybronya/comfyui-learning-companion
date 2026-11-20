---
name: image_to_image_upscale_lora_sampler_85
type: Image To Image
frequency: 3
level: moderate
coverage: 0.862333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [平台全量/Seedvr2+Z-image极致摄影优化放大 2026 3.26_2002001798711898113.json, "平台全量/ttp放大,效果不错_1924861233793540098.json", 平台全量/阮旭东_TTP高清放大修复工作流v1.0（20250927更新）_1961764280959963137.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Seedvr2+Z-image极致摄影优化放大 2026 3.26_2002001798711898113.json、平台全量/ttp放大,效果不错_1924861233793540098.json、平台全量/阮旭东_TTP高清放大修复工作流v1.0（20250927更新）_1961764280959963137.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ImageListToImageBatch` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `ImpactImageBatchToImageList` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageListToBatch+` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 9 - 30 | 3 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.2 | 0.2 - 0.3 | 3 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 9 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 0.3，3 个样本
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
