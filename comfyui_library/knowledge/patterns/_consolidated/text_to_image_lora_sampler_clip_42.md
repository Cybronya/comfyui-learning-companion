---
name: text_to_image_lora_sampler_clip_42
type: Text To Image
frequency: 19
level: strong
coverage: 0.798158
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1单图编辑流｜局部修改想改哪里改哪里_2108081920897806338.json, 图片生成/图生图/Qwen Image 2.1单图编辑角色四视图工作流，角色设计图生图处理工具_2106859828982407170.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2104763014581940225.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json, 图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜想修哪里修哪里_2107745036996800513.json, 图片生成/图生图/Qwen Image 2.1图像编辑利器｜图生图局部修改一句话搞定_2110685195149074434.json, 图片生成/图生图/Qwen Image 2.1多图编辑图片编辑全节点注释处理工具_2102541742317850626.json, 图片生成/图生图/Qwen Image 2.1多图编辑｜多参考图融合修改｜批量改图效率翻倍_2104764482592534530.json, 图片生成/图生图/Qwen Image 2.1｜万能输入文生图图生图一体工作流，千问2.1一站式创作_2107281533928300545.json, 图片生成/图生图/Qwen-Image-2.1图像编辑10张参考图｜局部重绘换装 图生图全能_2104094197203685378.json, 图片生成/图生图/Qwen-Image-2.1图像编辑｜最多10张参考图图生图随心改_2106230157538324481.json, 图片生成/图生图/最多10张参考图 Qwen-Image-2.1图像编辑2K输出换装局部重绘_2104274563130548225.json, 图片生成/图生图/最强换装工作流，电商服装展示一键换衣图生图处理工具_2106510801598246914.json, 图片生成/文生图/Qwen Image 2.1万能输入工作流，文生图图生图全场景覆盖处理方案_2107588581916233729.json, 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图两用_2110837013854375937.json, 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json, 图片生成/文生图/Qwen Image 2.1工作流合集｜文生图图生图多场景全家桶_2110683569914998785.json, 图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json, 图片生成/文生图/怪獸整理Qwen Image 2.1合集｜文生图换装修图全收录_2103070200995340289.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1单图编辑流｜局部修改想改哪里改哪里_2108081920897806338.json、图片生成/图生图/Qwen Image 2.1单图编辑角色四视图工作流，角色设计图生图处理工具_2106859828982407170.json、图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2104763014581940225.json、图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜一张图也能精修到位_2108523054933561346.json、图片生成/图生图/Qwen Image 2.1单图编辑｜图生图局部修改｜想修哪里修哪里_2107745036996800513.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 18/19 个有
- `Anything Everywhere3` —— 16/19 个有
- `ComfySwitchNode` —— 16/19 个有
- `QwenImage21Cache` —— 16/19 个有
- `CR Prompt Text` —— 15/19 个有
- `TextGenerateLTX2Prompt` —— 13/19 个有
- `GetNode` —— 12/19 个有
- `SetNode` —— 12/19 个有
- `BatchImagesNode` —— 11/19 个有
- `ShowText|pysssss` —— 11/19 个有
- `Fast Groups Bypasser (rgthree)` —— 10/19 个有
- `CR Text Concatenate` —— 9/19 个有
- `PreviewAny` —— 8/19 个有
- `CR Text` —— 6/19 个有
- `AIO_Preprocessor` —— 5/19 个有
- `FastGroupsBypassSwitch` —— 5/19 个有
- `Image Comparer (rgthree)` —— 5/19 个有
- `ImageBlend` —— 5/19 个有
- `PreviewImage` —— 5/19 个有
- `Seed (rgthree)` —— 5/19 个有
- `TextGenerate` —— 5/19 个有
- `easy showAnything` —— 5/19 个有
- `DWPreprocessor` —— 4/19 个有
- `DepthAnythingPreprocessor` —— 4/19 个有
- `Qwen3VL_Advanced` —— 4/19 个有
- `ResizeLongestToNode` —— 4/19 个有
- `PrimitiveStringMultiline` —— 3/19 个有
- `LoraLoaderBypassModelOnly` —— 2/19 个有
- `easy sleep` —— 2/19 个有
- `BlockifyMask` —— 1/19 个有
- `CompressImages` —— 1/19 个有
- `DepthAnythingV2Preprocessor` —— 1/19 个有
- `DrawMaskOnImage` —— 1/19 个有
- `ImageResizeKJ` —— 1/19 个有
- `ImageScaleToTotalPixels` —— 1/19 个有
- `LayerMask: BiRefNetUltraV2` —— 1/19 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/19 个有
- `LayerUtility: ImageBlend` —— 1/19 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（23/19 个样本）：Steps较低可能导致细节不足
