---
name: unknown_workflow_sampler_unet_vae_152
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.704
common_nodes: [Anything Everywhere3, BatchImagesNode, CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), KSampler, LoadImage, PreviewAny, PreviewImage, ResolutionSelector, SaveImage, SetNode, ShowText|pysssss, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen image 2.1人物文生图_2112139836655226882.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2101880819102081026.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104545244179165185.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104558210060480513.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2108808492491567105.json, 图片生成/文生图/👾怪獸-Qwen Image 2.1工作流合集👾_2103453643277168641.json, 视频生成/图生视频/Qwen_Image_2.1_人物换背景_2107641147056283650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_152

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen image 2.1人物文生图_2112139836655226882.json、图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2101880819102081026.json、图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104545244179165185.json、图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104558210060480513.json、图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2108808492491567105.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `Anything Everywhere3`
- `BatchImagesNode`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 6/7 个有
- `LayerUtility: ImageReelComposit` —— 6/7 个有
- `QwenImage21Cache` —— 6/7 个有
- `easy setNode` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `Seed (rgthree)` —— 5/7 个有
- `JjkText` —— 2/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `DWPreprocessor` —— 1/7 个有
- `DepthAnythingPreprocessor` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `FastGroupsBypassSwitch` —— 1/7 个有
- `ImageBlend` —— 1/7 个有
- `LoraLoaderBypassModelOnly` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `Qwen3VL_Advanced` —— 1/7 个有
- `QwenImage21SageAttentionT8` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 40 | 6 - 40 | 7 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 6 - 40，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
