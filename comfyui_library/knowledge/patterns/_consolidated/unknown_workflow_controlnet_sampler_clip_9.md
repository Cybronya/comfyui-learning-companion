---
name: unknown_workflow_controlnet_sampler_clip_9
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8574
common_nodes: [ApplyFluxControlNet, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, LoadFluxControlNet, LoadImage, ModelSamplingFlux, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/Flux 图生图 CN 三合一_1877296086783094785.json, 图片生成/图生图/flux-controlnet-depth-v3_1827249410790313985.json, 图片生成/图生图/flux-controlnet-hed-v3_1827932519047286786.json, 图片生成/图生图/图生图flux-controlnet-canny-v3_1827231381591126017.json, 平台全量/Flux. Watercolor Storybook Style – Characters_Scen_1889576178997518338.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux 图生图 CN 三合一_1877296086783094785.json、图片生成/图生图/flux-controlnet-depth-v3_1827249410790313985.json、图片生成/图生图/flux-controlnet-hed-v3_1827932519047286786.json、图片生成/图生图/图生图flux-controlnet-canny-v3_1827231381591126017.json、平台全量/Flux. Watercolor Storybook Style – Characters_Scen_1889576178997518338.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyFluxControlNet`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `LoadFluxControlNet`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 4/5 个有
- `DepthAnything_V2` —— 3/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/5 个有
- `CannyEdgePreprocessor` —— 2/5 个有
- `HEDPreprocessor` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
