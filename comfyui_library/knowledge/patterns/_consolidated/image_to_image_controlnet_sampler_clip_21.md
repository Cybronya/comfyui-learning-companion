---
name: image_to_image_controlnet_sampler_clip_21
type: Image To Image
frequency: 2
level: weak
coverage: 0.8125
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, JjkText, KSampler, LoadImage, RH_Prompter, SaveImage, ShowText|pysssss, TextCombinerTwo, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/图生图（SDXL+CN）_1876881531909136385.json, 图片生成/图生图/最简工装照，一键生成_1889735921187676162.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图生图（SDXL+CN）_1876881531909136385.json、图片生成/图生图/最简工装照，一键生成_1889735921187676162.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `JjkText`
- `KSampler`
- `LoadImage`
- `RH_Prompter`
- `SaveImage`
- `ShowText|pysssss`
- `TextCombinerTwo`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `DF_Image_scale_to_side` —— 1/2 个有
- `DepthAnythingPreprocessor` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.53 | - | 2 | 34% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.3 | - | 2 | 73% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.39 | - | 2 | 51% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.53，样本不足，未给区间，2 个样本，取值分散，一致性仅 34%
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.3，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.39，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
