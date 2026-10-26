---
name: unknown_workflow_sampler_unet_vae_130
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.60275
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json, 图片生成/图生图/Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090.json, 图片生成/图生图/Qwen-image21-图像编辑_2103256220042874881.json, 图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json, 图片生成/图生图/QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json, 图片生成/图生图/QwenImage2.1图片编辑+ 官方提示词助手_2102657855655600129.json, 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json, 视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_130

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json、图片生成/图生图/Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090.json、图片生成/图生图/Qwen-image21-图像编辑_2103256220042874881.json、图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json、图片生成/图生图/QwenImage2.1 I2I + 官方提示词助手_2102348928711741442.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `QwenImage21Cache` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `Seed (rgthree)` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `PreviewImage` —— 3/8 个有
- `SaveImageAdvanced` —— 3/8 个有
- `Any Switch (rgthree)` —— 2/8 个有
- `BatchImagesNode` —— 2/8 个有
- `ImageBatchMulti` —— 2/8 个有
- `JsonExtractString` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `TextConcatenator` —— 2/8 个有
- `TextGenerate` —— 2/8 个有
- `TextGenerateLTX2Prompt` —— 2/8 个有
- `EmptyImage` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 8 | 100% |
| 高度 | 1024 | 1024 - 1920 | 8 | 74% |
| 采样步数 | 30 | 25 - 50 | 8 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1920，8 个样本
- 采样步数 中位数 30，观测区间 25 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
