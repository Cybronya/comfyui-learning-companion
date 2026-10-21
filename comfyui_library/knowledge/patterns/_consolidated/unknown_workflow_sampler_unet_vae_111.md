---
name: unknown_workflow_sampler_unet_vae_111
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.726429
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 图像编辑_2104466208149032961.json, 图片生成/文生图/Qwen Image 2.1工作流合集_2101942307816820738.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2101880819102081026.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104545244179165185.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104558210060480513.json, 视频生成/图生视频/Qwen_Image_2.1_人物换背景_2107641147056283650.json, 视频生成/图生视频/【Qwen_Image_2.1】图生图_2102955819938705410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_111

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 图像编辑_2104466208149032961.json、图片生成/文生图/Qwen Image 2.1工作流合集_2101942307816820738.json、图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2101880819102081026.json、图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104545244179165185.json、图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104558210060480513.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 6/7 个有
- `BatchImagesNode` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `easy setNode` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `EmptyImage` —— 2/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 40 | 40 - 40 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
