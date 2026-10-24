---
name: unknown_workflow_sampler_unet_vae_17
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.7149
common_nodes: [CLIPLoader, CR Prompt Text, EmptyLatentImage, KSampler, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 图像编辑_2104466208149032961.json, 图片生成/图生图/Qwen Image 2.1图像合集_2101928184118861826.json, 图片生成/图生图/Qwen Image 2.1工作流合集_2102019794622042113.json, 图片生成/图生图/Qwen image 2.1多图编辑_2104503241475186689.json, 图片生成/图生图/qwen image2.1AI短剧漫剧人物三视图_2103430511829016578.json, 图片生成/图生图/qwen image2.1产品细节图_2102470856244031490.json, 图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json, 图片生成/图生图/【Qwen Image 2.1】图像生成 双图版_2102369979093053442.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集20步_2102363823524114434.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2102355136613015554.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2112774389644222465.json, 图片生成/图生图/【Qwen Image 2.1】图生图_2102944785588908034.json, 图片生成/图生图/图像生成大合集【Qwen Image 2.1】_2102573883814666241.json, 图片生成/文生图/Qwen Image 2.1 Character Reference Sheet (Four Views)_2102316050699345921.json, 图片生成/文生图/Qwen Image 2.1 Short Drama Asset Series – Environm_2102362481237782530.json, 图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json, 图片生成/文生图/Qwen Image 2.1工作流合集_2101942307816820738.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json, 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101781526932447234.json, 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_17

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 图像编辑_2104466208149032961.json、图片生成/图生图/Qwen Image 2.1图像合集_2101928184118861826.json、图片生成/图生图/Qwen Image 2.1工作流合集_2102019794622042113.json、图片生成/图生图/Qwen image 2.1多图编辑_2104503241475186689.json、图片生成/图生图/qwen image2.1AI短剧漫剧人物三视图_2103430511829016578.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 20 个 workflow 都包含：
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
- `Anything Everywhere3` —— 19/20 个有
- `Image Comparer (rgthree)` —— 19/20 个有
- `PreviewImage` —— 19/20 个有
- `ComfySwitchNode` —— 18/20 个有
- `LoadImage` —— 18/20 个有
- `easy setNode` —— 18/20 个有
- `LayerUtility: ImageReel` —— 17/20 个有
- `LayerUtility: ImageReelComposit` —— 17/20 个有
- `Fast Groups Bypasser (rgthree)` —— 16/20 个有
- `ShowText|pysssss` —— 16/20 个有
- `TextGenerateLTX2Prompt` —— 16/20 个有
- `GetNode` —— 15/20 个有
- `Seed (rgthree)` —— 15/20 个有
- `SetNode` —— 15/20 个有
- `PreviewAny` —— 11/20 个有
- `easy showAnything` —— 11/20 个有
- `BatchImagesNode` —— 10/20 个有
- `SeedVR2LoadDiTModel` —— 6/20 个有
- `SeedVR2LoadVAEModel` —— 6/20 个有
- `SeedVR2VideoUpscaler` —— 6/20 个有
- `LoraLoaderModelOnly` —— 5/20 个有
- `Any Switch (rgthree)` —— 4/20 个有
- `RHLLMChatNode` —— 4/20 个有
- `ResizeLongestToNode` —— 4/20 个有
- `easy getNode` —— 4/20 个有
- `Label (rgthree)` —— 3/20 个有
- `INTConstant` —— 2/20 个有
- `ImageScaleToTotalPixels` —— 2/20 个有
- `LayerUtility: TextJoin` —— 2/20 个有
- `Fast Bypasser (rgthree)` —— 1/20 个有
- `ImageScaleBy` —— 1/20 个有
- `PrimitiveBoolean` —— 1/20 个有
- `SplitImageWithAlpha` —— 1/20 个有
- `VOSR2ModelLoader` —— 1/20 个有
- `VOSR2Upscale` —— 1/20 个有
- `easy float` —— 1/20 个有
- `easy int` —— 1/20 个有
- `孤海注释` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 20 | 100% |
| 高度 | 1024 | 1024 - 1024 | 20 | 100% |
| 采样步数 | 40 | 20 - 40 | 20 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，20 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 20 - 40，20 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
