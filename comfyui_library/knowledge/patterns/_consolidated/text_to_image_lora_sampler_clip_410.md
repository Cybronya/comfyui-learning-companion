---
name: text_to_image_lora_sampler_clip_410
type: Text To Image
frequency: 5
level: strong
coverage: 0.7728
common_nodes: [AIO_Preprocessor, Anything Everywhere3, BatchImagesNode, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), FastGroupsBypassSwitch, GetNode, Image Comparer (rgthree), ImageBlend, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, ResolutionSelector, SaveImage, SetNode, ShowText|pysssss, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json, 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json, 图片生成/文生图/Qwen Image 2.1工作流合集｜文生图图生图多场景全家桶_2110683569914998785.json, 图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json, 图片生成/文生图/怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_410

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json、图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json、图片生成/文生图/Qwen Image 2.1工作流合集｜文生图图生图多场景全家桶_2110683569914998785.json、图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json、图片生成/文生图/怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FastGroupsBypassSwitch`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageBlend`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 4/5 个有
- `DWPreprocessor` —— 4/5 个有
- `DepthAnythingPreprocessor` —— 4/5 个有
- `Qwen3VL_Advanced` —— 4/5 个有
- `QwenImage21Cache` —— 3/5 个有
- `LoraLoaderBypassModelOnly` —— 2/5 个有
- `easy sleep` —— 2/5 个有
- `BlockifyMask` —— 1/5 个有
- `DepthAnythingV2Preprocessor` —— 1/5 个有
- `DrawMaskOnImage` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LayerMask: BiRefNetUltraV2` —— 1/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/5 个有
- `LayerUtility: ImageBlend` —— 1/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
