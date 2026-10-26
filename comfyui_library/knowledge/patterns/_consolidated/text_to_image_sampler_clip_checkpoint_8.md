---
name: text_to_image_sampler_clip_checkpoint_8
type: Text To Image
frequency: 10
level: moderate
coverage: 0.98
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json, 图片生成/文生图/SDLX1.0工作流_2065797462270504962.json, 图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json, 图片生成/文生图/SDXL文生图工作流_2101638559093575681.json, 图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json, 图片生成/文生图/hiresfix_esrgan双引擎图像放大_1959857918407553025.json, 图片生成/文生图/冰雕世界_1792766439749373954.json, 图片生成/文生图/半透明膨胀沙发_1795724323667951617.json, 图片生成/文生图/文生图折纸_1788776494500212738.json, 图片生成/文生图/艺术品高清图-青花龙_1778063653963108354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json、图片生成/文生图/SDLX1.0工作流_2065797462270504962.json、图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json、图片生成/文生图/SDXL文生图工作流_2101638559093575681.json、图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：98%

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
- `VAEEncode` —— 7/10 个有
- `LoraLoader` —— 6/10 个有
- `PreviewImage` —— 2/10 个有
- `ImageScale` —— 1/10 个有
- `ImageScaleBy` —— 1/10 个有
- `VAELoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 50 | 10 | 49% |
| Prompt 约束强度(CFG) | 8 | 2 - 8 | 10 | 75% |
| 采样算法 | dpmpp_2m | - | 10 | 30% |
| 调度器 | karras | - | 10 | 60% |
| 重绘幅度 | 1 | 0.3 - 1 | 10 | 67% |
| 宽度 | 768 | 512 - 1024 | 10 | 75% |
| 高度 | 896 | 640 - 1280 | 10 | 75% |
| LoRA 模型强度 | 0.555 | 0.5 - 1 | 6 | 72% |
| LoRA 文本强度 | 1 | 0.3 - 1 | 6 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 50，10 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 8，观测区间 2 - 8，10 个样本
- 采样算法 最常用 dpmpp_2m，10 个样本，一致性 30%
- 调度器 最常用 karras，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，10 个样本
- 宽度 中位数 768，观测区间 512 - 1024，10 个样本
- 高度 中位数 896，观测区间 640 - 1280，10 个样本
- LoRA 模型强度 中位数 0.555，观测区间 0.5 - 1，6 个样本
- LoRA 文本强度 中位数 1，观测区间 0.3 - 1，6 个样本
