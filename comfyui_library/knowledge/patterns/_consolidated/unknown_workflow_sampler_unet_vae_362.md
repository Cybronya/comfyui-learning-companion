---
name: unknown_workflow_sampler_unet_vae_362
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4615
common_nodes: [CLIPLoader, CR Text, Get resolution [Crystools], GrowMaskWithBlur, Image Comparer (rgthree), ImagePadForOutpaint, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview+, PainterFluxImageEdit, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageDetailTransfer, easy imageRemBg, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品背景的更换 硕阳_2018245087959977985.json, 平台全量/超好用产品更换背景万物皆可-Flux2-Klein_2016033663376429057.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_362

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品背景的更换 硕阳_2018245087959977985.json、平台全量/超好用产品更换背景万物皆可-Flux2-Klein_2016033663376429057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `Get resolution [Crystools]`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview+`
- `PainterFluxImageEdit`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageDetailTransfer`
- `easy imageRemBg`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PadImageToCanvas` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `kkPadImageToCanvas` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
