---
name: image_to_image_sampler_clip_unet_150
type: Image To Image
frequency: 4
level: moderate
coverage: 0.784
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen千问图生图，可生成中文，对标即梦_1952646987956043778.json, 图片生成/图生图/Qwen图生图_洗图+8步出图+教程说明_1959149285885554689.json, 图片生成/图生图/千问image图生图-洗图_1973967994604883970.json, 图片生成/图生图/洗图去ai+放大_1998033674337681409.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen千问图生图，可生成中文，对标即梦_1952646987956043778.json、图片生成/图生图/Qwen图生图_洗图+8步出图+教程说明_1959149285885554689.json、图片生成/图生图/千问image图生图-洗图_1973967994604883970.json、图片生成/图生图/洗图去ai+放大_1998033674337681409.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `LatentUpscale` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ImagePadKJ` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 12 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 58% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.45 | 0.27 - 0.5 | 4 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 12 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.45，观测区间 0.27 - 0.5，4 个样本
