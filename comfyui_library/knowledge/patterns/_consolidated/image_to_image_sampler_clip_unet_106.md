---
name: image_to_image_sampler_clip_unet_106
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9728
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/自用美女_1963796521585299457.json, 图片生成/文生图/芝麻街特效_2073346446350442497.json, 图片生成/文生图/质感提升kontext工作流万物提升_1985614052636479490.json, 视频生成/图生视频/FLUX kontext 开源模型 工作流_1937024075837640705.json, 视频生成/图生视频/Flux 去除马赛克_1994289242960576513.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_106

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/自用美女_1963796521585299457.json、图片生成/文生图/芝麻街特效_2073346446350442497.json、图片生成/文生图/质感提升kontext工作流万物提升_1985614052636479490.json、视频生成/图生视频/FLUX kontext 开源模型 工作流_1937024075837640705.json、视频生成/图生视频/Flux 去除马赛克_1994289242960576513.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `FluxKontextImageScale` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `LoraLoader` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RepeatLatentBatch` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 5 | 92% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
