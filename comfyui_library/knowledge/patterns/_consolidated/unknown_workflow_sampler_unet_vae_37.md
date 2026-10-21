---
name: unknown_workflow_sampler_unet_vae_37
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.645692
common_nodes: [Anything Everywhere3, CLIPLoader, CR Prompt Text, EmptyLatentImage, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, CR Prompt Text, Seed (rgthree)]
members: [图片生成/图生图/2102355136613015554.json, 图片生成/图生图/2102363823524114434.json, 图片生成/图生图/2102369979093053442.json, 图片生成/图生图/2102470856244031490.json, 图片生成/图生图/2102573883814666241.json, 图片生成/图生图/2104466208149032961.json, 图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json, 图片生成/文生图/Qwen Image 2.1 Character Reference Sheet (Four Views)_2102316050699345921.json, 图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json, 图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json, 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101781526932447234.json, 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_37

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/2102355136613015554.json、图片生成/图生图/2102363823524114434.json、图片生成/图生图/2102369979093053442.json、图片生成/图生图/2102470856244031490.json、图片生成/图生图/2102573883814666241.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 13 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 12/13 个有
- `PreviewImage` —— 12/13 个有
- `ComfySwitchNode` —— 11/13 个有
- `Fast Groups Bypasser (rgthree)` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `easy setNode` —— 11/13 个有
- `LayerUtility: ImageReel` —— 10/13 个有
- `LayerUtility: ImageReelComposit` —— 10/13 个有
- `Seed (rgthree)` —— 10/13 个有
- `ShowText|pysssss` —— 9/13 个有
- `TextGenerateLTX2Prompt` —— 9/13 个有
- `GetNode` —— 8/13 个有
- `SetNode` —— 8/13 个有
- `PreviewAny` —— 6/13 个有
- `SeedVR2LoadDiTModel` —— 6/13 个有
- `SeedVR2LoadVAEModel` —— 6/13 个有
- `SeedVR2VideoUpscaler` —— 6/13 个有
- `easy showAnything` —— 6/13 个有
- `BatchImagesNode` —— 5/13 个有
- `Any Switch (rgthree)` —— 4/13 个有
- `LoraLoaderModelOnly` —— 4/13 个有
- `RHLLMChatNode` —— 4/13 个有
- `ResizeLongestToNode` —— 4/13 个有
- `easy getNode` —— 4/13 个有
- `Label (rgthree)` —— 3/13 个有
- `INTConstant` —— 2/13 个有
- `ImageScaleToTotalPixels` —— 2/13 个有
- `LayerUtility: TextJoin` —— 2/13 个有
- `Fast Bypasser (rgthree)` —— 1/13 个有
- `ImageScaleBy` —— 1/13 个有
- `PrimitiveBoolean` —— 1/13 个有
- `SplitImageWithAlpha` —— 1/13 个有
- `VOSR2ModelLoader` —— 1/13 个有
- `VOSR2Upscale` —— 1/13 个有
- `easy float` —— 1/13 个有
- `easy int` —— 1/13 个有
- `孤海注释` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1024 | 1024 - 1024 | 13 | 100% |
| 采样步数 | 40 | 20 - 40 | 13 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 20 - 40，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、easy setNode、CR Prompt Text、Seed (rgthree)
