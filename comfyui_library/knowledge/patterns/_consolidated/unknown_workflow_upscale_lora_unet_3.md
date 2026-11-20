---
name: unknown_workflow_upscale_lora_unet_3
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.582
common_nodes: [CLIPLoader, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageCaptionNode, Label (rgthree), LayerFilter: HDREffects, LoadImage, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, SetNode, ShowText|pysssss, SplitImageWithAlpha, Text Multiline, UNETLoader, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageChooser]
problems: []
missing: []
members: [图片生成/文生图/moss 最新进阶版_2116735748065026049.json, 图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json, 图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json, 图片生成/文生图/一键运行：最新 moss image 文生图 放大工作流_2113889238105280513.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/moss 最新进阶版_2116735748065026049.json、图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json、图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json、图片生成/文生图/一键运行：最新 moss image 文生图 放大工作流_2113889238105280513.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCaptionNode`
- `Label (rgthree)`
- `LayerFilter: HDREffects`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SplitImageWithAlpha`
- `Text Multiline`
- `UNETLoader`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageChooser`

**可变部分**（部分 workflow 才有）：
- `CR Latent Input Switch` —— 3/4 个有
- `CR Seed` —— 3/4 个有
- `CR Text Input Switch (4 way)` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `KSampler (Efficient)` —— 3/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `SkipLayerGuidanceDiTSimple` —— 2/4 个有
- `TextEncodeQwenImage21` —— 2/4 个有
- `TextGenerate` —— 2/4 个有
- `easy positive` —— 2/4 个有
- `BasicGuider` —— 1/4 个有
- `CR Text Input Switch` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `ManualSigmas` —— 1/4 个有
- `PreviewTextNode` —— 1/4 个有
- `RandomNoise` —— 1/4 个有
- `SamplerCustomAdvanced` —— 1/4 个有
- `TESpeedQwenImage21` —— 1/4 个有
- `TE_image_pro_moss_box` —— 1/4 个有
- `TE_image_pro_moss_layout` —— 1/4 个有
- `VAEDecode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 3 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，3 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
