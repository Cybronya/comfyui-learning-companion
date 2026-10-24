---
name: text_to_image_controlnet_sampler_clip_22
type: Text To Image
frequency: 2
level: weak
coverage: 0.893
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, EmptyLatentImage, ImageResize+, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, Zoe-DepthMapPreprocessor]
problems: []
missing: []
members: [图片生成/图生图/10s照片转色彩头像_1891801702159298561.json, 图片生成/文生图/文生图+CN_Depth_Openpose_1778002614114390018.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/10s照片转色彩头像_1891801702159298561.json、图片生成/文生图/文生图+CN_Depth_Openpose_1778002614114390018.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `EmptyLatentImage`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `Zoe-DepthMapPreprocessor`

**可变部分**（部分 workflow 才有）：
- `IPAdapter` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.825 | - | 2 | 97% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7.495 | - | 2 | 93% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.73 | - | 2 | 63% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.825，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7.495，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.73，样本不足，未给区间，2 个样本
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
