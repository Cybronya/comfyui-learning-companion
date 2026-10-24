---
name: text_to_image_sampler_clip_checkpoint_8
type: Text To Image
frequency: 10
level: moderate
coverage: 0.9423
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json, 图片生成/文生图/SDLX1.0工作流_2065797462270504962.json, 图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json, 图片生成/文生图/SDXL文生图工作流_2101638559093575681.json, 图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json, 图片生成/文生图/hiresfix_esrgan双引擎图像放大_1959857918407553025.json, 图片生成/文生图/【遇见AI】基础放大方法之像素空间放大_2011366127523336193.json, 图片生成/文生图/冰雕世界_1792766439749373954.json, 图片生成/文生图/半透明膨胀沙发_1795724323667951617.json, 图片生成/文生图/基础CG图片高清放大工作流_2016839532573892610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json、图片生成/文生图/SDLX1.0工作流_2065797462270504962.json、图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json、图片生成/文生图/SDXL文生图工作流_2101638559093575681.json、图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 8/10 个有
- `UpscaleModelLoader` —— 8/10 个有
- `VAEEncode` —— 5/10 个有
- `LoraLoader` —— 4/10 个有
- `PreviewImage` —— 3/10 个有
- `VAELoader` —— 2/10 个有
- `ImageScale` —— 1/10 个有
- `ImageScaleBy` —— 1/10 个有
- `LatentPixelScale` —— 1/10 个有
- `UltimateSDUpscale` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 50 | 10 | 60% |
| Prompt 约束强度(CFG) | 8 | 6.5 - 8 | 10 | 93% |
| 采样算法 | dpmpp_2m | - | 10 | 50% |
| 调度器 | karras | - | 10 | 70% |
| 重绘幅度 | 1 | 0.6 - 1 | 10 | 86% |
| 宽度 | 768 | 512 - 1024 | 10 | 78% |
| 高度 | 896 | 512 - 1280 | 10 | 73% |
| LoRA 模型强度 | 0.58 | 0.55 - 1 | 4 | 72% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 6.5 - 8，10 个样本，取值集中（一致性 93%）
- 采样算法 最常用 dpmpp_2m，10 个样本，一致性 50%
- 调度器 最常用 karras，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，10 个样本，取值集中（一致性 86%）
- 宽度 中位数 768，观测区间 512 - 1024，10 个样本
- 高度 中位数 896，观测区间 512 - 1280，10 个样本
- LoRA 模型强度 中位数 0.58，观测区间 0.55 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
