---
name: unknown_workflow_upscale_sampler_unet
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.7365
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/角色资产4格资产图工作流02【Qwen-Image2.1+seedvr2放大——无需提示词】_2113046828030709761.json, 图片生成/图生图/Minimax H3 人像参考图专用生成器_2112535531715391490.json, 图片生成/图生图/QWEN-IMAGE2.1 全能图片编辑(官方提示词强化)_2101936542062309377.json, 图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json, 图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105492257238503425.json, 图片生成/图生图/Qwen-Image2.1 全能图片编辑(官方提示词强化)_2112460333402124289.json, 图片生成/图生图/Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834.json, 图片生成/图生图/Qwen-Image2.1 角色资产三视图生成_2112411740599308289.json, 图片生成/图生图/【AI军火商】全网最强角色资产4格详图制作【Qwen-Image2.1】_2108004428056973313.json, 图片生成/图生图/角色资产4格详图制作【Qwen-Image2.1】_2107476393411039233.json, 图片生成/图生图/角色资产4格详图制作【Qwen-Image2.1】_2113778569058021377.json, 图片生成/图生图/角色资产4格详图制作【Qwen-Image2.1】_2114199758721085441.json, 图片生成/文生图/QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978.json, 图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105111828585078785.json, 图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105488974495178753.json, 图片生成/文生图/Qwen-Image2.1 全能文生图(官方提示词强化)_2112470363312578562.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/反推提示词/角色资产4格资产图工作流02【Qwen-Image2.1+seedvr2放大——无需提示词】_2113046828030709761.json、图片生成/图生图/Minimax H3 人像参考图专用生成器_2112535531715391490.json、图片生成/图生图/QWEN-IMAGE2.1 全能图片编辑(官方提示词强化)_2101936542062309377.json、图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json、图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105492257238503425.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 15/16 个有
- `PrimitiveStringMultiline` —— 15/16 个有
- `Fast Groups Bypasser (rgthree)` —— 14/16 个有
- `LoadImage` —— 12/16 个有
- `QwenImage21Cache` —— 11/16 个有
- `PrimitiveBoolean` —— 10/16 个有
- `RegexExtract` —— 8/16 个有
- `ShowAnything|Mie` —— 8/16 个有
- `StringFormat` —— 8/16 个有
- `TextGenerate` —— 8/16 个有
- `PreviewImage` —— 7/16 个有
- `BatchImagesNode` —— 4/16 个有
- `孤海注释` —— 3/16 个有
- `EmptyImage` —— 2/16 个有
- `CR Prompt Text` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 16 | 100% |
| 高度 | 1024 | 1024 - 1024 | 16 | 100% |
| 采样步数 | 40 | 20 - 40 | 16 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 20 - 40，16 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
