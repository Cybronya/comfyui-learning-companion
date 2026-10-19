---
name: unknown_workflow_video_lora_sampler_481
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9635
common_nodes: [Any To Any, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CR Prompt Text, CreateVideo, GetVideoComponents, HunyuanVideoFoley, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, Qwen3_VQA, RHLLMChatNode, SaveVideo, StringReplace, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2065331654767505409.json, 视频生成/图生视频/2065702680814776322.json, 视频生成/图生视频/2073465859552669698.json, 视频生成/文生视频/（4步加速版）Bernini文生视频+音效v3_2073465929488490497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_481

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2065331654767505409.json、视频生成/图生视频/2065702680814776322.json、视频生成/图生视频/2073465859552669698.json、视频生成/文生视频/（4步加速版）Bernini文生视频+音效v3_2073465929488490497.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `Any To Any`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CreateVideo`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `RHLLMChatNode`
- `SaveVideo`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `easy batchAnything` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `easy imagesSplitImage` —— 3/4 个有
- `easy mergeVideosFromPaths` —— 3/4 个有
- `easy timelineEditor` —— 3/4 个有
- `easy timelineInfoOutput` —— 3/4 个有
- `easy timelineSegmentCount` —— 3/4 个有
- `easy timelineSegmentOutput` —— 3/4 个有
- `PrimitiveInt` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 4 - 10 | 4 | 57% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 10，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
