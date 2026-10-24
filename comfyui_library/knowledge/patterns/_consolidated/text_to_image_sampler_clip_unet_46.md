---
name: text_to_image_sampler_clip_unet_46
type: Text To Image
frequency: 12
level: weak
coverage: 0.80675
common_nodes: [Bjornulf_ShowFloat, Bjornulf_ShowInt, Boolean To Int [Dream], CFGGuider, CLIPLoader, CLIPTextEncode, CR Aspect Ratio, CR Prompt Text, ComfySwitchNode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize+, Int, JoinStringMulti, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, PreviewAny, PrimitiveBoolean, Qwen3VLProcessor, QwenImage21Cache, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SimpleMath+, TTP_text_mix, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, math_calculate]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein+Qwen Image2.1单图编辑｜双模型修图更稳_2108094045946990594.json, 图片生成/图生图/QWEN2.1人物服装细节换装 正面细节图电商展示_2110245461490757634.json, 图片生成/图生图/QWEN2.1人物服装细节换装 正面细节图电商展示_2110370384511066114.json, 图片生成/图生图/人物图+衣服正面图+衣服细节图==换衣-QWEN2.1_2108843476371730434.json, 图片生成/图生图/人物图加衣服正面图加衣服细节图换衣QWEN2.1 电商服装展示_2109424532212768769.json, 图片生成/图生图/人物图加衣服正面图加衣服细节图换衣QWEN2.1 电商服装展示_2109792396186836993.json, 图片生成/图生图/单图编辑-Flux2 Klein+Qwen image2.1_2107726878978170881.json, 图片生成/图生图/单纯地去水印+图案编辑+文字编辑_2103001760167190530.json, 图片生成/图生图/多指令改图提取图案-同步提示词小贴士-优化看图位置+放大_2106977875051237377.json, 图片生成/图生图/多指令改图提取图案-同步提示词小贴士-优化看图位置_2103036388051607553.json, 图片生成/图生图/多指令改图提取图案同步提示词小贴士优化看图位置加放大，图生图处理工具_2107616573891629058.json, 图片生成/图生图/多指令改图提取图案同步提示词｜优化看图位置加放大，改图神器_2107343507139682305.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_46

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein+Qwen Image2.1单图编辑｜双模型修图更稳_2108094045946990594.json、图片生成/图生图/QWEN2.1人物服装细节换装 正面细节图电商展示_2110245461490757634.json、图片生成/图生图/QWEN2.1人物服装细节换装 正面细节图电商展示_2110370384511066114.json、图片生成/图生图/人物图+衣服正面图+衣服细节图==换衣-QWEN2.1_2108843476371730434.json、图片生成/图生图/人物图加衣服正面图加衣服细节图换衣QWEN2.1 电商服装展示_2109424532212768769.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowInt`
- `Boolean To Int [Dream]`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Aspect Ratio`
- `CR Prompt Text`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize+`
- `Int`
- `JoinStringMulti`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewAny`
- `PrimitiveBoolean`
- `Qwen3VLProcessor`
- `QwenImage21Cache`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `TTP_text_mix`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `math_calculate`

**可变部分**（部分 workflow 才有）：
- `ImpactMinMax` —— 11/12 个有
- `孤海注释` —— 10/12 个有
- `ImageBatchMulti` —— 9/12 个有
- `PreviewImage` —— 9/12 个有
- `ImageFromBatch` —— 8/12 个有
- `Image Comparer (rgthree)` —— 7/12 个有
- `ImageResize+` —— 7/12 个有
- `JjkText` —— 7/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `SaveImageAdvanced` —— 7/12 个有
- `easy int` —— 7/12 个有
- `solarL_SaveImagesToZip` —— 7/12 个有
- `QwenImage21EditTextEncode_EditUtils` —— 6/12 个有
- `TextEncodeQwenImage21` —— 6/12 个有
- `easy convertAnything` —— 6/12 个有
- `YYZPack_YYZ_Image_Blank` —— 5/12 个有
- `AddMask` —— 4/12 个有
- `CropByBBoxes` —— 4/12 个有
- `DrawMaskOnImage` —— 4/12 个有
- `INPAINT_MaskBoundingBox` —— 4/12 个有
- `InvertMask` —— 4/12 个有
- `PrimitiveBoundingBox` —— 4/12 个有
- `Sa2VANodeTpl` —— 4/12 个有
- `ImageScaleBy` —— 3/12 个有
- `SeedVR2LoadDiTModel` —— 3/12 个有
- `SeedVR2LoadVAEModel` —— 3/12 个有
- `SeedVR2VideoUpscaler` —— 3/12 个有
- `TTP_Image_Assy` —— 3/12 个有
- `TTP_Image_Tile_Batch` —— 3/12 个有
- `TTP_Tile_image_size` —— 3/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 12 | 19% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 12 | 43% |
| 采样算法 | er_sde | - | 12 | 58% |
| 调度器 | beta | - | 12 | 58% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 1024 | 12 | 2% |
| 高度 | 80 | 80 - 1024 | 12 | 2% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，12 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，12 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 er_sde，12 个样本，一致性 58%
- 调度器 最常用 beta，12 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，12 个样本，取值分散，一致性仅 2%
- 高度 中位数 80，观测区间 80 - 1024，12 个样本，取值分散，一致性仅 2%
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
