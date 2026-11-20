---
name: unknown_workflow_unet_vae_6
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7953
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, LoadImage, PrimitiveBoolean, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json, 图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json, 图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json, 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json, 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json, 图片生成/图生图/Qwen image 2.1 多图编辑工作流_2102302931948228610.json, 图片生成/图生图/pandy-Qwen2.1-JM3D全身公仔_2114275920147214337.json, 图片生成/图生图/pandy-Qwen2.1-雕版复古_2114276003089567745.json, 图片生成/文生图/图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609.json, 图片生成/文生图/图生_文生二合一的qwen-image2.1-极速版_2109841509704097794.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json、图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json、图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json、图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json、图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `LoadImage`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `TextGenerateLTX2Prompt` —— 7/10 个有
- `easy showAnything` —— 7/10 个有
- `KSamplerSelect` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `ManualSigmas` —— 6/10 个有
- `SamplerCustom` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `KSampler` —— 4/10 个有
- `PrimitiveInt` —— 4/10 个有
- `孤海注释` —— 4/10 个有
- `QwenImage21Cache` —— 3/10 个有
- `Any Switch (rgthree)` —— 2/10 个有
- `ImageScaleToTotalPixels` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `TextGenerate` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageMergeNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 10 | 100% |
| 高度 | 1024 | 1024 - 1024 | 10 | 100% |
| 采样步数 | 32.5 | 25 - 40 | 4 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 32.5，观测区间 25 - 40，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
