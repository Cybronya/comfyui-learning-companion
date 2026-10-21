---
name: unknown_workflow_video_lora_sampler_854
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.596
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAny, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy forLoopEnd, easy forLoopStart, easy promptLine]
problems: []
missing: []
members: [视频生成/图生视频/2007324073478594561.json, 视频生成/图生视频/2006663467071180801.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_854

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2007324073478594561.json、视频生成/图生视频/2006663467071180801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWStringMultiline` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `WanVideoNAG` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy indexAnything` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy lengthAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 86% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
