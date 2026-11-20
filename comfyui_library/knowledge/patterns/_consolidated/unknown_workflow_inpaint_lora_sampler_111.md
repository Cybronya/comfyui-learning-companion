---
name: unknown_workflow_inpaint_lora_sampler_111
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.811
common_nodes: [AddMaskForICLora, CLIPTextEncode, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Catvton虚拟试衣-手工涂抹LoRA_1964917326493663233.json, 平台全量/catvton换装_1893948039902703618.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_111

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Catvton虚拟试衣-手工涂抹LoRA_1964917326493663233.json、平台全量/catvton换装_1893948039902703618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMaskForICLora`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `Image Blank` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `ImageCrop+` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/2 个有
- `easy mathInt` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
