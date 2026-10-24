---
name: text_to_image_upscale_sampler_clip_17
type: Text To Image
frequency: 7
level: moderate
coverage: 0.921
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, Image Comparer (rgthree), KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图转绘放大工作流_2065409794936238081.json, 图片生成/文生图/文生图基础款_2054007362377265154.json, 图片生成/文生图/文生图基础款（精致美女）_2055217694504431617.json, 图片生成/文生图/文生图：Qwen-image-Edite-Remix-AIO-v2.0_2045815282651893761.json, 图片生成/文生图/文生图：Qwen_2046105862854418434.json, 图片生成/文生图/文生图：真人_2047281640380047362.json, 视频生成/文生视频/文生图基础款_2037367917335027714.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图生图转绘放大工作流_2065409794936238081.json、图片生成/文生图/文生图基础款_2054007362377265154.json、图片生成/文生图/文生图基础款（精致美女）_2055217694504431617.json、图片生成/文生图/文生图：Qwen-image-Edite-Remix-AIO-v2.0_2045815282651893761.json、图片生成/文生图/文生图：Qwen_2046105862854418434.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 7 | 79% |
| 高度 | 1024 | 768 - 1536 | 7 | 75% |
| 采样步数 | 20 | 4 - 20 | 7 | 40% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 7 | 31% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | karras | - | 7 | 57% |
| 重绘幅度 | 1 | 0.7 - 1 | 7 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，7 个样本
- 高度 中位数 1024，观测区间 768 - 1536，7 个样本
- 采样步数 中位数 20，观测区间 4 - 20，7 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，7 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 karras，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，7 个样本，取值集中（一致性 89%）
