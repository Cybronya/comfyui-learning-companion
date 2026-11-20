---
name: unknown_workflow_sampler_unet_vae_283
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.80775
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image2.1姿态编辑_2101935950074048514.json, 图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json, 图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json, 图片生成/图生图/Qwen-Image-2.1 多角度相机控制_2109821564979081218.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_283

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image2.1姿态编辑_2101935950074048514.json、图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json、图片生成/图生图/Qwen-Image-2.1 动漫转真人_2108914677098045442.json、图片生成/图生图/Qwen-Image-2.1 多角度相机控制_2109821564979081218.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `GroupSwitcher` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `NuiKr.OpenPoseEditor` —— 1/4 个有
- `OpenposePreprocessor` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `easy promptList` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 16.5 | 8 - 25 | 4 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 16.5，观测区间 8 - 25，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
