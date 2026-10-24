---
name: unknown_workflow_sampler_unet_vae_311
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7195
common_nodes: [CFGGuider, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSamplerSelect, ManualSigmas, PreviewAny, PrimitiveStringMultiline, QwenImage21Cache, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json, 图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_311

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json、图片生成/文生图/Qwen Image 2.1 Turbo：文生图_2110484342584733697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `SaveImageAdvanced` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
