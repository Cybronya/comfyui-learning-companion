---
name: image_to_image_sampler_checkpoint_vae_2
type: Image To Image
frequency: 4
level: weak
coverage: 0.975
common_nodes: [CheckpointLoaderSimple, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王017.三图融合-优化_2034659049958023169.json, 图片生成/图生图/Qwen-Image-Edit-Rapid-AIO_2091382579567087618.json, 图片生成/图生图/照片换角度（V0.1）_2019027166733803522.json, 图片生成/文生图/Qwen-Image-Edit-Rapid-AIO-图像编辑_1977650991560577025.json]
source: knowledge_consolidation
---

# image_to_image_sampler_checkpoint_vae_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王017.三图融合-优化_2034659049958023169.json、图片生成/图生图/Qwen-Image-Edit-Rapid-AIO_2091382579567087618.json、图片生成/图生图/照片换角度（V0.1）_2019027166733803522.json、图片生成/文生图/Qwen-Image-Edit-Rapid-AIO-图像编辑_1977650991560577025.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |
| 采样步数 | 12 | 4 - 30 | 4 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | sa_solver | - | 4 | 50% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 30，4 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 sa_solver，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
