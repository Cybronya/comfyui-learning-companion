---
name: text_to_image_controlnet_upscale_latent_upscale_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.541667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Prompt Text, CannyEdgePreprocessor, ConditioningZeroOut, EmptyLatentImage, GetNode, Image Comparer (rgthree), KSampler, LatentUpscaleBy, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, ModelPatchLoader, PreviewImage, Qwen3_VQA, QwenImageDiffsynthControlnet, SaveImage, SetNode, Text Concatenate, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy imagePixelPerfect, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-imageControlNet提示词反推+控制2.0ENGENG⭐️⭐️⭐️⭐️⭐️洗图超写实—_2087110421571526657.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️洗图超写实——Z-image ControlNet控制2.0 + 提示词反推_2001440598282432513.json, 图片生成/图生图/【109】Z-image ControlNet控制2.0 + 提示词反推_2000772272614932481.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_latent_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-imageControlNet提示词反推+控制2.0ENGENG⭐️⭐️⭐️⭐️⭐️洗图超写实—_2087110421571526657.json、图片生成/图生图/⭐️⭐️⭐️⭐️⭐️洗图超写实——Z-image ControlNet控制2.0 + 提示词反推_2001440598282432513.json、图片生成/图生图/【109】Z-image ControlNet控制2.0 + 提示词反推_2000772272614932481.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CannyEdgePreprocessor`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LatentUpscaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `Qwen3_VQA`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SetNode`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy imagePixelPerfect`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `SDXLPromptStyler` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `UltimateSDUpscale` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | ddim_uniform | - | 3 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 ddim_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
