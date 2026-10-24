---
name: image_to_image_controlnet_sampler_clip_19
type: Image To Image
frequency: 2
level: weak
coverage: 0.9645
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/传统controlnet加载器inpaint内补图生图扩图工作流（练习）_1965849915626819585.json, 图片生成/图生图/电商工作流_2070325171109580802.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/传统controlnet加载器inpaint内补图生图扩图工作流（练习）_1965849915626819585.json、图片生成/图生图/电商工作流_2070325171109580802.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `InpaintPreprocessor` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.475 | - | 2 | 74% |
| ControlNet 权重 | 0.925 | - | 2 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.475，样本不足，未给区间，2 个样本
- ControlNet 权重 中位数 0.925，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
