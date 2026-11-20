---
name: image_to_image_controlnet_sampler_clip_15
type: Image To Image
frequency: 2
level: weak
coverage: 0.7755
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [comfyui-workflow-templates-json/sd3.5_large_depth.json, 图片生成/图生图/【AI小王子】34.图生图openpose姿态预处理_2046786138668535809.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/sd3.5_large_depth.json、图片生成/图生图/【AI小王子】34.图生图openpose姿态预处理_2046786138668535809.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `6b0ed7ac-f476-44c9-9dad-b3f23ef985f8` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 86% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.75 | - | 2 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
