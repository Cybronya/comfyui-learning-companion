---
name: unknown_workflow_inpaint_upscale_lora_8
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9195
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, Evaluate Strings, FluxGuidance, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, Seed Everywhere, Text Multiline, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy imageInsetCrop, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json, 平台全量/ICEdit图像编辑 输入指令一句话改图_1931142153484087298.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json、平台全量/ICEdit图像编辑 输入指令一句话改图_1931142153484087298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `Evaluate Strings`
- `FluxGuidance`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `Seed Everywhere`
- `Text Multiline`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 1/2 个有
- `BaiduTranslateNode` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `FaceAnalysisModels` —— 1/2 个有
- `FaceBoundingBox` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
