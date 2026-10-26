---
name: image_to_image_controlnet_sampler_clip_7
type: Image To Image
frequency: 5
level: strong
coverage: 0.8162
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, KSampler, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json, 图片生成/文生图/Qwen终极文生图及CN控制网_1961095516283191298.json, 图片生成/文生图/qwen image instant union_1960550214228672513.json, 图片生成/文生图/千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946.json, 图片生成/文生图/🦖QWen-Image Controlnet多合一生图_1961690453156499458.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json、图片生成/文生图/Qwen终极文生图及CN控制网_1961095516283191298.json、图片生成/文生图/qwen image instant union_1960550214228672513.json、图片生成/文生图/千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946.json、图片生成/文生图/🦖QWen-Image Controlnet多合一生图_1961690453156499458.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
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
- `AIO_Preprocessor` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `Canny` —— 3/5 个有
- `ImageScaleDownToSize` —— 3/5 个有
- `ImageStitch` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `DepthAnything_V2` —— 1/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/5 个有
- `NunchakuQwenImageDiTLoader` —— 1/5 个有
- `PMRF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 1 | 0.8 - 1 | 5 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 92%）
