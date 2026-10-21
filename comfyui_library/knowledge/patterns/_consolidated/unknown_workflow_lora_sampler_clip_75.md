---
name: unknown_workflow_lora_sampler_clip_75
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7465
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, DF_Text_Box, Flux2Scheduler, GH_CropRestore, GH_MaskCropV2, GetImageSize+, GuHaiMaskDetect, KSamplerSelect, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, Mask Invert, RandomNoise, ReferenceLatent, SAM3Segment, SamplerCustomAdvanced, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海注释, 孤海遮罩分析, 布尔孤海, 数学运算_孤海]
problems: []
missing: [CR Text, CR Text Concatenate, Mask Fill Holes, Mask Invert, SimpleMath+, 图像缩放V2_孤海, 孤海-遮罩混合运算, 孤海遮罩分析, 布尔孤海, 数学运算_孤海, GetImageSize+]
members: [图片生成/图生图/2074386683885346818.json, 图片生成/文生图/换发型_2088083592109977601.json, 图片生成/文生图/换发型_2088155136811163649.json, 数字人/数字人/Klein-换发型V2-优化版_2094598027389530113.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2074386683885346818.json、图片生成/文生图/换发型_2088083592109977601.json、图片生成/文生图/换发型_2088155136811163649.json、数字人/数字人/Klein-换发型V2-优化版_2094598027389530113.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewImage` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、Mask Fill Holes、Mask Invert、SimpleMath+
