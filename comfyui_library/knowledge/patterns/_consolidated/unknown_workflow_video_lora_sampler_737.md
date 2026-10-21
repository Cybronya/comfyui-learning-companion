---
name: unknown_workflow_video_lora_sampler_737
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5375
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetNode, KSampler, LoadImage, Power Lora Loader (rgthree), PreviewImage, ProcessString, SetNode, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy promptLine, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1985971814922891266.json, 视频生成/图生视频/1988448828670001154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_737

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1985971814922891266.json、视频生成/图生视频/1988448828670001154.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSampler`
- `LoadImage`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `ProcessString`
- `SetNode`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy promptLine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `QZ_ResolutionPreset` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | 1 | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
