---
name: unknown_workflow_inpaint_lora_sampler_55
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8585
common_nodes: [CLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json, 图片生成/图生图/Wan修手简单版-手动遮罩_1951207158161584130.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json、图片生成/图生图/Wan修手简单版-手动遮罩_1951207158161584130.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `ShowText` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
