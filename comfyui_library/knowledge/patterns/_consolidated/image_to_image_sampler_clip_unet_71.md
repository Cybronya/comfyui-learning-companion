---
name: image_to_image_sampler_clip_unet_71
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9055
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein图生图工作流_2061337284183683073.json, 图片生成/图生图/Klein + Zimage图像细化+放大_2093345706391195650.json, 图片生成/图生图/Qwen-Image图生图3D孙悟空_1954028272784953345.json, 图片生成/图生图/Qwen-Image图生图_1953321268298874882.json, 图片生成/图生图/工作流千问篇2-Qwen千问图生图-国产大模型之光_2022219062620721153.json, 图片生成/文生图/千问洗图图生图工作流_1988906774222737410.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_71

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2-klein图生图工作流_2061337284183683073.json、图片生成/图生图/Klein + Zimage图像细化+放大_2093345706391195650.json、图片生成/图生图/Qwen-Image图生图3D孙悟空_1954028272784953345.json、图片生成/图生图/Qwen-Image图生图_1953321268298874882.json、图片生成/图生图/工作流千问篇2-Qwen千问图生图-国产大模型之光_2022219062620721153.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `UnetLoaderGGUF` —— 3/6 个有
- `ClipInterrogator` —— 2/6 个有
- `JWImageResizeByLongerSide` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `CLIPLoaderGGUF` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 20 | 6 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.625 | 0.2 - 1 | 6 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 20，6 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.625，观测区间 0.2 - 1，6 个样本
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
