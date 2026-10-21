---
name: unknown_workflow_upscale_sampler_unet_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6735
common_nodes: [CLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, PreviewAny, PrimitiveStringMultiline, RegexExtract, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, StringConcatenate, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json, 图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen Image2.1文生图（Generate重写提示词）2609_2106051239590064129.json、图片生成/文生图/Qwen image 2.1文生图（带模型和节点下载链接）_2102689936490192898.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveImageAdvanced` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 83% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
