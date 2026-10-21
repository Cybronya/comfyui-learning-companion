---
name: unknown_workflow_video_lora_sampler_282
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.99275
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, INTConstant, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, Text Concatenate, UNETLoader, VAELoader, VHS_VideoCombine, Wan22PromptSelector, WanImageToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2076940992846065665.json, 视频生成/图生视频/2080827285132898306.json, 视频生成/图生视频/2079587652592037890.json, 视频生成/图生视频/最强 Wan2.2 Remix V3 图生视频｜丝滑流畅升级版_2087862856862748674.json, 视频生成/图生视频/2064528658047520769.json, 视频生成/图生视频/2072282561220530178.json, 视频生成/文生视频/定制风景文生视频风景视频快速生成_2077718229480468482.json, 视频生成/文生视频/定制风景文生视频风景视频快速生成_2077733281923162113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_282

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2076940992846065665.json、视频生成/图生视频/2080827285132898306.json、视频生成/图生视频/2079587652592037890.json、视频生成/图生视频/最强 Wan2.2 Remix V3 图生视频｜丝滑流畅升级版_2087862856862748674.json、视频生成/图生视频/2064528658047520769.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `INTConstant`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `Text Concatenate`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanImageToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 7/8 个有
- `RIFE VFI` —— 7/8 个有
- `VAEDecode` —— 7/8 个有
- `LoadImage` —— 5/8 个有
- `ConditioningKrea2Rebalance` —— 3/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `EmptyLatentImage` —— 3/8 个有
- `Int` —— 3/8 个有
- `TTResolutionSelector` —— 3/8 个有
- `easy promptLine` —— 3/8 个有
- `JjkText` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
