---
name: image_to_image_sampler_clip_checkpoint_13
type: Image To Image
frequency: 2
level: weak
coverage: 0.806
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ICLightConditioning, KSampler, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/IC-Light V2官方工作流_1930184992649854977.json, 图片生成/图生图/iclight1.5打光_1904110598605676545.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/IC-Light V2官方工作流_1930184992649854977.json、图片生成/图生图/iclight1.5打光_1904110598605676545.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ICLightConditioning`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CreateShapeMask` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `MaskBlur+` —— 1/2 个有
- `RemapMaskRange` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 5.025 | - | 2 | 41% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.97 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 5.025，样本不足，未给区间，2 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.97，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
