---
name: unknown_workflow_controlnet_ipadapter_upscale_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9365
common_nodes: [Anything Everywhere3, ApplyInstantID, ApplyPulid, CLIPSetLastLayer, CLIPTextEncode, CLIPVisionLoader, CR Apply LoRA Stack, CheckpointLoader|pysssss, Concat Text _O, ConditioningCombine, ConditioningSetAreaPercentage, ControlNetLoader, Crop Face, DF_Image_scale_to_side, EmptyLatentImage, GoogleTranslateTextNode, IPAdapterAdvanced, IPAdapterModelLoader, Image Filter Adjustments, ImageUpscaleWithModel, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler (Efficient), LatentUpscaleBy, Load RetinaFace, LoadImage, PreviewImage, PulidEvaClipLoader, PulidModelLoader, SDXLPromptStyler, SaveImage, ShowText, Text _O, UpscaleModelLoader, easy loraStack]
problems: []
missing: []
members: [图片生成/图生图/3D手办一键制作_1949638781774766082.json, 图片生成/图生图/人物转卡通自定义提示词3D手办高清一键制作_2067069311004532737.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/3D手办一键制作_1949638781774766082.json、图片生成/图生图/人物转卡通自定义提示词3D手办高清一键制作_2067069311004532737.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyInstantID`
- `ApplyPulid`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Apply LoRA Stack`
- `CheckpointLoader|pysssss`
- `Concat Text _O`
- `ConditioningCombine`
- `ConditioningSetAreaPercentage`
- `ControlNetLoader`
- `Crop Face`
- `DF_Image_scale_to_side`
- `EmptyLatentImage`
- `GoogleTranslateTextNode`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `Image Filter Adjustments`
- `ImageUpscaleWithModel`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler (Efficient)`
- `LatentUpscaleBy`
- `Load RetinaFace`
- `LoadImage`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidModelLoader`
- `SDXLPromptStyler`
- `SaveImage`
- `ShowText`
- `Text _O`
- `UpscaleModelLoader`
- `easy loraStack`

**可变部分**（部分 workflow 才有）：
- `TT_img_enc` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
