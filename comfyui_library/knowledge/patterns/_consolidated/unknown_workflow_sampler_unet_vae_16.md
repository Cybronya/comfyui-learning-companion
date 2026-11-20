---
name: unknown_workflow_sampler_unet_vae_16
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.797708
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json, 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2110914073675259905.json, 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json, 图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json, 图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json, 图片生成/图生图/Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json, 图片生成/图生图/Face+Swap换脸+Qwen-Image-2.1模特换头+换脸_2110526511987122178.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2101985763167653889.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102008336353939458.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102025891684634626.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102585909454659586.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2115759350521356289.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2115800248063979521.json, 图片生成/图生图/Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578.json, 图片生成/图生图/Qwen Image 2.1 图片换装！B站艾橘溪_2101836548382740482.json, 图片生成/图生图/Qwen Image 2.1图像编辑_2101559779452866561.json, 图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2107755188273635330.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2107781008266452993.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2116859535926317057.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2116863222442717185.json, 图片生成/图生图/Qwen_Image_2.1图像编辑_2108748975942750210.json, 图片生成/图生图/Qwen_Image_2.1图像编辑_2110553190163902466.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json、图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2110914073675259905.json、图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json、图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json、图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 23/24 个有
- `BatchImagesNode` —— 20/24 个有
- `JjkText` —— 18/24 个有
- `ResolutionSelector` —— 18/24 个有
- `PrimitiveStringMultiline` —— 13/24 个有
- `TextGenerateLTX2Prompt` —— 12/24 个有
- `SaveImageAdvanced` —— 10/24 个有
- `ImageCompare` —— 9/24 个有
- `TextGenerate` —— 9/24 个有
- `PreviewAny` —— 7/24 个有
- `GetImageSize` —— 4/24 个有
- `ModelAttentionBackend` —— 3/24 个有
- `ResizeImageMaskNode` —— 3/24 个有
- `CR Text` —— 1/24 个有
- `easy showAnything` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 24 | 98% |
| 高度 | 1024 | 1024 - 1920 | 24 | 77% |
| 采样步数 | 50 | 25 - 50 | 24 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，24 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，24 个样本
- 采样步数 中位数 50，观测区间 25 - 50，24 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
