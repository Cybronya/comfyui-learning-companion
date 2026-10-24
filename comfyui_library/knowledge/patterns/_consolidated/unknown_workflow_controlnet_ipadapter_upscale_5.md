---
name: unknown_workflow_controlnet_ipadapter_upscale_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.643
common_nodes: [Any Switch (rgthree), Anything Everywhere, Anything Everywhere3, BNK_CLIPTextEncodeAdvanced, BrushNet, BrushNetLoader, ConditioningCombine, ConstrainImage|pysssss, ControlNetApplyAdvanced, ControlNetLoader, DetailerForEach, GetImageSize+, GetNode, GrowMask, GrowMaskWithBlur, ICLightConditioning, IPAdapter, IPAdapterUnifiedLoader, Image Overlay, ImagePass, ImageScale, InspyrenetRembg, InvertMask, InvertMask (segment anything), LoadAndApplyICLightUnet, LoadImage, MaskToSEGS, SaveImage, SetNode, SubtractMask, UltimateSDUpscale, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/一键换背景丨重新打光丨保留文字细节_1905841921451806722.json, 图片生成/图生图/图生图+换背景+打光_1901189314448105473.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键换背景丨重新打光丨保留文字细节_1905841921451806722.json、图片生成/图生图/图生图+换背景+打光_1901189314448105473.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `Anything Everywhere3`
- `BNK_CLIPTextEncodeAdvanced`
- `BrushNet`
- `BrushNetLoader`
- `ConditioningCombine`
- `ConstrainImage|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailerForEach`
- `GetImageSize+`
- `GetNode`
- `GrowMask`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `Image Overlay`
- `ImagePass`
- `ImageScale`
- `InspyrenetRembg`
- `InvertMask`
- `InvertMask (segment anything)`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToSEGS`
- `SaveImage`
- `SetNode`
- `SubtractMask`
- `UltimateSDUpscale`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `workflow/CLIP文本编码器` —— 1/2 个有
- `workflow/k` —— 1/2 个有
- `workflow/k采样器` —— 1/2 个有
- `workflow/模型加载器` —— 1/2 个有
- `workflow>CLIP文本编码器` —— 1/2 个有
- `workflow>k` —— 1/2 个有
- `workflow>k采样器` —— 1/2 个有
- `workflow>模型加载器` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
