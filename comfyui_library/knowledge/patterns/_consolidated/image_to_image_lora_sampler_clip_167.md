---
name: image_to_image_lora_sampler_clip_167
type: Image To Image
frequency: 2
level: weak
coverage: 0.9045
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GoogleTranslateTextNode, ImageConcanate, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, PDIMAGE_LongerSize, PreviewImage, RMBG, ReferenceLatent, SaveImage, TTP_Expand_And_Mask, TeaCache, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/最强换头！Flux Kontext Put it here进阶工作流V1_1946789124498944002.json, 图片生成/图生图/自动换脸（put it here）_1952723944556138498.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_167

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/最强换头！Flux Kontext Put it here进阶工作流V1_1946789124498944002.json、图片生成/图生图/自动换脸（put it here）_1952723944556138498.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GoogleTranslateTextNode`
- `ImageConcanate`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PDIMAGE_LongerSize`
- `PreviewImage`
- `RMBG`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Expand_And_Mask`
- `TeaCache`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 1/2 个有
- `Bool` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `ImageCropper` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoadImageOutput` —— 1/2 个有
- `PMRF` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
