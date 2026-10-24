---
name: unknown_workflow_unet_vae_6
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.728583
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, LoadImage, PrimitiveBoolean, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/(V2)-qwen-image2.1-编辑_2102577867103236097.json, 图片生成/图生图/QWEN-IMAGE2.1 全能图片编辑(官方提示词强化)_2101936542062309377.json, 图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json, 图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105492257238503425.json, 图片生成/图生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json, 图片生成/图生图/Qwen+image+2.1图片编辑_2104102668070383618.json, 图片生成/图生图/Qwen-Image2.1 全能图片编辑(官方提示词强化)_2112460333402124289.json, 图片生成/图生图/qwen-image2.1(多功能官流）_2105926870020747266.json, 图片生成/文生图/qwen-image2.1(turbo二合一工作流）_2109125599800422402.json, 图片生成/文生图/qwen-image2.1(turbo二合一工作流）_2112131978324697090.json, 图片生成/文生图/图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609.json, 图片生成/文生图/图生_文生二合一的qwen-image2.1-极速版_2109841509704097794.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/(V2)-qwen-image2.1-编辑_2102577867103236097.json、图片生成/图生图/QWEN-IMAGE2.1 全能图片编辑(官方提示词强化)_2101936542062309377.json、图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json、图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105492257238503425.json、图片生成/图生图/Qwen Image 2.1文生图和多图编辑（官流）2609_2106051868412694529.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 12 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `PrimitiveBoolean`
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
- `Image Comparer (rgthree)` —— 10/12 个有
- `KSampler` —— 8/12 个有
- `PreviewAny` —— 8/12 个有
- `PrimitiveInt` —— 8/12 个有
- `Any Switch (rgthree)` —— 6/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `ModelAttentionBackend` —— 6/12 个有
- `RegexExtract` —— 6/12 个有
- `GetImageSize` —— 4/12 个有
- `ImageResizeKJv2` —— 4/12 个有
- `KSamplerSelect` —— 4/12 个有
- `ManualSigmas` —— 4/12 个有
- `SamplerCustom` —— 4/12 个有
- `SeedVR2LoadDiTModel` —— 4/12 个有
- `SeedVR2LoadVAEModel` —— 4/12 个有
- `SeedVR2VideoUpscaler` —— 4/12 个有
- `ShowAnything|Mie` —— 4/12 个有
- `StringFormat` —— 4/12 个有
- `SaveImageAdvanced` —— 2/12 个有
- `StringConcatenate` —— 2/12 个有
- `孤海注释` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 25 - 40 | 8 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，观测区间 25 - 40，8 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
