---
name: text_to_image_sampler_clip_checkpoint_12
type: Text To Image
frequency: 7
level: moderate
coverage: 0.880286
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【RICK】肖像大师高清版(模特生成)_1906519526463442946.json, 图片生成/文生图/图像细节放大_2012407929160343554.json, 图片生成/文生图/小易第一课 工作流搭建【20260527】_2060680098830962690.json, 图片生成/文生图/文生图SD-XL基础工作流_2029187667841257473.json, 图片生成/文生图/文生图_2046755529770405889.json, 图片生成/文生图/文生图基础款_1990029530519793666.json, 图片生成/文生图/清晰_2013889963875639297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/【RICK】肖像大师高清版(模特生成)_1906519526463442946.json、图片生成/文生图/图像细节放大_2012407929160343554.json、图片生成/文生图/小易第一课 工作流搭建【20260527】_2060680098830962690.json、图片生成/文生图/文生图SD-XL基础工作流_2029187667841257473.json、图片生成/文生图/文生图_2046755529770405889.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `LatentUpscaleBy` —— 4/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `LatentUpscale` —— 1/7 个有
- `Lora Loader` —— 1/7 个有
- `PortraitMaster_中文版` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 7 | 82% |
| 高度 | 768 | 512 - 1280 | 7 | 66% |
| 采样步数 | 25 | 20 - 40 | 7 | 74% |
| Prompt 约束强度(CFG) | 8 | 6.5 - 8 | 7 | 92% |
| 采样算法 | euler | - | 7 | 43% |
| 调度器 | karras | - | 7 | 57% |
| 重绘幅度 | 1 | 0.5 - 1 | 7 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，7 个样本，取值集中（一致性 82%）
- 高度 中位数 768，观测区间 512 - 1280，7 个样本
- 采样步数 中位数 25，观测区间 20 - 40，7 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 6.5 - 8，7 个样本，取值集中（一致性 92%）
- 采样算法 最常用 euler，7 个样本，一致性 43%
- 调度器 最常用 karras，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，7 个样本
