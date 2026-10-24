---
name: unknown_workflow_sampler_unet_vae_93
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7136
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1图像编辑_2101559779452866561.json, 图片生成/图生图/Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2107755188273635330.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2107781008266452993.json, 图片生成/图生图/Qwen_Image_2.1图像编辑_2108748975942750210.json, 图片生成/图生图/Qwen_Image_2.1图像编辑_2110553190163902466.json, 图片生成/文生图/AI换装丨Qwen-Image 2.1丨双图试穿·智能提示词_2108075858605993985.json, 图片生成/文生图/Qwen Image 2.1：文生图_2101751274873122818.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2111477762887348225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_93

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图像编辑_2101559779452866561.json、图片生成/图生图/Qwen Image 2.1自动分镜 短剧分镜_2102191085471752193.json、图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json、图片生成/图生图/Qwen Image 2.1：图像编辑_2107755188273635330.json、图片生成/图生图/Qwen Image 2.1：图像编辑_2107781008266452993.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImageAdvanced` —— 9/10 个有
- `LoadImage` —— 8/10 个有
- `ResolutionSelector` —— 7/10 个有
- `ImageCompare` —— 6/10 个有
- `TextGenerate` —— 6/10 个有
- `JjkText` —— 5/10 个有
- `PreviewAny` —— 5/10 个有
- `BatchImagesNode` —— 4/10 个有
- `GetImageSize` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `ResizeImageMaskNode` —— 3/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 10 | 98% |
| 高度 | 1024 | 1024 - 1920 | 10 | 76% |
| 采样步数 | 25 | 25 - 50 | 10 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，10 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，10 个样本
- 采样步数 中位数 25，观测区间 25 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
