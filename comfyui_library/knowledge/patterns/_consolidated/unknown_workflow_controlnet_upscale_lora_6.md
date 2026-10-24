---
name: unknown_workflow_controlnet_upscale_lora_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.778
common_nodes: [AILab_QwenVL, BasicScheduler, CFGGuider, CLIPLoader, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, Image Comparer (rgthree), ImageBlur, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PreviewImage, RandomNoise, SamplerCustom, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy positive, easy promptConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/二维码美化防检测_2083209367024922626.json, 图片生成/文生图/SD1.5-艺术二维码-二维码美化_2026877662597222401.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/二维码美化防检测_2083209367024922626.json、图片生成/文生图/SD1.5-艺术二维码-二维码美化_2026877662597222401.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `ImageBlur`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy positive`
- `easy promptConcat`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
