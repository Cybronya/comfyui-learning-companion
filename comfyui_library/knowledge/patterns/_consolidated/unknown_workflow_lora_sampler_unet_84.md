---
name: unknown_workflow_lora_sampler_unet_84
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.803875
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, ImageBatch, ImageScaleToTotalPixels, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveInt, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy joinImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/next scene V2自动分镜生成_1980154422523236353.json, 图片生成/图生图/Qwen-Edit2511工作流_2003702124506693633.json, 图片生成/图生图/Qwen-Edit2511工作流_2027208837106765825.json, 图片生成/图生图/QwenImageEdit vs PLUS版对比工作流_1971777410565926913.json, 图片生成/图生图/eigen-全能图片V1图像编辑能力增强_1991503068768509954.json, 图片生成/图生图/一句话指令，精度图像编辑_1987338025019617282.json, 图片生成/文生图/QwenImageEdit 2509原版 VS R1增强_1983422173471776770.json, 图片生成/文生图/QwenImageEdit MeiTu VS 2509_1983355804264898562.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/next scene V2自动分镜生成_1980154422523236353.json、图片生成/图生图/Qwen-Edit2511工作流_2003702124506693633.json、图片生成/图生图/Qwen-Edit2511工作流_2027208837106765825.json、图片生成/图生图/QwenImageEdit vs PLUS版对比工作流_1971777410565926913.json、图片生成/图生图/eigen-全能图片V1图像编辑能力增强_1991503068768509954.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `ImageBatch`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy joinImageBatch`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `ShowText|pysssss` —— 7/8 个有
- `Text Concatenate` —— 6/8 个有
- `CustomAddLabel` —— 2/8 个有
- `GetNode` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `easy loraNames` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `OpenposePreprocessor` —— 1/8 个有
- `ProcessString` —— 1/8 个有
- `Qwen2.5VL` —— 1/8 个有
- `easy promptLine` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 8 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，8 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（14/8 个样本）：Steps较低可能导致细节不足
