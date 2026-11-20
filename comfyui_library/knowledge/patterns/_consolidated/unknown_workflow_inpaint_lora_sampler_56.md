---
name: unknown_workflow_inpaint_lora_sampler_56
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.799
common_nodes: [CLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json, 图片生成/图生图/Wan修手简单版-手动遮罩_1951207158161584130.json, 平台全量/009.修手_2004635945972494338.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json、图片生成/图生图/Wan修手简单版-手动遮罩_1951207158161584130.json、平台全量/009.修手_2004635945972494338.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `LayerMask: LoadSAM2Model` —— 1/3 个有
- `LayerMask: ObjectDetectorYOLO8` —— 1/3 个有
- `LayerMask: SAM2UltraV2` —— 1/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 35 | 3 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 0.3 | 0.15 - 0.3 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 35，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 0.3，观测区间 0.15 - 0.3，3 个样本
