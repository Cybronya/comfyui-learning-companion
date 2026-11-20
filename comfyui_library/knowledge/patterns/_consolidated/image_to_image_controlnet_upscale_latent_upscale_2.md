---
name: image_to_image_controlnet_upscale_latent_upscale_2
type: Image To Image
frequency: 3
level: moderate
coverage: 0.762333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, ImageScale, KSampler, LatentUpscale, LoadImage, PreviewImage, ReActorFaceSwap, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/老照片修复神器_1910535592873263105.json, 平台全量/旧照片修复_1890361725483667458.json, 平台全量/老照片修复_1904204636566228993.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_latent_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/老照片修复神器_1910535592873263105.json、平台全量/旧照片修复_1890361725483667458.json、平台全量/老照片修复_1904204636566228993.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ImageScale`
- `KSampler`
- `LatentUpscale`
- `LoadImage`
- `PreviewImage`
- `ReActorFaceSwap`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `LeReS-DepthMapPreprocessor` —— 2/3 个有
- `LineArtPreprocessor` —— 2/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 7.5 | 2 - 7.5 | 3 | 54% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.7 | 3 | 93% |
| ControlNet 权重 | 0.3 | 0 - 0.4 | 3 | 27% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 2 - 7.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.7，3 个样本，取值集中（一致性 93%）
- ControlNet 权重 中位数 0.3，观测区间 0 - 0.4，3 个样本，取值分散，一致性仅 27%
