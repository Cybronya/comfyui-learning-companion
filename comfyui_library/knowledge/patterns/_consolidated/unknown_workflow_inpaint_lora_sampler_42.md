---
name: unknown_workflow_inpaint_lora_sampler_42
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.949
common_nodes: [CLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json, 图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json, 图片生成/图生图/超强局部修复 哪里有问题点哪里_1956703472843198466.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json、图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json、图片生成/图生图/超强局部修复 哪里有问题点哪里_1956703472843198466.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

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
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerMask: MaskPreview` —— 2/3 个有
- `BboxDetectorCombined_v2` —— 1/3 个有
- `DownloadAndLoadFlorence2Model` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `UltralyticsDetectorProvider` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.25 | 0.05 - 0.3 | 3 | 46% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.25，观测区间 0.05 - 0.3，3 个样本，取值分散，一致性仅 46%
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
