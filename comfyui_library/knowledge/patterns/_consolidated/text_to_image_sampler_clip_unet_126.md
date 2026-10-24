---
name: text_to_image_sampler_clip_unet_126
type: Text To Image
frequency: 5
level: strong
coverage: 0.9876
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image图生图-局部重绘_1994196646854672386.json, 图片生成/图生图/最新模型Z-image，秒杀FLUX2，图像反推_1994237148719235073.json, 图片生成/文生图/1文生图基础流_2025773663856893953.json, 图片生成/文生图/Z-image文生图+图生图+提示词反推_1994191793115824130.json, 图片生成/文生图/Z-image文生图-十个案例_1994576108777578497.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_126

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Z-image图生图-局部重绘_1994196646854672386.json、图片生成/图生图/最新模型Z-image，秒杀FLUX2，图像反推_1994237148719235073.json、图片生成/文生图/1文生图基础流_2025773663856893953.json、图片生成/文生图/Z-image文生图+图生图+提示词反推_1994191793115824130.json、图片生成/文生图/Z-image文生图-十个案例_1994576108777578497.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 4/5 个有
- `Joy_caption_two_load` —— 4/5 个有
- `MuyeTextEditOutput` —— 3/5 个有
- `Fast Groups Muter (rgthree)` —— 2/5 个有
- `MuyeLoadImage` —— 2/5 个有
- `InpaintModelConditioning` —— 1/5 个有
- `RH_Nano_Banana2_Image2Image` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 5 | 71% |
| 高度 | 1920 | 1080 - 1920 | 5 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，5 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，5 个样本
