---
name: unknown_workflow_sampler_unet_vae_34
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.650929
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, CR Prompt Text, Seed (rgthree)]
members: [图片生成/图生图/2102355136613015554.json, 图片生成/图生图/2102363823524114434.json, 图片生成/图生图/2102369979093053442.json, 图片生成/图生图/2102470856244031490.json, 图片生成/图生图/2102573883814666241.json, 图片生成/图生图/2104466208149032961.json, 图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json, 图片生成/文生图/Qwen Image 2.1 图像编辑_2104466208149032961.json, 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104545244179165185.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104558210060480513.json, 视频生成/图生视频/Qwen_Image_2.1_人物换背景_2107641147056283650.json, 视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json, 视频生成/图生视频/【Qwen_Image_2.1】图生图_2102955819938705410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_34

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/2102355136613015554.json、图片生成/图生图/2102363823524114434.json、图片生成/图生图/2102369979093053442.json、图片生成/图生图/2102470856244031490.json、图片生成/图生图/2102573883814666241.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 13/14 个有
- `CR Prompt Text` —— 12/14 个有
- `GetNode` —— 12/14 个有
- `PreviewImage` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `Anything Everywhere3` —— 11/14 个有
- `BatchImagesNode` —— 11/14 个有
- `LayerUtility: ImageReel` —— 11/14 个有
- `LayerUtility: ImageReelComposit` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 10/14 个有
- `PreviewAny` —— 10/14 个有
- `ShowText|pysssss` —— 9/14 个有
- `easy setNode` —— 9/14 个有
- `Seed (rgthree)` —— 8/14 个有
- `easy showAnything` —— 8/14 个有
- `LoraLoaderModelOnly` —— 4/14 个有
- `EmptyImage` —— 3/14 个有
- `ImageScaleToTotalPixels` —— 2/14 个有
- `PrimitiveBoolean` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 14 | 100% |
| 高度 | 1024 | 1024 - 1024 | 14 | 100% |
| 采样步数 | 40 | 20 - 50 | 14 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，14 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 20 - 50，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、easy setNode、CR Prompt Text、Seed (rgthree)
