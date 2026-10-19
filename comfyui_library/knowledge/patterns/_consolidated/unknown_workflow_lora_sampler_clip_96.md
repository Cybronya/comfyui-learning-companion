---
name: unknown_workflow_lora_sampler_clip_96
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.65
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, DF_Text_Box, Flux2Scheduler, GH_CropRestore, GH_MaskCropV2, GetImageSize+, GuHaiMaskDetect, KSamplerSelect, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, Mask Invert, RandomNoise, ReferenceLatent, SAM3Segment, SamplerCustomAdvanced, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海注释, 孤海遮罩分析, 布尔孤海, 数学运算_孤海]
problems: []
missing: [CR Text, CR Text Concatenate, Mask Fill Holes, Mask Invert, SimpleMath+, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海遮罩分析, 布尔孤海, 数学运算_孤海, GetImageSize+]
members: [图片生成/图生图/2074386683885346818.json, 数字人/数字人/Klein-换发型V2-优化版_2094598027389530113.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_96

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2074386683885346818.json、数字人/数字人/Klein-换发型V2-优化版_2094598027389530113.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DF_Text_Box`
- `Flux2Scheduler`
- `GH_CropRestore`
- `GH_MaskCropV2`
- `GetImageSize+`
- `GuHaiMaskDetect`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `Mask Invert`
- `RandomNoise`
- `ReferenceLatent`
- `SAM3Segment`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `图像缩放V2_孤海`
- `孤海-遮罩混合运算`
- `孤海注释`
- `孤海遮罩分析`
- `布尔孤海`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、Mask Fill Holes、Mask Invert、SimpleMath+
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
