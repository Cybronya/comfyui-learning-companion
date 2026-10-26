---
name: unknown_workflow_sampler_unet_vae_14
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.812136
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json, 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2110914073675259905.json, 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json, 图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json, 图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json, 图片生成/图生图/Face Swap  Qwen-Image-2.1模特换头+换脸_2102208882394357762.json, 图片生成/图生图/Face+Swap换脸+Qwen-Image-2.1模特换头+换脸_2110526511987122178.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2101985763167653889.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102008336353939458.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102025891684634626.json, 图片生成/图生图/Qwen Image 2.1 一键图片换装_2102585909454659586.json, 图片生成/图生图/Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578.json, 图片生成/图生图/Qwen Image 2.1 图片换装！B站艾橘溪_2101836548382740482.json, 图片生成/图生图/Qwen Image 2.1图像编辑_2101559779452866561.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2107755188273635330.json, 图片生成/图生图/Qwen Image 2.1：图像编辑_2107781008266452993.json, 图片生成/图生图/Qwen image 2.1 3图编辑_2101904839130312705.json, 图片生成/图生图/Qwen image 2.1单图编辑_2101881268609830914.json, 图片生成/图生图/Qwen image 2.1双图编辑_2101903016357097474.json, 图片生成/图生图/Qwen_Image_2.1图像编辑_2108748975942750210.json, 图片生成/图生图/Qwen_Image_2.1图像编辑_2110553190163902466.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_14

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/反推提示词/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json、图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2110914073675259905.json、图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json、图片生成/图生图/CGD_qwen-image-2.1-rh-image-edit_2104821386530349058.json、图片生成/图生图/Character Costume Changes Qwen Image 2.1 人物换装_2102208875008184321.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 22 个 workflow 都包含：
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
- `ComfySwitchNode` —— 21/22 个有
- `BatchImagesNode` —— 18/22 个有
- `ResolutionSelector` —— 18/22 个有
- `JjkText` —— 16/22 个有
- `TextGenerateLTX2Prompt` —— 12/22 个有
- `PrimitiveStringMultiline` —— 11/22 个有
- `SaveImageAdvanced` —— 11/22 个有
- `ImageCompare` —— 7/22 个有
- `TextGenerate` —— 7/22 个有
- `PreviewAny` —— 5/22 个有
- `GetImageSize` —— 4/22 个有
- `easy showAnything` —— 4/22 个有
- `ImageConcatMulti` —— 3/22 个有
- `ModelAttentionBackend` —— 3/22 个有
- `ResizeImageMaskNode` —— 3/22 个有
- `easy cleanGpuUsed` —— 3/22 个有
- `CR Text` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1088 | 22 | 98% |
| 高度 | 1024 | 1024 - 1920 | 22 | 77% |
| 采样步数 | 50 | 25 - 50 | 22 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1088，22 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，22 个样本
- 采样步数 中位数 50，观测区间 25 - 50，22 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
