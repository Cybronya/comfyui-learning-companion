---
name: text_to_image_controlnet_upscale_sampler_7
type: Text To Image
frequency: 2
level: weak
coverage: 0.8175
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, EmptyLatentImage, Image Comparer (rgthree), ImageResizeKJ, KSampler, LayerUtility: Florence2Image2Prompt, LoadImage, PreviewImage, SaveImage, ShowText|pysssss, StyleModelApply, StyleModelLoader, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX毛坯房一键出图_1920132831186718722.json, 平台全量/毛胚房转精装修【AI小王子】_1912393100894109698.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_sampler_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FLUX毛坯房一键出图_1920132831186718722.json、平台全量/毛胚房转精装修【AI小王子】_1912393100894109698.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `KSampler`
- `LayerUtility: Florence2Image2Prompt`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `LoadFlorence2Model` —— 1/2 个有
- `PromptComposerMerge` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.7 | - | 2 | 86% |
| 宽度 | 940 | - | 2 | 54% |
| 高度 | 640 | - | 2 | 80% |
| ControlNet 权重 | 0.95 | - | 2 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 宽度 中位数 940，样本不足，未给区间，2 个样本
- 高度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- ControlNet 权重 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
