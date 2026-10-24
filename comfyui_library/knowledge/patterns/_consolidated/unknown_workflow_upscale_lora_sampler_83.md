---
name: unknown_workflow_upscale_lora_sampler_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.759
common_nodes: [Anything Everywhere3, BasicScheduler, CFGGuider, CLIPTextEncodeFlux, CR Latent Input Switch, CR Prompt List, ConditioningZeroOut, DetailDaemonSamplerNode, DualCLIPLoader, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, GetNode, ImageResizeKJv2, KSamplerSelect, LayerUtility: ImageBlendAdvance, LoadImage, LoraLoaderModelOnly, Preview Chooser, PrimitiveFloat, PrimitiveInt, Prompts Everywhere, RH_Translator, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, Save Text File, SaveImage, SetNode, ShowText|pysssss, StringConcatenate, Text To Image (mtb), UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_DuplicateLatents, easy imageConcat, easy imageSize, easy textIndexSwitch, ttN concat, ttN text]
problems: []
missing: []
members: [图片生成/图生图/Flux_图生图_1936997360503279618.json, 图片生成/文生图/Flux_文生图_1937002317839257602.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux_图生图_1936997360503279618.json、图片生成/文生图/Flux_文生图_1937002317839257602.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncodeFlux`
- `CR Latent Input Switch`
- `CR Prompt List`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Preview Chooser`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Prompts Everywhere`
- `RH_Translator`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `Save Text File`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StringConcatenate`
- `Text To Image (mtb)`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_DuplicateLatents`
- `easy imageConcat`
- `easy imageSize`
- `easy textIndexSwitch`
- `ttN concat`
- `ttN text`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768x1344 (0.57) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 768x1344 (0.57)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
