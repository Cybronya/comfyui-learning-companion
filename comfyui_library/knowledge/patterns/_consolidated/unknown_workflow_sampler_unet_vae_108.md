---
name: unknown_workflow_sampler_unet_vae_108
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.631286
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [PlaySound|pysssss, easy int]
members: [图片生成/图生图/2102301480060538882.json, 图片生成/图生图/2102585909454659586.json, 图片生成/图生图/2103753279908966401.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json, 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json, 图片生成/文生图/千问QWEN image 2.1 文生图+图生图整合流_2102301480060538882.json, 视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_108

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102301480060538882.json、图片生成/图生图/2102585909454659586.json、图片生成/图生图/2103753279908966401.json、图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json、图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `TextGenerateLTX2Prompt` —— 5/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `GetNode` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `easy int` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `EmptyImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |
| 采样步数 | 40 | 25 - 50 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：PlaySound|pysssss、easy int
