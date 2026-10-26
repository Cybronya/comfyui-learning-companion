---
name: unknown_workflow_upscale_sampler_unet_11
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.70325
common_nodes: [Any Switch (rgthree), Anything Everywhere3, CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, QwenImage21Cache, RHLLMChatNode, ResizeLongestToNode, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json, 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json, 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101781526932447234.json, 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json、图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列11集_2102948623549026306.json、图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101781526932447234.json、图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere3`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `RHLLMChatNode`
- `ResizeLongestToNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `Fast Bypasser (rgthree)` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `SplitImageWithAlpha` —— 1/4 个有
- `VOSR2ModelLoader` —— 1/4 个有
- `VOSR2Upscale` —— 1/4 个有
- `easy float` —— 1/4 个有
- `easy int` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
