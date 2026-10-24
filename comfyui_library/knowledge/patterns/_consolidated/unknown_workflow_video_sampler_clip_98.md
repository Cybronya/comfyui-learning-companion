---
name: unknown_workflow_video_sampler_clip_98
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.581
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, Fast Groups Bypasser (rgthree), ImageLoader, Int, JWStringConcat, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Work-Fisher-全自动Qwen3VL+文生图+图生视频_1983065711180427265.json, 视频生成/图生视频/Work-Fisher-全自动Qwen3VL+文生图+图生视频+_2006367145126531073.json, 视频生成/图生视频/Work-Fisher-全自动Qwen3VL+文生图+图生视频_2056017029798350850.json, 视频生成/图生视频/gen全能视频Si-全自动qwen3-vl图片反推提示词 【图生视频】_1983541525290360833.json, 视频生成/图生视频/全自动Qwen3VL参考图反推+文生图+图生视频三合一工作流_2033860844664131586.json, 视频生成/图生视频/全自动Qwen3VL参考图反推提示词+文生图+图生视频_2002649806117978113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Work-Fisher-全自动Qwen3VL+文生图+图生视频_1983065711180427265.json、视频生成/图生视频/Work-Fisher-全自动Qwen3VL+文生图+图生视频+_2006367145126531073.json、视频生成/图生视频/Work-Fisher-全自动Qwen3VL+文生图+图生视频_2056017029798350850.json、视频生成/图生视频/gen全能视频Si-全自动qwen3-vl图片反推提示词 【图生视频】_1983541525290360833.json、视频生成/图生视频/全自动Qwen3VL参考图反推+文生图+图生视频三合一工作流_2033860844664131586.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Any To Any` —— 5/6 个有
- `EmptySD3LatentImage` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `KSampler` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MultiplePathsInput` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `VHS_SelectFilename` —— 5/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | 1 | 1 - 1 | 6 | 100% |
| 重绘幅度 | euler_ancestral | - | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，6 个样本，一致性 100%
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
