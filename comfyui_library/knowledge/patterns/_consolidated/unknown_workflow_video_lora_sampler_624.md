---
name: unknown_workflow_video_lora_sampler_624
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.643
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, GetImageRangeFromBatch, INTConstant, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Chromoed_comfyUI_native 英伟达图像编辑_1987385808426569730.json, 图片生成/图生图/Chromoed_comfyUI_native_1985980590061170689.json, 图片生成/图生图/生图-单图编辑-Chrono Edit-官方_1987134248253632514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_624

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Chromoed_comfyUI_native 英伟达图像编辑_1987385808426569730.json、图片生成/图生图/Chromoed_comfyUI_native_1985980590061170689.json、图片生成/图生图/生图-单图编辑-Chrono Edit-官方_1987134248253632514.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `GetImageRangeFromBatch`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy positive` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
