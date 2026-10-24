---
name: unknown_workflow_controlnet_lora_sampler_35
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.696
common_nodes: [AnyLineArtPreprocessor_aux, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionLoader, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingV2Preprocessor, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageResize+, KSamplerSelect, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy promptConcat]
problems: []
missing: []
members: [图片生成/文生图/Flux_Redux风格迁移线稿+深度控制毛坯线稿出图_1960575042071519233.json, 视频生成/图生视频/自己用：图像转线稿_1960875231386767361.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux_Redux风格迁移线稿+深度控制毛坯线稿出图_1960575042071519233.json、视频生成/图生视频/自己用：图像转线稿_1960875231386767361.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSamplerSelect`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy promptConcat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
