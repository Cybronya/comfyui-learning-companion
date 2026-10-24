---
name: image_to_image_upscale_lora_sampler_6
type: Image To Image
frequency: 17
level: strong
coverage: 0.902706
common_nodes: [CFGNorm, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2509 特效生成_2004005512771452930.json, 图片生成/图生图/Qwen Edit Image 2511 ——空调、风扇气流等特效生成_2006280875578757122.json, 图片生成/图生图/Qwen-Edit-2509-人像光线迁移_2060994886178000897.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_1997616377580204033.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2052216361736253441.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2052285131456557058.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2056196328450994178.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2059799208827383809.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2059802346313572353.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2059893421149614082.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2067061263775129601.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2067435409872867329.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移_2067515942933975041.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移工作流_2049696687299543041.json, 图片生成/图生图/Qwen-Edit-2509-光线迁移工作流_2052705834458730497.json, 图片生成/图生图/Qwen-Edit-2511 一致性增强_2051942635396452354.json, 图片生成/图生图/草图转kv海报_1998567957515132930.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Qwen 2509 特效生成_2004005512771452930.json、图片生成/图生图/Qwen Edit Image 2511 ——空调、风扇气流等特效生成_2006280875578757122.json、图片生成/图生图/Qwen-Edit-2509-人像光线迁移_2060994886178000897.json、图片生成/图生图/Qwen-Edit-2509-光线迁移_1997616377580204033.json、图片生成/图生图/Qwen-Edit-2509-光线迁移_2052216361736253441.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGNorm`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 14/17 个有
- `UNETLoader` —— 14/17 个有
- `LoadDiffusionModelShared //Inspire` —— 3/17 个有
- `LoadTextEncoderShared //Inspire` —— 3/17 个有
- `easy cleanGpuUsed` —— 3/17 个有
- `easy imageSize` —— 3/17 个有
- `CR Prompt Text` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `CR Seed` —— 1/17 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/17 个有
- `ImageStitch` —— 1/17 个有
- `LayerUtility: ImageReel` —— 1/17 个有
- `LayerUtility: ImageReelComposit` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 17 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（18/17 个样本）：Steps较低可能导致细节不足
