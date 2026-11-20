---
name: text_to_image_sampler_clip_unet_26
type: Text To Image
frequency: 16
level: weak
coverage: 0.814
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, PreviewImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json, 图片生成/图生图/Qwen2.1双图版｜Flux2Klein自动生成图｜双参考融合效果更自然_2102585557531578370.json, 图片生成/图生图/qwen image2.1短剧漫剧三视图｜写实人物角色批量出图_2103704294355726338.json, 图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图图生图反推全都有_2111770424299315201.json, 图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图海报制作图生图｜一站式出图全家桶_2104759923023372289.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜文生图图生图全覆盖｜其它图片处理也拿手_2104789567328047105.json, 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json, 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json, 图片生成/文生图/Qwen Image 2.1工作流合集｜文生图图生图多场景全家桶_2110683569914998785.json, 图片生成/文生图/Qwen Image 2.1生成大合集精简版｜文生图图生图双模式｜日常出图够用了_2104773678444670978.json, 图片生成/文生图/qwen image2.1三视图｜写实人物角色批量出图_2103766316233613313.json, 图片生成/文生图/qwen image2.1写实三视图｜人物角色批量出图 文生图图生图通吃_2104099183790739457.json, 图片生成/文生图/写实角色三视图批量出图 qwen image2.1人物设定一键生成_2104276130005082113.json, 图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json, 图片生成/文生图/怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_26

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen2.1双图版_Flux2Klein自动生成图_2102391245615230977.json、图片生成/图生图/Qwen2.1双图版｜Flux2Klein自动生成图｜双参考融合效果更自然_2102585557531578370.json、图片生成/图生图/qwen image2.1短剧漫剧三视图｜写实人物角色批量出图_2103704294355726338.json、图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图图生图反推全都有_2111770424299315201.json、图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图海报制作图生图｜一站式出图全家桶_2104759923023372289.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 16 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 15/16 个有
- `LoraLoaderModelOnly` —— 15/16 个有
- `solarL_SaveImagesToZip` —— 15/16 个有
- `GetNode` —— 14/16 个有
- `QwenImage21Cache` —— 14/16 个有
- `SetNode` —— 14/16 个有
- `ShowText|pysssss` —— 14/16 个有
- `孤海注释` —— 14/16 个有
- `BatchImagesNode` —— 12/16 个有
- `PreviewAny` —— 12/16 个有
- `LayerUtility: ImageReel` —— 11/16 个有
- `LayerUtility: ImageReelComposit` —— 11/16 个有
- `Fast Groups Bypasser (rgthree)` —— 10/16 个有
- `easy showAnything` —— 10/16 个有
- `easy setNode` —— 9/16 个有
- `AIO_Preprocessor` —— 5/16 个有
- `CR Text` —— 5/16 个有
- `FastGroupsBypassSwitch` —— 5/16 个有
- `ImageBlend` —— 5/16 个有
- `Seed (rgthree)` —— 5/16 个有
- `CR Text Concatenate` —— 4/16 个有
- `DWPreprocessor` —— 4/16 个有
- `DepthAnythingPreprocessor` —— 4/16 个有
- `Qwen3VL_Advanced` —— 4/16 个有
- `EmptyFlux2LatentImage` —— 2/16 个有
- `LoraLoader` —— 2/16 个有
- `LoraLoaderBypassModelOnly` —— 2/16 个有
- `easy sleep` —— 2/16 个有
- `BlockifyMask` —— 1/16 个有
- `DepthAnythingV2Preprocessor` —— 1/16 个有
- `DrawMaskOnImage` —— 1/16 个有
- `ImageResizeKJ` —— 1/16 个有
- `ImageScaleToTotalPixels` —— 1/16 个有
- `LayerMask: BiRefNetUltraV2` —— 1/16 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/16 个有
- `LayerUtility: ImageBlend` —— 1/16 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 16 | 23% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 16 | 80% |
| 采样算法 | er_sde | - | 16 | 94% |
| 调度器 | beta | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| LoRA 模型强度 | 0.4 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 80 | 80 - 1024 | 16 | 0% |
| 高度 | 80 | 80 - 1024 | 16 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，16 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，16 个样本，取值集中（一致性 80%）
- 采样算法 最常用 er_sde，16 个样本，一致性 94%
- 调度器 最常用 beta，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，16 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，16 个样本，取值分散，一致性仅 0%
- 高发问题（22/16 个样本）：Steps较低可能导致细节不足
