---
name: unknown_workflow_sampler_clip_unet_386
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.966667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux基础图片生成+图片放大_1948919650907238402.json, 图片生成/文生图/Flux完整版文生图-在线生图【SirenYi】_1907035068605292545.json, 图片生成/文生图/Flux文生图+控制+换脸+放大_1948911760146345986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_386

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux基础图片生成+图片放大_1948919650907238402.json、图片生成/文生图/Flux完整版文生图-在线生图【SirenYi】_1907035068605292545.json、图片生成/文生图/Flux文生图+控制+换脸+放大_1948911760146345986.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 2/3 个有
- `DeepTranslatorTextNode` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `UltimateSDUpscale` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `easy int` —— 2/3 个有
- `ACN_AdvancedControlNetApplySingle_v2` —— 1/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ApplyPulidFlux` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `InstantIDFaceAnalysis` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PulidFluxEvaClipLoader` —— 1/3 个有
- `PulidFluxModelLoader` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 3 | 65% |
| 高度 | 512 | 512 - 1024 | 3 | 65% |
| ControlNet 权重 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，3 个样本
- 高度 中位数 512，观测区间 512 - 1024，3 个样本
