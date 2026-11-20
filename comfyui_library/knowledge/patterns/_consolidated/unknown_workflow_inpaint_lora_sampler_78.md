---
name: unknown_workflow_inpaint_lora_sampler_78
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8925
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyImage, FluxGuidance, ImageAndMaskPreview, ImageConcanate, ImageCrop, ImageResize+, ImageToMask, ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LoadImage, MaskToImage, Power Lora Loader (rgthree), PreviewImage, ResizeMask, SaveImage, TeaCache, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Ace++FaceSwap完美换脸_1927354917009121282.json, 平台全量/换脸ACE_1891473637336293378.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Ace++FaceSwap完美换脸_1927354917009121282.json、平台全量/换脸ACE_1891473637336293378.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageCrop`
- `ImageResize+`
- `ImageToMask`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `ResizeMask`
- `SaveImage`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 1/2 个有
- `InpaintCrop` —— 1/2 个有
- `InpaintStitch` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18.5 | - | 2 | 65% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | heun | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 18.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
