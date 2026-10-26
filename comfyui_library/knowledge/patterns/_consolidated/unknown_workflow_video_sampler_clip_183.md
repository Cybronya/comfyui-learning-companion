---
name: unknown_workflow_video_sampler_clip_183
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.838667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, INTConstant, ImageResizeKJv2, ImpactSwitch, Int, LayerUtility: BooleanOperatorV2, LayerUtility: If , LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAny, PrimitiveStringMultiline, RH_LLMAPI_NODE, SimpleMath+, String, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy cleanGpuUsed, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AIGC 工作流（课程）_1994360309320126465.json, 视频生成/图生视频/SmoothMixWWan 2.2 图生视频自动手动双模式_1995469432359202817.json, 视频生成/图生视频/SmoothMixWan2.2首尾帧视频_1995490071992262658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/AIGC 工作流（课程）_1994360309320126465.json、视频生成/图生视频/SmoothMixWWan 2.2 图生视频自动手动双模式_1995469432359202817.json、视频生成/图生视频/SmoothMixWan2.2首尾帧视频_1995490071992262658.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `INTConstant`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `Int`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `SimpleMath+`
- `String`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch (4 way)` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `ChinesePrompt_Mix` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Wan22PromptSelector` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 3 | 33% |
| Prompt 约束强度(CFG) | 6 | 1 - 8 | 3 | 41% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler_ancestral | - | 3 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 9，3 个样本，一致性 33%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 8，3 个样本，取值分散，一致性仅 41%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，3 个样本，一致性 67%
