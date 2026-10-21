---
name: unknown_workflow_upscale_lora_sampler_5
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.799727
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PathchSageAttentionKJ, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Load Line From File, Text Multiline, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader, easy anythingIndexSwitch, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: [MathExpression|pysssss, Text Load Line From File, Text Multiline, easy anythingIndexSwitch, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageBatchToImageList, easy imageListToImageBatch]
members: [图片生成/图生图/2102071673460711426.json, 图片生成/图生图/2102078912699392002.json, 图片生成/图生图/2102080371482513410.json, 图片生成/图生图/2102100907671511041.json, 图片生成/图生图/2102247918542614530.json, 图片生成/图生图/2102286556152295426.json, 图片生成/图生图/2102438785630953473.json, 图片生成/图生图/2102442855301214209.json, 图片生成/图生图/三视图_多视图_角色三视图_角色多视角_Qwen_2107026065003728897.json, 图片生成/文生图/三视图_多视图_角色三视图_角色多视角_Qwen_2086649054892744706.json, 视频生成/文生视频/三视图_多视图_角色三视图_角色多视角_Qwen_2045155129598418945.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/2102071673460711426.json、图片生成/图生图/2102078912699392002.json、图片生成/图生图/2102080371482513410.json、图片生成/图生图/2102100907671511041.json、图片生成/图生图/2102247918542614530.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Load Line From File`
- `Text Multiline`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Fast Bypasser (rgthree)` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 720 | 11 | 100% |
| 高度 | 1440 | 1440 - 1440 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 720，11 个样本，取值集中（一致性 100%）
- 高度 中位数 1440，观测区间 1440 - 1440，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、Text Load Line From File、Text Multiline、easy anythingIndexSwitch、easy batchAnything
