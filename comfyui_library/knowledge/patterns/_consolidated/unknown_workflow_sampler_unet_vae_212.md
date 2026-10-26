---
name: unknown_workflow_sampler_unet_vae_212
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.837
common_nodes: [CLIPLoader, EmptyLatentImage, KSamplerSelect, ManualSigmas, ResolutionSelector, SamplerCustom, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/qwen_image_2.1 _ 图像编辑 加速版_2103402673738436610.json, 图片生成/图生图/【qwen_image_2.1】图生图 多宫格_2109499886868713474.json, 图片生成/图生图/【qwen_image_2.1】图生图 角色三视图_2109460733288341506.json, 图片生成/文生图/Qwen_Image_2.1_Turbo_官方8步_文生图_2109357397138567170.json, 图片生成/文生图/qen image 2.1turbo 图片编辑_2062017330061860865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_212

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen_image_2.1 _ 图像编辑 加速版_2103402673738436610.json、图片生成/图生图/【qwen_image_2.1】图生图 多宫格_2109499886868713474.json、图片生成/图生图/【qwen_image_2.1】图生图 角色三视图_2109460733288341506.json、图片生成/文生图/Qwen_Image_2.1_Turbo_官方8步_文生图_2109357397138567170.json、图片生成/文生图/qen image 2.1turbo 图片编辑_2062017330061860865.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `ManualSigmas`
- `ResolutionSelector`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `ModelAttentionBackend` —— 2/5 个有
- `QwenImage21Cache` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `BatchImagesNode` —— 1/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `TextGenerateLTX2Prompt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
