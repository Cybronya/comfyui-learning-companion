---
name: unknown_workflow_upscale_sampler_unet_6
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.731833
common_nodes: [CLIPLoader, ComfySwitchNode, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Moss image 官方文生图_2112078306463019010.json, 图片生成/文生图/Moss image 文生图角色资产生成+真实美感【提示词增强】_2112449151177940994.json, 图片生成/文生图/QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978.json, 图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105111828585078785.json, 图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105488974495178753.json, 图片生成/文生图/Qwen-Image2.1 全能文生图(官方提示词强化)_2112470363312578562.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_6

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Moss image 官方文生图_2112078306463019010.json、图片生成/文生图/Moss image 文生图角色资产生成+真实美感【提示词增强】_2112449151177940994.json、图片生成/文生图/QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978.json、图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105111828585078785.json、图片生成/文生图/QWEN-IMAGE2.1_全能文生图(官方提示词强化)_2105488974495178753.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/6 个有
- `RegexExtract` —— 4/6 个有
- `ShowAnything|Mie` —— 4/6 个有
- `StringFormat` —— 4/6 个有
- `TextEncodeQwenImage21` —— 4/6 个有
- `CLIPTextEncode` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 50 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 43% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 50，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
