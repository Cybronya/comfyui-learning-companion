---
name: unknown_workflow_inpaint_lora_sampler_48
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.87075
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/qwen2509-P图改字局部重绘万能改图改字-无痕迹，美工的万能助手_1997085821570322433.json, 平台全量/【Qwen2511】p图改字无痕迹_2000768295085240322.json, 平台全量/局部改图改字 -无痕迹_2005084296908075010.json, 数字人/数字人/【Qwen2511】p图改字无痕迹_2108230336445509634.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/qwen2509-P图改字局部重绘万能改图改字-无痕迹，美工的万能助手_1997085821570322433.json、平台全量/【Qwen2511】p图改字无痕迹_2000768295085240322.json、平台全量/局部改图改字 -无痕迹_2005084296908075010.json、数字人/数字人/【Qwen2511】p图改字无痕迹_2108230336445509634.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `InpaintCrop` —— 2/4 个有
- `InpaintCropImproved` —— 2/4 个有
- `InpaintStitch` —— 2/4 个有
- `InpaintStitchImproved` —— 2/4 个有
- `MaskBlur+` —— 2/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 3 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
