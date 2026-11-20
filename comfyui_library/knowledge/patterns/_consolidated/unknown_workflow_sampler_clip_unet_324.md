---
name: unknown_workflow_sampler_clip_unet_324
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.858
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Flux2Scheduler, FluxKontextImageScale, ImageScaleBy, KSamplerSelect, LoadImage, PreviewAny, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy positive]
problems: []
missing: []
members: [图片生成/图生图/F2klein沙发白底图与室内场景图融合工作流_2060871504107237377.json, 图片生成/图生图/Flux2-klein-风格转换_2027976064428937217.json, 平台全量/flux2-klein-万能风格转换器_2026559394309214209.json, 平台全量/flux2-klein-产品静物摄影师-虚拟摄影工作室_2021222484376297474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_324

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/F2klein沙发白底图与室内场景图融合工作流_2060871504107237377.json、图片生成/图生图/Flux2-klein-风格转换_2027976064428937217.json、平台全量/flux2-klein-万能风格转换器_2026559394309214209.json、平台全量/flux2-klein-产品静物摄影师-虚拟摄影工作室_2021222484376297474.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `FluxKontextImageScale`
- `ImageScaleBy`
- `KSamplerSelect`
- `LoadImage`
- `PreviewAny`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `SamplerEulerAncestral` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RMBG` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `WujiStyleSelector` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy promptConcat` —— 2/4 个有
- `CFGNorm` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `DetailDaemonSamplerNode` —— 1/4 个有
- `Florence2ModelLoader` —— 1/4 个有
- `Florence2Run` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `Int` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `PreviewBridge` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `SamplerCustom` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
