---
name: unknown_workflow_lora_sampler_unet_232
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.922
common_nodes: [Bjornulf_ShowInt, CLIPLoader, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler (Efficient), LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEEncode, VAELoader, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageCount, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图片压缩包大批量去水印_2049459057039249410.json, 图片生成/图生图/批量去水印【qwen】_1971962512713379841.json, 图片生成/图生图/批量去水印【好用】_1984252237239173122.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_232

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片压缩包大批量去水印_2049459057039249410.json、图片生成/图生图/批量去水印【qwen】_1971962512713379841.json、图片生成/图生图/批量去水印【好用】_1984252237239173122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler (Efficient)`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LoadImage` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
