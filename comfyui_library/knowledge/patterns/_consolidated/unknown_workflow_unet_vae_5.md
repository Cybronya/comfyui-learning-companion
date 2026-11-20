---
name: unknown_workflow_unet_vae_5
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.770833
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, LoadImage, PrimitiveBoolean, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json, 图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json, 图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json, 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json, 图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json, 图片生成/图生图/Qwen image 2.1 多图编辑工作流_2102302931948228610.json, 图片生成/图生图/pandy-Qwen2.1-JM3D全身公仔_2114275920147214337.json, 图片生成/图生图/pandy-Qwen2.1-雕版复古_2114276003089567745.json, 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json, 图片生成/文生图/图生_文生二合一的qwen-image2.1-turbo int8极速版_2109305146009284609.json, 图片生成/文生图/图生_文生二合一的qwen-image2.1-极速版_2109841509704097794.json, 视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 turbo 光影迁移_2112413229950521345.json、图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json、图片生成/图生图/Qwen image 2.1 图生图提示词增强_2101913388136886273.json、图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102032777880358913.json、图片生成/图生图/Qwen image 2.1 多图编辑-带提示词增强-int8版_2102302487393951746.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 12 个 workflow 都包含：
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
- `BatchImagesNode` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `TextGenerateLTX2Prompt` —— 9/12 个有
- `easy showAnything` —— 9/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 6/12 个有
- `KSampler` —— 6/12 个有
- `KSamplerSelect` —— 6/12 个有
- `ManualSigmas` —— 6/12 个有
- `SamplerCustom` —— 6/12 个有
- `QwenImage21Cache` —— 5/12 个有
- `ImageScaleToTotalPixels` —— 4/12 个有
- `PrimitiveInt` —— 4/12 个有
- `孤海注释` —— 4/12 个有
- `Image Comparer (rgthree)` —— 3/12 个有
- `Any Switch (rgthree)` —— 2/12 个有
- `GetNode` —— 2/12 个有
- `ModelAttentionBackend` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `TextGenerate` —— 2/12 个有
- `EmptyImage` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `ImageMergeNode` —— 1/12 个有
- `PreviewImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |
| 采样步数 | 40 | 25 - 50 | 6 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 50，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
