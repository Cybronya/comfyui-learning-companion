---
name: unknown_workflow_sampler_clip_unet_447
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9645
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/根据参考图修改图片_2016313387927478274.json, 图片生成/图生图/漫反射图案提取（klein2）_2077593751765209090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_447

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/根据参考图修改图片_2016313387927478274.json、图片生成/图生图/漫反射图案提取（klein2）_2077593751765209090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `1hew_TextListToString` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `DF_String_Concatenate` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PurgeVRAM_UTK` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `TextToLowercase` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
