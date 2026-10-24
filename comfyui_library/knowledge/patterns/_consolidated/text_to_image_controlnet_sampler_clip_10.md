---
name: text_to_image_controlnet_sampler_clip_10
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8462
common_nodes: [CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/3 - ControlNet_控图练习_1958846628482461697.json, 图片生成/图生图/SD1.5-Controlnet-Canny官方工作流_1930209981948399618.json, 图片生成/图生图/SD1.5-Controlnet-Depth官方工作流_1930211789093421057.json, 图片生成/图生图/SDXL版本的ControlNet_2011070077621248002.json, 图片生成/图生图/图生图基础工作流-ControlNet_1988172136642732034.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/3 - ControlNet_控图练习_1958846628482461697.json、图片生成/图生图/SD1.5-Controlnet-Canny官方工作流_1930209981948399618.json、图片生成/图生图/SD1.5-Controlnet-Depth官方工作流_1930211789093421057.json、图片生成/图生图/SDXL版本的ControlNet_2011070077621248002.json、图片生成/图生图/图生图基础工作流-ControlNet_1988172136642732034.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 4/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `VAELoader` —— 2/5 个有
- `Zoe-DepthMapPreprocessor` —— 2/5 个有
- `Canny` —— 1/5 个有
- `Checkpoint Loader (Simple)` —— 1/5 个有
- `DWPreprocessor` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageGetSize` —— 1/5 个有
- `RH_Translator` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 25 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 7 | 6 - 8 | 5 | 89% |
| 采样算法 | dpmpp_2m | - | 5 | 40% |
| 调度器 | karras | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 512 - 832 | 5 | 80% |
| 高度 | 512 | 512 - 1280 | 5 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 8，5 个样本，取值集中（一致性 89%）
- 采样算法 最常用 dpmpp_2m，5 个样本，一致性 40%
- 调度器 最常用 karras，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 832，5 个样本
- 高度 中位数 512，观测区间 512 - 1280，5 个样本
