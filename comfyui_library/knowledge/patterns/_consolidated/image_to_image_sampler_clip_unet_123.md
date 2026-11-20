---
name: image_to_image_sampler_clip_unet_123
type: Image To Image
frequency: 4
level: weak
coverage: 0.8405
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/服装3D展示flux_2045420200736067586.json, 图片生成/图生图/（官方版）Qwen Image图生图V1（文字自动修复）_1953048270995189762.json, 图片生成/文生图/Qwen Image Layered 分层模型_2003650272847118337.json, 图片生成/文生图/Qwen Image Layered千问分层文生_图生一体流_2002200397173387266.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_123

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/服装3D展示flux_2045420200736067586.json、图片生成/图生图/（官方版）Qwen Image图生图V1（文字自动修复）_1953048270995189762.json、图片生成/文生图/Qwen Image Layered 分层模型_2003650272847118337.json、图片生成/文生图/Qwen Image Layered千问分层文生_图生一体流_2002200397173387266.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `EmptyHunyuanLatentVideo` —— 2/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `LatentCutToBatch` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `LatentFromBatch` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 5 - 40 | 4 | 25% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 4 | 4 | 42% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 0.3 - 1 | 4 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 5 - 40，4 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 4，4 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
