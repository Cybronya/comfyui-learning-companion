---
name: image_to_image_controlnet_upscale_lora
type: Image To Image
frequency: 15
level: moderate
coverage: 0.744933
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleBy, ImageScaleToTotalPixels, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetUnionControlNetType, ShowText|pysssss, Text, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ET漫画转真人最好用(Qwen2511+lora+Z-image+SeedVR2)_2045180116375965698.json, 图片生成/图生图/Qwen2511+lora+Z-image二次元转真人_2011333616126664706.json, 图片生成/图生图/【楚心钟陌】Qwen+Zi，二次元转BJD娃娃，DW，CPP反推。_2008819372302802945.json, 图片生成/图生图/【楚心钟陌】动漫少女出图_2013254862045192193.json, 图片生成/图生图/【楚心钟陌】真人转动漫lora串串，个人风格参数_2017185954292834305.json, 图片生成/图生图/【楚心钟陌】真人转动漫lora串串，自定义参数_2017232745080033281.json, 图片生成/图生图/【法外狂徒】Qwen2511动漫转真人_2016905075851010050.json, 图片生成/图生图/二次元动漫转真人+高清放大- Qwen image2511+Z-image_2011000105125548033.json, 图片生成/图生图/动漫_漫画转真人2D转3D(Qwen2511+lora+Z-image+SeedVR2)_2065319867183620098.json, 图片生成/图生图/最强超真实二次元动漫转真人（Qwen2511+lora+Z-image+高清放大）_2014691519944466434.json, 图片生成/图生图/漫画转真人 高阶版 (Qwen2511+lora+Z-image+SeedVR2)_2038145192552828930.json, 图片生成/图生图/漫画转真人6.0(Qwen2511+lora+Z-image+SeedVR2)_2062795782926987266.json, 图片生成/图生图/漫画转真人，最终版_2046010999525875713.json, 平台全量/动画转写实_Qwen2511+Z-image+SeedVR2_2043866360836526082.json, 平台全量/动画转写实_Qwen2511+Z-image+SeedVR2_2043954647026634753.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/ET漫画转真人最好用(Qwen2511+lora+Z-image+SeedVR2)_2045180116375965698.json、图片生成/图生图/Qwen2511+lora+Z-image二次元转真人_2011333616126664706.json、图片生成/图生图/【楚心钟陌】Qwen+Zi，二次元转BJD娃娃，DW，CPP反推。_2008819372302802945.json、图片生成/图生图/【楚心钟陌】动漫少女出图_2013254862045192193.json、图片生成/图生图/【楚心钟陌】真人转动漫lora串串，个人风格参数_2017185954292834305.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 15 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `Text`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `LayerUtility: ImageReel` —— 14/15 个有
- `LayerUtility: ImageReelComposit` —— 14/15 个有
- `easy showAnything` —— 14/15 个有
- `ImpactExecutionOrderController` —— 13/15 个有
- `SetNode` —— 13/15 个有
- `UNETLoader` —— 13/15 个有
- `easy clearCacheAll` —— 13/15 个有
- `llama_cpp_instruct_adv` —— 10/15 个有
- `llama_cpp_model_loader` —— 10/15 个有
- `llama_cpp_unload_model` —— 10/15 个有
- `PreviewImage` —— 9/15 个有
- `Image Comparer (rgthree)` —— 8/15 个有
- `RunningHub Deepcleaner` —— 6/15 个有
- `llama_cpp_parameters` —— 6/15 个有
- `Float` —— 4/15 个有
- `GroupSwitcher` —— 4/15 个有
- `JWInteger` —— 4/15 个有
- `UnetLoaderGGUF` —— 4/15 个有
- `ModelscopeApiImageCaptionNode` —— 3/15 个有
- `Qwen3_VQA` —— 2/15 个有
- `Anything Everywhere` —— 1/15 个有
- `CompressImages` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `WD14Tagger|pysssss` —— 1/15 个有
- `string_util_StrFormat` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 0.8 - 1 | 15 | 90% |
| 采样步数 | 8 | 4 - 10 | 15 | 68% |
| Prompt 约束强度(CFG) | 1.6 | 1 - 2 | 15 | 73% |
| 采样算法 | euler | - | 15 | 73% |
| 调度器 | simple | - | 15 | 73% |
| 重绘幅度 | 0.3 | 0.1 - 0.8 | 15 | 43% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 0.8 - 1，15 个样本，取值集中（一致性 90%）
- 采样步数 中位数 8，观测区间 4 - 10，15 个样本
- Prompt 约束强度(CFG) 中位数 1.6，观测区间 1 - 2，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 73%
- 调度器 最常用 simple，15 个样本，一致性 73%
- 重绘幅度 中位数 0.3，观测区间 0.1 - 0.8，15 个样本，取值分散，一致性仅 43%
- 高发问题（33/15 个样本）：Steps较低可能导致细节不足
