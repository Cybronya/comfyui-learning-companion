---
name: unknown_workflow_video_sampler_clip_75
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.56
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, Fast Groups Bypasser (rgthree), ImageLoader, Int, JWStringConcat, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: [Any To Any, LayerUtility: ImageScaleByAspectRatio V2, RIFE VFI, easy cleanGpuUsed, CR Prompt Text]
members: [图片生成/文生图/1983065711180427265.json, 视频生成/图生视频/1983065711180427265.json, 视频生成/图生视频/2006367145126531073.json, 视频生成/图生视频/2056017029798350850.json, 视频生成/图生视频/1983541525290360833.json, 视频生成/图生视频/2033860844664131586.json, 视频生成/图生视频/2002649806117978113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1983065711180427265.json、视频生成/图生视频/1983065711180427265.json、视频生成/图生视频/2006367145126531073.json、视频生成/图生视频/2056017029798350850.json、视频生成/图生视频/1983541525290360833.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `ImageLoader`
- `Int`
- `JWStringConcat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Any To Any` —— 6/7 个有
- `EmptySD3LatentImage` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `KSampler` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `MultiplePathsInput` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `VHS_SelectFilename` —— 6/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | 1 | 1 - 1 | 7 | 100% |
| 重绘幅度 | euler_ancestral | - | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，7 个样本，一致性 100%
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Any To Any、LayerUtility: ImageScaleByAspectRatio V2、RIFE VFI、easy cleanGpuUsed、CR Prompt Text
