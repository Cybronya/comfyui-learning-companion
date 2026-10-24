---
name: image_to_image_sampler_clip_vae_28
type: Image To Image
frequency: 6
level: moderate
coverage: 0.925
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/图生图训练模板_2042065010142224385.json, 图片生成/图生图/工作流基础篇-3-基础图生图工作流（写实和动漫双风格）_2012422631575785474.json, 图片生成/图生图/简单图生图_2034160543371628545.json, 图片生成/图生图/自动化妆2_Automatic makeup2_img2img_1911604879872225281.json, 图片生成/图生图/自动化妆_细节增强器_1896904379117772802.json, 图片生成/文生图/文生图基础款_1983414020642381826.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_28

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/图生图训练模板_2042065010142224385.json、图片生成/图生图/工作流基础篇-3-基础图生图工作流（写实和动漫双风格）_2012422631575785474.json、图片生成/图生图/简单图生图_2034160543371628545.json、图片生成/图生图/自动化妆2_Automatic makeup2_img2img_1911604879872225281.json、图片生成/图生图/自动化妆_细节增强器_1896904379117772802.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 5/6 个有
- `LoraLoader` —— 2/6 个有
- `CheckpointLoaderSimple_Any` —— 1/6 个有
- `Image Compare (mtb)` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 24 | 6 | 91% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 6 | 100% |
| 采样算法 | dpmpp_2m | - | 6 | 33% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 0.5 | 0.24 - 1 | 6 | 57% |
| LoRA 模型强度 | 0.5 | - | 2 | 0% |
| LoRA 文本强度 | 0.7 | - | 2 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 24，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 0.5，观测区间 0.24 - 1，6 个样本
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- LoRA 文本强度 中位数 0.7，样本不足，未给区间，2 个样本
