---
name: unknown_workflow_upscale_vae_40
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6334
common_nodes: [GH_CropRestore, GH_MaskCropV2, Image Comparer (rgthree), ImageToMask, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LoadImage, MaskPreview, MaskPreview+, MuyeTextEditOutput, PreviewImage, RH_Nano_Banana2_Gemini31Flash, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy float, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/真实换脸 Real Face Swap_2095326961064304641.json, 平台全量/修手 人手修复 手部局部重绘 精修_2078757593299898369.json, 平台全量/修手_1890093910163857409.json, 平台全量/换脸 99.9%相似_2073750101985677313.json, 平台全量/超强自动换头换脸 全自动写实换脸换装 指定换脸真实自然 换脸+99.9%相似_2073928263692546050.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_40

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/真实换脸 Real Face Swap_2095326961064304641.json、平台全量/修手 人手修复 手部局部重绘 精修_2078757593299898369.json、平台全量/修手_1890093910163857409.json、平台全量/换脸 99.9%相似_2073750101985677313.json、平台全量/超强自动换头换脸 全自动写实换脸换装 指定换脸真实自然 换脸+99.9%相似_2073928263692546050.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 5 个 workflow 都包含：
- `GH_CropRestore`
- `GH_MaskCropV2`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `MaskPreview`
- `MaskPreview+`
- `MuyeTextEditOutput`
- `PreviewImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy float`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `FaceAlign` —— 3/5 个有
- `FaceAnalysisModels` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 3/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/5 个有
- `Masks Add` —— 3/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/5 个有
- `RH_RhartImageG2ImageToImage` —— 3/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
