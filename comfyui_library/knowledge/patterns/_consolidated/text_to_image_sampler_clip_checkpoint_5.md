---
name: text_to_image_sampler_clip_checkpoint_5
type: Text To Image
frequency: 13
level: moderate
coverage: 0.928308
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json, 图片生成/文生图/SDLX1.0工作流_2065797462270504962.json, 图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json, 图片生成/文生图/SDXL文生图工作流_2101638559093575681.json, 图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json, 图片生成/文生图/hiresfix_esrgan双引擎图像放大_1959857918407553025.json, 图片生成/文生图/【遇见AI】基础放大方法之像素空间放大_2011366127523336193.json, 图片生成/文生图/冰雕世界_1792766439749373954.json, 图片生成/文生图/半透明膨胀沙发_1795724323667951617.json, 图片生成/文生图/基础CG图片高清放大工作流_2016839532573892610.json, 图片生成/文生图/文生图折纸_1788776494500212738.json, 平台全量/EPIC Space Scene_1862398770582585345.json, 平台全量/基础高清放大工作流_2016754898511073281.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json、图片生成/文生图/SDLX1.0工作流_2065797462270504962.json、图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json、图片生成/文生图/SDXL文生图工作流_2101638559093575681.json、图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 11/13 个有
- `UpscaleModelLoader` —— 11/13 个有
- `VAEEncode` —— 7/13 个有
- `LoraLoader` —— 6/13 个有
- `PreviewImage` —— 5/13 个有
- `VAELoader` —— 3/13 个有
- `ImageScale` —— 2/13 个有
- `LatentPixelScale` —— 2/13 个有
- `UltimateSDUpscale` —— 2/13 个有
- `ColorCorrect` —— 1/13 个有
- `ImageScaleBy` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 50 | 13 | 63% |
| Prompt 约束强度(CFG) | 8 | 5 - 8 | 13 | 86% |
| 采样算法 | dpmpp_2m | - | 13 | 46% |
| 调度器 | karras | - | 13 | 62% |
| 重绘幅度 | 1 | 0.06 - 1 | 13 | 65% |
| 宽度 | 768 | 512 - 1024 | 13 | 79% |
| 高度 | 768 | 512 - 1280 | 13 | 73% |
| LoRA 模型强度 | 0.58 | 0.5 - 1 | 6 | 70% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 50，13 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 8，13 个样本，取值集中（一致性 86%）
- 采样算法 最常用 dpmpp_2m，13 个样本，一致性 46%
- 调度器 最常用 karras，13 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.06 - 1，13 个样本
- 宽度 中位数 768，观测区间 512 - 1024，13 个样本
- 高度 中位数 768，观测区间 512 - 1280，13 个样本
- LoRA 模型强度 中位数 0.58，观测区间 0.5 - 1，6 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 0.06，低于常用下限 0.1（）
