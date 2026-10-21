---
name: unknown_workflow_sampler_unet_vae_31
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.857643
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json, 图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json, 图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json, 图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json, 图片生成/文生图/qwen-image-2.1文生图_2102011026517614593.json, 图片生成/文生图/qwen-image-2.1文生图｜高效创作，一键生图_2105572911326261250.json, 图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json, 图片生成/文生图/qwen2.1基础工作流  i2v  t2v_2102578292409847810.json, 图片生成/文生图/图像编辑（多图）-qwen image 2.1_2101936015538737153.json, 视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json, 视频生成/图生视频/Qwen_Image_2.1_参考人物姿势_2102963142430126082.json, 视频生成/文生视频/Qwen_Image_2.1_PE_文生图_2104447077903323137.json, 视频生成/文生视频/Qwen_Image_2.1_文生图-PE版_2106926003867185154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_31

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json、图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json、图片生成/文生图/image_qwen_image_2_1_t2i_2102665438198059010.json、图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json、图片生成/文生图/qwen-image-2.1文生图_2101682733440389121.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 12/14 个有
- `ComfySwitchNode` —— 6/14 个有
- `QwenImage21Cache` —— 6/14 个有
- `EmptyImage` —— 5/14 个有
- `LoadImage` —— 5/14 个有
- `PreviewImage` —— 5/14 个有
- `SaveImageAdvanced` —— 5/14 个有
- `CR Prompt Text` —— 4/14 个有
- `QwenPERewriteT8` —— 4/14 个有
- `easy cleanGpuUsed` —— 4/14 个有
- `easy showAnything` —— 4/14 个有
- `AIO_Preprocessor` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `Seed (rgthree)` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 14 | 76% |
| 高度 | 1024 | 1024 - 2048 | 14 | 71% |
| 采样步数 | 25 | 25 - 40 | 14 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，14 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，14 个样本
- 采样步数 中位数 25，观测区间 25 - 40，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
