---
name: unknown_workflow_inpaint_sampler_clip_118
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.687
common_nodes: [CLIPTextEncode, DualCLIPLoader, Fast Groups Bypasser (rgthree), FeatherMask, FluxGuidance, GetNode, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LoadImage, MaskPreview+, Note Plus (mtb), PreviewImage, RepeatLatentBatch, SaveImage, SetNode, ToBoolNode, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy ifElse]
problems: []
missing: []
members: [平台全量/Flux 局部擦除_1921465506887565313.json, 平台全量/手部修复_1900844995425746946.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Flux 局部擦除_1921465506887565313.json、平台全量/手部修复_1900844995425746946.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FeatherMask`
- `FluxGuidance`
- `GetNode`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskPreview+`
- `Note Plus (mtb)`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `SetNode`
- `ToBoolNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `LayerStyle: ColorOverlay V2` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `MaskFromColor+` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `easy imageBatchToImageList` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
