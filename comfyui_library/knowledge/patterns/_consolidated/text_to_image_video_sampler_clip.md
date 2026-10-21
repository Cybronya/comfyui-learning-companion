---
name: text_to_image_video_sampler_clip
type: Text To Image
frequency: 6
level: moderate
coverage: 0.945
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, ImageOnlyCheckpointLoader, KSampler, SVD_img2vid_Conditioning, SaveImage, VAEDecode, VHS_VideoCombine, VideoLinearCFGGuidance]
problems: []
missing: []
members: [图片生成/文生图/高清产品摄影水果水下特写视频制作文生图_2069597159812591618.json, 视频生成/文生视频/1845741279811661826.json, 视频生成/文生视频/1792516752509292545.json, 视频生成/文生视频/1801584137573183489.json, 视频生成/文生视频/高清产品摄影水果视频制作_1782313135814782978.json, 视频生成/文生视频/1782653285233111041.json]
source: knowledge_consolidation
---

# text_to_image_video_sampler_clip

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/高清产品摄影水果水下特写视频制作文生图_2069597159812591618.json、视频生成/文生视频/1845741279811661826.json、视频生成/文生视频/1792516752509292545.json、视频生成/文生视频/1801584137573183489.json、视频生成/文生视频/高清产品摄影水果视频制作_1782313135814782978.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `SVD_img2vid_Conditioning`
- `SaveImage`
- `VAEDecode`
- `VHS_VideoCombine`
- `VideoLinearCFGGuidance`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `LoraLoader` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有
- `VAELoader` —— 3/6 个有
- `CLIPSetLastLayer` —— 2/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `UltimateSDUpscale` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 50 | 6 | 55% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 8 | 6 | 43% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | normal | - | 6 | 67% |
| 重绘幅度 | 1 | 0.4 - 1 | 6 | 75% |
| 宽度 | 640 | 640 - 1280 | 6 | 69% |
| 高度 | 864 | 512 - 1536 | 6 | 66% |
| LoRA 模型强度 | 0.65 | 0.65 - 0.8 | 3 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 50，6 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 8，6 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 normal，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，6 个样本
- 宽度 中位数 640，观测区间 640 - 1280，6 个样本
- 高度 中位数 864，观测区间 512 - 1536，6 个样本
- LoRA 模型强度 中位数 0.65，观测区间 0.65 - 0.8，3 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
