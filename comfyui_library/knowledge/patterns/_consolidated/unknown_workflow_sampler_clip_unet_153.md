---
name: unknown_workflow_sampler_clip_unet_153
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.818111
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, DualCLIPLoader, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, FluxKontextImageScale, GetImageSize+, ImageConcanate, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext  基础单图编辑版_1943937775508815873.json, 图片生成/图生图/Kontext 一键扩图_1950452572160180226.json, 图片生成/图生图/🥎Kontext 一句话改变人物方向 自动润色版🤹_1938590655125839873.json, 图片生成/图生图/🥎【真王炸】Kontext 开源—单图编辑版🤹_1938440067062894593.json, 图片生成/图生图/🥎【真王炸】Kontext 开源—双图组合版🤹_1938440356646031361.json, 平台全量/Kontext Dev-单图编辑V2.3_1941487840805208065.json, 平台全量/Kontext Dev-扩图_1946130484546203649.json, 平台全量/Kontext 开源—单图编辑版_1950030604827017218.json, 平台全量/Kontext 开源—双图组合版_1950029306611326978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Kontext  基础单图编辑版_1943937775508815873.json、图片生成/图生图/Kontext 一键扩图_1950452572160180226.json、图片生成/图生图/🥎Kontext 一句话改变人物方向 自动润色版🤹_1938590655125839873.json、图片生成/图生图/🥎【真王炸】Kontext 开源—单图编辑版🤹_1938440067062894593.json、图片生成/图生图/🥎【真王炸】Kontext 开源—双图组合版🤹_1938440356646031361.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `ImageConcanate`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 8/9 个有
- `RH_LLMAPI_NODE` —— 8/9 个有
- `easy showAnything` —— 7/9 个有
- `GetNode` —— 3/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 3/9 个有
- `LoraLoader` —— 3/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `RH_Captioner` —— 3/9 个有
- `SDXLPromptStyler` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `UltimateSDUpscale` —— 3/9 个有
- `UpscaleModelLoader` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `Anything Everywhere` —— 2/9 个有
- `EmptyImage` —— 2/9 个有
- `ImagePadForOutpaintMasked_UTK` —— 2/9 个有
- `ImpactInt` —— 2/9 个有
- `LoadKontextPresets` —— 2/9 个有
- `Any Switch (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
