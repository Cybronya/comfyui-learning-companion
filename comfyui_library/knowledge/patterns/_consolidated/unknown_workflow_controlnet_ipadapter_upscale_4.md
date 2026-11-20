---
name: unknown_workflow_controlnet_ipadapter_upscale_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.821
common_nodes: [Anything Everywhere3, ApplyInstantID, ApplyPulid, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConcatText_Zho, ControlNetLoader, Crop Face, DF_Image_scale_to_side, EmptyLatentImage, HighRes-Fix Script, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Crop Face, Image Paste Face, ImageScaleToTotalPixels, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler (Efficient), LatentUpscaleBy, Load RetinaFace, LoadImage, LoraLoader, PrepImageForClipVision, PreviewImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, RH_Captioner, SaveImage, ShowText|pysssss, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/PVC人物手办制作_1892113110004834306.json, 图片生成/图生图/真人转卡通手办_1912439003017113601.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/PVC人物手办制作_1892113110004834306.json、图片生成/图生图/真人转卡通手办_1912439003017113601.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyInstantID`
- `ApplyPulid`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConcatText_Zho`
- `ControlNetLoader`
- `Crop Face`
- `DF_Image_scale_to_side`
- `EmptyLatentImage`
- `HighRes-Fix Script`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Crop Face`
- `Image Paste Face`
- `ImageScaleToTotalPixels`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler (Efficient)`
- `LatentUpscaleBy`
- `Load RetinaFace`
- `LoadImage`
- `LoraLoader`
- `PrepImageForClipVision`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `RH_Captioner`
- `SaveImage`
- `ShowText|pysssss`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Compare` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: QWenImage2Prompt` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 100% |
| LoRA 模型强度 | -1.25 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 -1.25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
