---
name: image_to_image_sampler_clip_unet_139
type: Image To Image
frequency: 3
level: moderate
coverage: 0.77
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen千问图生图，可生成中文，对标即梦_1952646987956043778.json, 图片生成/图生图/Qwen图生图_洗图+8步出图+教程说明_1959149285885554689.json, 图片生成/图生图/千问image图生图-洗图_1973967994604883970.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_139

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen千问图生图，可生成中文，对标即梦_1952646987956043778.json、图片生成/图生图/Qwen图生图_洗图+8步出图+教程说明_1959149285885554689.json、图片生成/图生图/千问image图生图-洗图_1973967994604883970.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LatentUpscale` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ImagePadKJ` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 20 | 3 | 78% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 4 | 3 | 76% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.4 - 0.5 | 3 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.4 - 0.5，3 个样本，取值集中（一致性 90%）
