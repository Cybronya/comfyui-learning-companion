---
name: unknown_workflow_controlnet_lora_sampler_18
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.922
common_nodes: [BasicScheduler, CLIPTextEncode, CLIPVisionLoader, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingV2Preprocessor, FluxGuidance, ImageConcanate, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoraLoaderModelOnly, RH_Captioner, ReduxAdvanced, SamplerCustom, SaveImage, String Literal, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/For循环批量处理图像_1953363369694777345.json, 图片生成/图生图/图像风格转绘_1953286478332948482.json, 图片生成/图生图/美漫_漫画风格转绘_1926326791407910913.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/For循环批量处理图像_1953363369694777345.json、图片生成/图生图/图像风格转绘_1953286478332948482.json、图片生成/图生图/美漫_漫画风格转绘_1926326791407910913.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `FluxGuidance`
- `ImageConcanate`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoraLoaderModelOnly`
- `RH_Captioner`
- `ReduxAdvanced`
- `SamplerCustom`
- `SaveImage`
- `String Literal`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Display Any (rgthree)` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `Image Compare (mtb)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `NunchakuTextEncoderLoader` —— 1/3 个有
- `RHBatchImages:` —— 1/3 个有
- `RHExtractImage` —— 1/3 个有
- `RHUploadZip` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy imageCount` —— 1/3 个有
- `easy joinImageBatch` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.3 - 0.45 | 3 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.3 - 0.45，3 个样本，取值集中（一致性 82%）
