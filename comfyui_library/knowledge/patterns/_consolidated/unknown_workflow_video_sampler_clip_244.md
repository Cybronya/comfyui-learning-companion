---
name: unknown_workflow_video_sampler_clip_244
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.931
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CM_IntToFloat, CheckpointLoaderSimple, DeepTranslatorTextNode, EmptyImage, Int, KSamplerSelect, LTXVConditioning, LTXVPreprocess, LTXVScheduler, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, RH_Captioner, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, Textbox, VAEDecodeTiled, VHS_VideoCombine, easy imageSize, easy mathFloat, easy textSwitch]
problems: []
missing: []
members: [视频生成/图生视频/1897935910422695937.json, 视频生成/图生视频/1897833408846843906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_244

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1897935910422695937.json、视频生成/图生视频/1897833408846843906.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CheckpointLoaderSimple`
- `DeepTranslatorTextNode`
- `EmptyImage`
- `Int`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVPreprocess`
- `LTXVScheduler`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `Textbox`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy imageSize`
- `easy mathFloat`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 1/2 个有
- `EmptyLTXVLatentVideo` —— 1/2 个有
- `LTXVAddGuide` —— 1/2 个有
- `LTXVCropGuides` —— 1/2 个有
- `LTXVImgToVideo` —— 1/2 个有
- `Text Find and Replace` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
