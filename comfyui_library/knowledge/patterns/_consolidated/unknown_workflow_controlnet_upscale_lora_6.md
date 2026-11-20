---
name: unknown_workflow_controlnet_upscale_lora_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.703
common_nodes: [Anything Everywhere, Anything Everywhere3, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Upscale Image, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DeepTranslatorTextNode, DetailDaemonSamplerNode, DualCLIPLoader, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageResize+, ImageResizeKJ, ImageScaleBy, ImageTile+, ImageUntile+, ImageUpscaleWithModel, ImpactInt, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MultiplySigmas, PreviewImage, RH_Captioner, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, SetNode, ShowText|pysssss, UNETLoader, UltimateSDUpscaleCustomSample, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/全能高清放大-超好用_1895347981006798850.json, 图片生成/图生图/全能高清放大-非常好用_1913291379412299778.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/全能高清放大-超好用_1895347981006798850.json、图片生成/图生图/全能高清放大-非常好用_1913291379412299778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DeepTranslatorTextNode`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageTile+`
- `ImageUntile+`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MultiplySigmas`
- `PreviewImage`
- `RH_Captioner`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.12 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
