---
name: unknown_workflow_sampler_unet_vae_127
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.731833
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, PreviewAny, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Prompt Text]
members: [图片生成/图生图/(V2)-qwen-image2.1-编辑_2102577867103236097.json, 图片生成/图生图/2102423497988460545.json, 图片生成/图生图/2105926870020747266.json, 图片生成/图生图/2106051868412694529.json, 图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json, 图片生成/文生图/qwen-image2.1(多功能官流）_2105926870020747266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_127

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/(V2)-qwen-image2.1-编辑_2102577867103236097.json、图片生成/图生图/2102423497988460545.json、图片生成/图生图/2105926870020747266.json、图片生成/图生图/2106051868412694529.json、图片生成/文生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `Any Switch (rgthree)` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `CR Prompt Text` —— 1/6 个有
- `RegexExtract` —— 1/6 个有
- `SaveImageAdvanced` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 25 - 30 | 6 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 25 - 30，6 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
