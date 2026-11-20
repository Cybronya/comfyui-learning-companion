---
name: unknown_workflow_upscale_lora_unet_4
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.596667
common_nodes: [CLIPLoader, CR Latent Input Switch, CR Text Input Switch (4 way), EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageCaptionNode, Label (rgthree), LayerFilter: HDREffects, LoadImage, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, SetNode, ShowText|pysssss, SplitImageWithAlpha, Text Multiline, UNETLoader, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageChooser]
problems: []
missing: []
members: [图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json, 图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json, 图片生成/文生图/一键运行：最新 moss image 文生图 放大工作流_2113889238105280513.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json、图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json、图片生成/文生图/一键运行：最新 moss image 文生图 放大工作流_2113889238105280513.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Latent Input Switch`
- `CR Text Input Switch (4 way)`
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
- `CR Seed` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `KSampler (Efficient)` —— 2/3 个有
- `TextEncodeQwenImage21` —— 2/3 个有
- `TextGenerate` —— 2/3 个有
- `easy positive` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `KSamplerSelect` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `PreviewTextNode` —— 1/3 个有
- `RandomNoise` —— 1/3 个有
- `SamplerCustomAdvanced` —— 1/3 个有
- `SkipLayerGuidanceDiTSimple` —— 1/3 个有
- `TESpeedQwenImage21` —— 1/3 个有
- `VAEDecode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14.5 | - | 2 | 28% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 14.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
