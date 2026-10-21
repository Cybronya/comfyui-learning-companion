---
name: text_to_image_lora_sampler_clip_84
type: Text To Image
frequency: 11
level: strong
coverage: 0.806273
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text, Seed (rgthree)]
members: [图片生成/图生图/2102274702399070209.json, 图片生成/图生图/2102513018897788929.json, 图片生成/图生图/2102557478423715841.json, 图片生成/图生图/Qwen Image 2.1｜万能输入文生图图生图一体工作流，千问2.1一站式创作_2107281533928300545.json, 图片生成/文生图/Qwen Image 2.1万能输入工作流，文生图图生图全场景覆盖处理方案_2107588581916233729.json, 图片生成/文生图/Qwen Image 2.1图像生成大合集｜文生图海报制作图生图｜一站式出图全家桶_2104759923023372289.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜多场景图片处理全搞定_2106628243129458690.json, 图片生成/文生图/Qwen Image 2.1图像编辑｜文生图图生图全覆盖｜其它图片处理也拿手_2104789567328047105.json, 图片生成/文生图/Qwen Image 2.1工作流合集，文生图图生图多场景覆盖方案_2103981137117925377.json, 图片生成/文生图/Qwen Image 2.1生成大合集精简版｜文生图图生图双模式｜日常出图够用了_2104773678444670978.json, 图片生成/文生图/怪獸出品Qwen Image 2.1工作流合集｜文生图图生图双模式打包_2103663285953458177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/2102274702399070209.json、图片生成/图生图/2102513018897788929.json、图片生成/图生图/2102557478423715841.json、图片生成/图生图/Qwen Image 2.1｜万能输入文生图图生图一体工作流，千问2.1一站式创作_2107281533928300545.json、图片生成/文生图/Qwen Image 2.1万能输入工作流，文生图图生图全场景覆盖处理方案_2107588581916233729.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/11 个有
- `PreviewAny` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `TextGenerateLTX2Prompt` —— 9/11 个有
- `Anything Everywhere3` —— 8/11 个有
- `ComfySwitchNode` —— 8/11 个有
- `GetNode` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `BatchImagesNode` —— 6/11 个有
- `Image Comparer (rgthree)` —— 6/11 个有
- `easy showAnything` —— 5/11 个有
- `LayerUtility: ImageReel` —— 4/11 个有
- `LayerUtility: ImageReelComposit` —— 4/11 个有
- `Seed (rgthree)` —— 4/11 个有
- `ShowText|pysssss` —— 4/11 个有
- `FastGroupsBypassSwitch` —— 3/11 个有
- `AIO_Preprocessor` —— 2/11 个有
- `CR Text` —— 2/11 个有
- `CR Text Concatenate` —— 2/11 个有
- `DWPreprocessor` —— 2/11 个有
- `DepthAnythingPreprocessor` —— 2/11 个有
- `ImageBlend` —— 2/11 个有
- `MiniMaxH3EasyMediaLoader` —— 2/11 个有
- `MiniMaxH3EasyMediaSplitter` —— 2/11 个有
- `Qwen3VL_Advanced` —— 2/11 个有
- `QwenPERewriteT8` —— 2/11 个有
- `easy setNode` —— 2/11 个有
- `easy sleep` —— 2/11 个有
- `GH_ImageVideoComparer` —— 1/11 个有
- `ImageBatchMultiV2` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、Seed (rgthree)
