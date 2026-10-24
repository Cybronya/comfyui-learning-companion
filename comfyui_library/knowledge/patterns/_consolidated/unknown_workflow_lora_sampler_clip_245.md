---
name: unknown_workflow_lora_sampler_clip_245
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.883
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EasyCache, FluxGuidance, GetNode, ImpactInt, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, ResizeImageMixlab, SamplerCustomAdvanced, SaveImage, SetNode, SimpleMath+, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/flux.2 (Klein)-增加图片细节_2012729777114849282.json, 图片生成/图生图/flux.2单图编辑_2013969319683690498.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_245

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux.2 (Klein)-增加图片细节_2012729777114849282.json、图片生成/图生图/flux.2单图编辑_2013969319683690498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EasyCache`
- `FluxGuidance`
- `GetNode`
- `ImpactInt`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `ResizeImageMixlab`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `DiffusionModelLoaderKJ` —— 1/2 个有
- `GGUFLoaderKJ` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LyingSigmaSampler` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
