---
name: unknown_workflow_ipadapter_inpaint_sampler
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7505
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ClipInterrogator, Fast Groups Bypasser (rgthree), INPAINT_InpaintWithModel, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, Image Blend by Mask, Image Comparer (rgthree), Image Power Noise, ImageCompositeMasked, ImagePadForOutpaint, InvertMask, JWImageResizeByLongerSide, KSampler, LayerMask: MaskGrow, LoadImage, MaskPreview+, MaskToImage, PreviewImage, RepeatLatentBatch, SaveImage, ShowText|pysssss, VAEDecode, easy imageSize, preview_mask]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/简易扩图工作流_V1【PD】_1910584503918653441.json, 图片生成/图生图/简易扩图工作流_V1【PD】_2114315862000881665.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_inpaint_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/简易扩图工作流_V1【PD】_1910584503918653441.json、图片生成/图生图/简易扩图工作流_V1【PD】_2114315862000881665.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ClipInterrogator`
- `Fast Groups Bypasser (rgthree)`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `Image Blend by Mask`
- `Image Comparer (rgthree)`
- `Image Power Noise`
- `ImageCompositeMasked`
- `ImagePadForOutpaint`
- `InvertMask`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `easy imageSize`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
