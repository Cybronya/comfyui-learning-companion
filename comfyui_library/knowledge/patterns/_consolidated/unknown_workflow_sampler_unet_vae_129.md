---
name: unknown_workflow_sampler_unet_vae_129
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json, 图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json, 图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json, 图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json, 图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json, 图片生成/图生图/Qwen-Image-2.1 图片编辑总控_2101868365479497729.json, 图片生成/图生图/Qwen-Image-2.1 多角度相机控制_2109821564979081218.json, 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo-6步LORA快速出圖_2103865932690059265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_129

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json、图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json、图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json、图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json、图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `ComfySwitchNode` —— 6/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `QwenImage21Cache` —— 5/8 个有
- `GetImageSize` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `ImageScaleBy` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `QwenMultiangleCameraNode` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有
- `VAEEncodeTiled` —— 1/8 个有
- `easy promptList` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 8 | 71% |
| 高度 | 1024 | 1024 - 2048 | 8 | 71% |
| 采样步数 | 12 | 6 - 25 | 8 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.18 - 1 | 8 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，8 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，8 个样本
- 采样步数 中位数 12，观测区间 6 - 25，8 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.18 - 1，8 个样本
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
