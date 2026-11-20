---
name: image_to_image_upscale_sampler_clip_19
type: Image To Image
frequency: 6
level: strong
coverage: 0.7135
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), INTConstant, Image Comparer (rgthree), Image Filter Adjustments, ImageScaleBy, ImpactInt, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, PrimitiveFloat, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SomethingToString, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/(电商工具流)Z image-turbo极致写实反推单图洗图可选直出4K_2032695868960280577.json, 图片生成/文生图/Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016207552249339905.json, 图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json, 图片生成/文生图/Z-Image-Base大合集+文生图+洗图_2016472904732516353.json, 图片生成/文生图/☃️开源王者 Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016340251035308033.json, 视频生成/文生视频/Z Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016769190719393793.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/(电商工具流)Z image-turbo极致写实反推单图洗图可选直出4K_2032695868960280577.json、图片生成/文生图/Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016207552249339905.json、图片生成/文生图/Z-Image Base 极致写实+文生图_图生图洗图 SeedVR2.5 + TTP 高清放大_2016741486603276289.json、图片生成/文生图/Z-Image-Base大合集+文生图+洗图_2016472904732516353.json、图片生成/文生图/☃️开源王者 Z-IMAGE-BASE大合集支持文生图 _ 图片洗图_2016340251035308033.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `ImageScaleBy`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Qwen3_VQA` —— 5/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `ImpactInversedSwitch` —— 1/6 个有
- `KOOK_ImageCompression` —— 1/6 个有
- `KOOK_SaveJPGImage` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有
- `easy int` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有
- `llama_cpp_parameters` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 6 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 6 | 100% |
| 采样算法 | res_multistep | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 6 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，6 个样本，取值集中（一致性 95%）
