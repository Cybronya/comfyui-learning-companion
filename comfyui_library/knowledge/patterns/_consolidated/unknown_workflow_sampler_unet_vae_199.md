---
name: unknown_workflow_sampler_unet_vae_199
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8352
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, PreviewAny, ResolutionSelector, SaveImage, StringConstantMultiline, StringFunction|pysssss, StringReplace, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json, 图片生成/图生图/Qwen2.1图像编辑_PE增强【已清理think】_2101899697924431873.json, 图片生成/图生图/qwen2.1图像编辑_2103878738139246594.json, 图片生成/图生图/qwen2.1移除rgba_2103878728098082818.json, 图片生成/图生图/qwen_image_21_controlnet_2105931638281687042.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_199

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json、图片生成/图生图/Qwen2.1图像编辑_PE增强【已清理think】_2101899697924431873.json、图片生成/图生图/qwen2.1图像编辑_2103878738139246594.json、图片生成/图生图/qwen2.1移除rgba_2103878728098082818.json、图片生成/图生图/qwen_image_21_controlnet_2105931638281687042.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
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
- `BatchImagesNode` —— 4/5 个有
- `ComfySwitchNode` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `QwenImage21Cache` —— 4/5 个有
- `easy seed` —— 4/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `ModelPatchLoader` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ZImageFunControlnet` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 40 | 40 - 40 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
