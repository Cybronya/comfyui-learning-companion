---
name: unknown_workflow_video_lora_sampler_980
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6655
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, GetNode, ImageBatchExtendWithOverlap, ImageResizeKJv2, Int, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ProcessString, SetNode, SimpleMath+, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy forLoopEnd, easy forLoopStart, easy int, easy promptLine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/无限循环长视频-SVI 2 Pro_2005513754672594946.json, 视频生成/图生视频/无限长视频-SVI 2 Pro（qwen3自动提示词）_2005845376299139073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_980

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/无限循环长视频-SVI 2 Pro_2005513754672594946.json、视频生成/图生视频/无限长视频-SVI 2 Pro（qwen3自动提示词）_2005845376299139073.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SetNode`
- `SimpleMath+`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `SomethingToString` —— 1/2 个有
- `TextToNumber` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
