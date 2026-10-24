---
name: unknown_workflow_upscale_lora_unet_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6125
common_nodes: [CLIPLoader, CR Latent Input Switch, CR Text Input Switch (4 way), EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageCaptionNode, Label (rgthree), LayerFilter: HDREffects, LoadImage, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, SetNode, ShowText|pysssss, SplitImageWithAlpha, Text Multiline, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageChooser, easy positive]
problems: []
missing: []
members: [图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json, 图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_unet_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/一键运行：Qwen-Image-2.1 文生图 高清放大 反推 图像选择_2105542674064437249.json、图片生成/文生图/一键运行：qwen image 2.1 turbo int8 最新文生图_2109204440988340226.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
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
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageChooser`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CR Seed` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `KSampler (Efficient)` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `PreviewTextNode` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `TESpeedQwenImage21` —— 1/2 个有
- `VAEDecode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
