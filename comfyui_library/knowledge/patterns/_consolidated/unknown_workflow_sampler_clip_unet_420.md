---
name: unknown_workflow_sampler_clip_unet_420
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.816
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, JjkText, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_Captioner_Pro, RH_Nano_Banana2_Gemini31Flash, RH_RhartImageG2ImageToImage, RH_Translator, RandomNoise, ReferenceLatent, Repeater|pysssss, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/⭐️ 线稿转绘 _ 全能图片G2 丨Kelin丨2_2082268482082787329.json, 图片生成/图生图/线稿转绘 _ 2 全能图片G2 kelin_2082032894230491138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_420

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/⭐️ 线稿转绘 _ 全能图片G2 丨Kelin丨2_2082268482082787329.json、图片生成/图生图/线稿转绘 _ 2 全能图片G2 kelin_2082032894230491138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `JjkText`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_Captioner_Pro`
- `RH_Nano_Banana2_Gemini31Flash`
- `RH_RhartImageG2ImageToImage`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `Repeater|pysssss`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Image Input Switch` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageSwitch` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有
- `忽略多组孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
