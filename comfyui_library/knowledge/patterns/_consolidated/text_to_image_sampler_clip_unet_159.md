---
name: text_to_image_sampler_clip_unet_159
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9195
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商洗海报宣传图，排版文字工作流_1978005353789018113.json, 图片生成/文生图/Qwen出图_1955863541137985538.json, 图片生成/文生图/Z-image-base 反推提示词文生图_2016442671014875137.json, 图片生成/文生图/反推提示词-生图-百度-ERNIE-Image_2044624422065147906.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/电商洗海报宣传图，排版文字工作流_1978005353789018113.json、图片生成/文生图/Qwen出图_1955863541137985538.json、图片生成/文生图/Z-image-base 反推提示词文生图_2016442671014875137.json、图片生成/文生图/反推提示词-生图-百度-ERNIE-Image_2044624422065147906.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `ImageScaleDownToSize` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `AILab_MiniCPM_4_V` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `ImageGetSize` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 960 | 512 - 1024 | 4 | 76% |
| 高度 | 1408 | 512 - 1536 | 4 | 65% |
| 采样步数 | 25 | 20 - 35 | 4 | 79% |
| Prompt 约束强度(CFG) | 3.75 | 3.5 - 4 | 4 | 93% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 960，观测区间 512 - 1024，4 个样本
- 高度 中位数 1408，观测区间 512 - 1536，4 个样本
- 采样步数 中位数 25，观测区间 20 - 35，4 个样本
- Prompt 约束强度(CFG) 中位数 3.75，观测区间 3.5 - 4，4 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
