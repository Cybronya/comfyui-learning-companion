---
name: unknown_workflow_sampler_unet_vae_147
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.765
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, PreviewAny, ResolutionSelector, SaveImage, StringConstantMultiline, StringFunction|pysssss, StringReplace, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [StringFunction|pysssss, easy seed, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json, 图片生成/图生图/2101899697924431873.json, 图片生成/图生图/2105931638281687042.json, 图片生成/文生图/qwen_image_21_controlnet_2105931638281687042.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json、图片生成/图生图/2101899697924431873.json、图片生成/图生图/2105931638281687042.json、图片生成/文生图/qwen_image_21_controlnet_2105931638281687042.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `ResolutionSelector`
- `SaveImage`
- `StringConstantMultiline`
- `StringFunction|pysssss`
- `StringReplace`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 3/4 个有
- `ComfySwitchNode` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `ModelPatchLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ZImageFunControlnet` —— 2/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 40 | 40 - 40 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：StringFunction|pysssss、easy seed、LayerUtility: ImageScaleByAspectRatio V2
