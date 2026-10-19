---
name: unknown_workflow_video_lora_sampler_566
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.786667
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, ImageFromBatch, Int, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, Text Load Line From File, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: [CR Model Input Switch, CR Text, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, Text Load Line From File, Text Multiline, easy batchAnything, easy cleanGpuUsed, easy convertAnything, easy forLoopEnd, easy forLoopStart]
members: [图片生成/文生图/1953042137630896130.json, 视频生成/图生视频/1950632434528374786.json, 视频生成/图生视频/1989316745833967618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_566

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1953042137630896130.json、视频生成/图生视频/1950632434528374786.json、视频生成/图生视频/1989316745833967618.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Text Load Line From File`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageSmartSharpen+` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CR Model Input Switch` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `ConditionalTextOutput` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Qwen3_VQA_Plus` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy convertAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 2.5 | 3 | 53% |
| 调度器 | lcm | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 2.5，3 个样本
- 调度器 最常用 lcm，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Model Input Switch、CR Text、LayerUtility: PurgeVRAM V2、MathExpression|pysssss、Text Load Line From File
