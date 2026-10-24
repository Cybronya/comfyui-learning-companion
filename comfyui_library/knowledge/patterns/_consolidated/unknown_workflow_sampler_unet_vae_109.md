---
name: unknown_workflow_sampler_unet_vae_109
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.777222
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize, ImageScaleToTotalPixels, ImageStitch, KSampler, LoadImage, PrimitiveInt, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit2511工作流_2003702124506693633.json, 图片生成/图生图/Qwen-Edit2511工作流_2027208837106765825.json, 图片生成/图生图/QwenImageEdit vs PLUS版对比工作流_1971777410565926913.json, 图片生成/图生图/eigen-全能图片V1图像编辑能力增强_1991503068768509954.json, 图片生成/图生图/一句话指令，精度图像编辑_1987338025019617282.json, 图片生成/图生图/图片编辑模型 FireRed-Image-Edit_2029846409733738497.json, 图片生成/文生图/QwenImageEdit 2509原版 VS R1增强_1983422173471776770.json, 图片生成/文生图/QwenImageEdit MeiTu VS 2509_1983355804264898562.json, 图片生成/文生图/QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_109

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit2511工作流_2003702124506693633.json、图片生成/图生图/Qwen-Edit2511工作流_2027208837106765825.json、图片生成/图生图/QwenImageEdit vs PLUS版对比工作流_1971777410565926913.json、图片生成/图生图/eigen-全能图片V1图像编辑能力增强_1991503068768509954.json、图片生成/图生图/一句话指令，精度图像编辑_1987338025019617282.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PrimitiveInt`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `easy joinImageBatch` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `Text Concatenate` —— 5/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `CustomAddLabel` —— 2/9 个有
- `easy loraNames` —— 2/9 个有
- `AILab_QwenVL` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `OpenposePreprocessor` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 9 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，9 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（15/9 个样本）：Steps较低可能导致细节不足
