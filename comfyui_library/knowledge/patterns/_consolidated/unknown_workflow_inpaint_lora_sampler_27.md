---
name: unknown_workflow_inpaint_lora_sampler_27
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.91175
common_nodes: [CLIPLoader, CLIPTextEncode, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json, 图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json, 图片生成/图生图/手脚修复_2017856742083792897.json, 图片生成/图生图/超强局部修复 哪里有问题点哪里_1956703472843198466.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【🛫书墨】手部快速修复流——官方wan2.1_1944824629200343041.json、图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json、图片生成/图生图/手脚修复_2017856742083792897.json、图片生成/图生图/超强局部修复 哪里有问题点哪里_1956703472843198466.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `LayerMask: MaskPreview` —— 3/4 个有
- `ModelSamplingSD3` —— 3/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `BboxDetectorCombined_v2` —— 1/4 个有
- `DownloadAndLoadFlorence2Model` —— 1/4 个有
- `Florence2Run` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `InpaintCrop` —— 1/4 个有
- `InpaintStitch` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `UltralyticsDetectorProvider` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | uni_pc | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.215 | 0.05 - 0.3 | 4 | 52% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 uni_pc，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.215，观测区间 0.05 - 0.3，4 个样本
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
