---
name: image_to_image_controlnet_sampler_clip_18
type: Image To Image
frequency: 3
level: strong
coverage: 0.958667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, ControlNetLoader, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/传统controlnet加载器inpaint内补图生图扩图工作流（练习）_1965849915626819585.json, 图片生成/图生图/电商工作流_2070325171109580802.json, 平台全量/人像妆容_1778058323459903490.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/传统controlnet加载器inpaint内补图生图扩图工作流（练习）_1965849915626819585.json、图片生成/图生图/电商工作流_2070325171109580802.json、平台全量/人像妆容_1778058323459903490.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Canny` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CLIPSetLastLayer` —— 1/3 个有
- `DF_Text_Box` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `InpaintPreprocessor` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `SDXLResolutionPresets` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.36 | 0.35 - 0.6 | 3 | 74% |
| ControlNet 权重 | 1 | 0.85 - 1 | 3 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.36，观测区间 0.35 - 0.6，3 个样本
- ControlNet 权重 中位数 1，观测区间 0.85 - 1，3 个样本，取值集中（一致性 93%）
