---
name: text_to_image_controlnet_sampler_clip_32
type: Text To Image
frequency: 2
level: weak
coverage: 0.7595
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, PreviewImage, SaveImage, Seed (rgthree), VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/文生图/工作流基础系列21-SDXL文生图_图生图工作流_2049633890658209794.json, 图片生成/文生图/工作流基础系列22-SD1.5文生图_图生图_ControlNet工作流_2047955233560596481.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/工作流基础系列21-SDXL文生图_图生图工作流_2049633890658209794.json、图片生成/文生图/工作流基础系列22-SD1.5文生图_图生图_ControlNet工作流_2047955233560596481.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7.5 | - | 2 | 93% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.635 | - | 2 | 79% |
| ControlNet 权重 | 0.8 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.635，样本不足，未给区间，2 个样本
- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
