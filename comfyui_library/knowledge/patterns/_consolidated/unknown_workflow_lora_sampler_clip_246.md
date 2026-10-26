---
name: unknown_workflow_lora_sampler_clip_246
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9635
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, Flux2Scheduler, ImageAndMaskPreview, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_Translator, RandomNoise, ReferenceLatent, ResizeImagesByLongerEdge, SAM3Segment, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/4.精准改图编辑_2050624023272402945.json, 图片生成/图生图/6.去除物体_2050758953088368641.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_246

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/4.精准改图编辑_2050624023272402945.json、图片生成/图生图/6.去除物体_2050758953088368641.json）

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
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImageAndMaskPreview`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `ResizeImagesByLongerEdge`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatchToReference` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `INPAINT_ExpandMask` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
