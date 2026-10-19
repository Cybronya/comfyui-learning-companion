---
name: unknown_workflow_video_sampler_clip_101
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.581833
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2079816909545107457.json, 视频生成/图生视频/1983516962250760194.json, 视频生成/图生视频/2068956549908881410.json, 视频生成/图生视频/1984186286053474306.json, 视频生成/图生视频/2044709107302670338.json, 视频生成/图生视频/2010308124921569281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_101

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2079816909545107457.json、视频生成/图生视频/1983516962250760194.json、视频生成/图生视频/2068956549908881410.json、视频生成/图生视频/1984186286053474306.json、视频生成/图生视频/2044709107302670338.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `KSampler` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `QwenImageLatentAspectRatio` —— 1/6 个有
- `RHLLMChatNode` —— 1/6 个有
- `easy imageScaleDownToSize` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 6 | 83% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | normal | - | 6 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，6 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 normal，6 个样本，一致性 83%
