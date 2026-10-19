---
name: unknown_workflow_sampler_clip_unet_94
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.754
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), ImageColorMatch+, JjkText, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PlaySound|pysssss, PreviewAny, PreviewImage, Qwen3VL_Chat, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107037189610762241.json, 图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107090731931361281.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107037189610762241.json、图片生成/图生图/图片风格迁移转化 • 灵感造像师：实现像素级保留与灵魂级风格注入生成器_2107090731931361281.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `JjkText`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewAny`
- `PreviewImage`
- `Qwen3VL_Chat`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
