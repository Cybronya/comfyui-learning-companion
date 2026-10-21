---
name: text_to_image_upscale_sampler_clip_34
type: Text To Image
frequency: 2
level: weak
coverage: 0.976
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, RH_LLMAPI_NODE, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageSize]
problems: []
missing: []
members: [图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_1996506151086866434.json, 图片生成/文生图/最强文生图-直出4K-Z-IMAGE-BASE_2021401918278471682.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图-直出4K-速度更快-效果更好Z-Image_1996506151086866434.json、图片生成/文生图/最强文生图-直出4K-Z-IMAGE-BASE_2021401918278471682.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Image Filter Adjustments` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1184 | - | 2 | 70% |
| 高度 | 1600 | - | 2 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 17.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1184，样本不足，未给区间，2 个样本
- 高度 中位数 1600，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
