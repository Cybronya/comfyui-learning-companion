---
name: unknown_workflow_sampler_clip_unet_258
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8128
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, DeepTranslatorTextNode, DualCLIPLoader, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, FluxKontextImageScale, GetImageSize+, ImageConcanate, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, RH_LLMAPI_NODE, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext  基础单图编辑版_1943937775508815873.json, 图片生成/图生图/Kontext 一键扩图_1950452572160180226.json, 图片生成/图生图/🥎Kontext 一句话改变人物方向 自动润色版🤹_1938590655125839873.json, 图片生成/图生图/🥎【真王炸】Kontext 开源—单图编辑版🤹_1938440067062894593.json, 图片生成/图生图/🥎【真王炸】Kontext 开源—双图组合版🤹_1938440356646031361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_258

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext  基础单图编辑版_1943937775508815873.json、图片生成/图生图/Kontext 一键扩图_1950452572160180226.json、图片生成/图生图/🥎Kontext 一句话改变人物方向 自动润色版🤹_1938590655125839873.json、图片生成/图生图/🥎【真王炸】Kontext 开源—单图编辑版🤹_1938440067062894593.json、图片生成/图生图/🥎【真王炸】Kontext 开源—双图组合版🤹_1938440356646031361.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `DeepTranslatorTextNode`
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
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 4/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `Anything Everywhere` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImagePadForOutpaintMasked_UTK` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoadKontextPresets` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `SDXLPromptStyler` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
