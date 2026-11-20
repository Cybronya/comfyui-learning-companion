---
name: unknown_workflow_controlnet_ipadapter_upscale_2
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8985
common_nodes: [Anything Everywhere3, ApplyInstantID, ApplyPulid, CLIPSetLastLayer, CLIPTextEncode, CLIPVisionLoader, CR Apply LoRA Stack, Concat Text _O, ConditioningCombine, ConditioningSetAreaPercentage, ControlNetLoader, Crop Face, DF_Image_scale_to_side, EmptyLatentImage, IPAdapterAdvanced, IPAdapterModelLoader, Image Filter Adjustments, ImageUpscaleWithModel, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler (Efficient), LatentUpscaleBy, Load RetinaFace, LoadImage, PreviewImage, PulidEvaClipLoader, PulidModelLoader, SDXLPromptStyler, SaveImage, Text _O, UpscaleModelLoader, easy loraStack]
problems: []
missing: []
members: [图片生成/图生图/3D手办一键制作_1949638781774766082.json, 图片生成/图生图/人物转卡通自定义提示词3D手办高清一键制作_2067069311004532737.json, 平台全量/Cute You 2_1825798084449185794.json, 平台全量/Cute You 2_1826540905435197442.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/3D手办一键制作_1949638781774766082.json、图片生成/图生图/人物转卡通自定义提示词3D手办高清一键制作_2067069311004532737.json、平台全量/Cute You 2_1825798084449185794.json、平台全量/Cute You 2_1826540905435197442.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyInstantID`
- `ApplyPulid`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Apply LoRA Stack`
- `Concat Text _O`
- `ConditioningCombine`
- `ConditioningSetAreaPercentage`
- `ControlNetLoader`
- `Crop Face`
- `DF_Image_scale_to_side`
- `EmptyLatentImage`
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
- `Text _O`
- `UpscaleModelLoader`
- `easy loraStack`

**可变部分**（部分 workflow 才有）：
- `BRIA_RMBG_ModelLoader_Zho` —— 2/4 个有
- `BRIA_RMBG_Zho` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `CheckpointLoader|pysssss` —— 2/4 个有
- `GoogleTranslateTextNode` —— 2/4 个有
- `HfImageToRGB` —— 2/4 个有
- `HighRes-Fix Script` —— 2/4 个有
- `Image Overlay` —— 2/4 个有
- `ImageGenResolutionFromImage` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `ImpactFloat` —— 2/4 个有
- `ShowText` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `WD14Tagger|pysssss` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `CM_IntBinaryOperation` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 768 | 768 - 768 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）
