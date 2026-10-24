---
name: image_to_image_video_lora_sampler_4
type: Image To Image
frequency: 6
level: strong
coverage: 0.930667
common_nodes: [Any To Any, CLIPLoader, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, Qwen3_VQA, RunningHub Deepcleaner, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAEEncode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy imageListToImageBatch, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen-Edit-2511_2065267923194830849.json, 图片生成/图生图/千问Qwen-Edit-2511【12个漫剧分镜生成工作流】_2064248572484345858.json, 图片生成/图生图/千问Qwen-Edit-2511【12个漫剧分镜生成工作流】_2066703299922972674.json, 图片生成/图生图/漫剧分镜生成（千问Edit2511场景角色一致性保持）_2013174580898172930.json, 图片生成/图生图/漫剧分镜生成（千问Edit2511场景角色一致性保持）_2016863442661019650.json, 图片生成/文生图/12个漫剧分镜生成工作流Qwen-Edit2511-nextscene_2021581375052193793.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/千问Qwen-Edit-2511_2065267923194830849.json、图片生成/图生图/千问Qwen-Edit-2511【12个漫剧分镜生成工作流】_2064248572484345858.json、图片生成/图生图/千问Qwen-Edit-2511【12个漫剧分镜生成工作流】_2066703299922972674.json、图片生成/图生图/漫剧分镜生成（千问Edit2511场景角色一致性保持）_2013174580898172930.json、图片生成/图生图/漫剧分镜生成（千问Edit2511场景角色一致性保持）_2016863442661019650.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `Any To Any`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `Qwen3_VQA`
- `RunningHub Deepcleaner`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `EnhancedLoadDiffusionModel` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
