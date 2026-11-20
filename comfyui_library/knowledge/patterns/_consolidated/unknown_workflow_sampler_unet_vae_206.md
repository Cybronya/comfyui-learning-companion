---
name: unknown_workflow_sampler_unet_vae_206
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7368
common_nodes: [BatchImagesNode, CLIPLoader, CenterCropImages, EmptyImage, EmptyLatentImage, GetImageSize, GetNode, ImageFromBatch, ImageScaleBy, KSampler, LoadImage, PreviewImage, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy imageSplitGrid]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1故事板图片生成及高清放大2609_2106041166184673281.json, 图片生成/图生图/qwen_image2.1AI短剧真人写实类角色卡生成器_2113887691749285890.json, 图片生成/图生图/qwen_image_2_1_storyboard_2kupscale_2104471312159825921.json, 图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109925252414394370.json, 图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109981748993024002.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_206

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1故事板图片生成及高清放大2609_2106041166184673281.json、图片生成/图生图/qwen_image2.1AI短剧真人写实类角色卡生成器_2113887691749285890.json、图片生成/图生图/qwen_image_2_1_storyboard_2kupscale_2104471312159825921.json、图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109925252414394370.json、图片生成/图生图/qwen_image_storyboard_2kupscale_character_data_2109981748993024002.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CenterCropImages`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `ImageFromBatch`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageSplitGrid`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 25 | 25 - 25 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
