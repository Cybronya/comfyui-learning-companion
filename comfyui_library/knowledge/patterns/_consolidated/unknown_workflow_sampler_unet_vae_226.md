---
name: unknown_workflow_sampler_unet_vae_226
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.3975
common_nodes: [CLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, KSampler, LoadImage, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI代码侠土豆-Qwen Image 2.1 图生图_2101914903496974338.json, 图片生成/图生图/Qwen Image 2.1多图编辑2609_2106043418517524481.json, 图片生成/图生图/【尺素】Qwen_image_2_1多图编辑_2101917765199290370.json, 图片生成/图生图/【尺素】Qwen_image_2_1多图编辑（自带PE）_2101909045711032321.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_226

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI代码侠土豆-Qwen Image 2.1 图生图_2101914903496974338.json、图片生成/图生图/Qwen Image 2.1多图编辑2609_2106043418517524481.json、图片生成/图生图/【尺素】Qwen_image_2_1多图编辑_2101917765199290370.json、图片生成/图生图/【尺素】Qwen_image_2_1多图编辑（自带PE）_2101909045711032321.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：40%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `QwenImage21Cache` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `BatchImagesNode` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 40 | 25 - 50 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
