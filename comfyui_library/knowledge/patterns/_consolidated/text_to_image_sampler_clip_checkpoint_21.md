---
name: text_to_image_sampler_clip_checkpoint_21
type: Text To Image
frequency: 3
level: strong
coverage: 0.911667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/生成人物图像(肖像大师）_2076571370456182786.json, 图片生成/文生图/肖像大师-根据提示词生成人物肖像_2061354886461218818.json, 视频生成/文生视频/文生图基础款_2037367917335027714.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/生成人物图像(肖像大师）_2076571370456182786.json、图片生成/文生图/肖像大师-根据提示词生成人物肖像_2061354886461218818.json、视频生成/文生视频/文生图基础款_2037367917335027714.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PortraitMaster_中文版` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1280 | 1024 - 1280 | 3 | 90% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 3 | 94% |
| 采样算法 | dpmpp_2m | - | 3 | 33% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，3 个样本，取值集中（一致性 94%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 33%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
