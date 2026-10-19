---
name: unknown_workflow_upscale_sampler_unet_4
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.70725
common_nodes: [CLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, PrimitiveStringMultiline, RegexExtract, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105111828585078785.json, 图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105488974495178753.json, 图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json, 图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105111828585078785.json、图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105488974495178753.json、图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json、图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `ShowAnything|Mie` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `StringFormat` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 37.5 | 25 - 40 | 4 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 37.5，观测区间 25 - 40，4 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
