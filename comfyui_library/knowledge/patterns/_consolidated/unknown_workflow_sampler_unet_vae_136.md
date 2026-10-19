---
name: unknown_workflow_sampler_unet_vae_136
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.799
common_nodes: [CLIPLoader, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, PreviewImage, QwenImage21Cache, QwenPERewriteT8, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json, 视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json, 视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json, 视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json, 视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json、视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json、视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json、视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json、视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 4/5 个有
- `LoadImage` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有

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
