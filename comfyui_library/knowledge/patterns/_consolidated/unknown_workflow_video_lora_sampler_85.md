---
name: unknown_workflow_video_lora_sampler_85
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.767062
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, DF_Integer, Fast Groups Bypasser (rgthree), INTConstant, ImageResizeKJv2, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, RIFE VFI, SaveImage, SimpleMath+, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, easy promptLine, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, RIFE VFI, SimpleMath+, Text Multiline, easy cleanGpuUsed, easy clearCacheAll, CR Prompt Text, easy promptLine]
members: [图片生成/图生图/2074200565537656834.json, 图片生成/文生图/1985901390851710978.json, 视频生成/图生视频/1978956982134673409.json, 视频生成/图生视频/1979224907714301953.json, 视频生成/图生视频/1979025771903750146.json, 视频生成/图生视频/2009447313822982146.json, 视频生成/图生视频/2049416361801158657.json, 视频生成/图生视频/2009894943287939073.json, 视频生成/图生视频/2064716899979718657.json, 视频生成/图生视频/1978804615628099585.json, 视频生成/图生视频/2009509747891904514.json, 视频生成/图生视频/图生图（自动分镜）电影级+视频生成_2074200565537656834.json, 视频生成/图生视频/2062483360198516737.json, 视频生成/图生视频/2056237842430480386.json, 视频生成/文生视频/1978956982134673409.json, 视频生成/文生视频/1979224907714301953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/2074200565537656834.json、图片生成/文生图/1985901390851710978.json、视频生成/图生视频/1978956982134673409.json、视频生成/图生视频/1979224907714301953.json、视频生成/图生视频/1979025771903750146.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DF_Integer`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SaveImage`
- `SimpleMath+`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `easy promptLine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/16 个有
- `DifferentialDiffusion` —— 10/16 个有
- `JWStringConcat` —— 10/16 个有
- `ProcessString` —— 10/16 个有
- `Qwen3_VQA` —— 10/16 个有
- `Text Multiline` —— 10/16 个有
- `easy clearCacheAll` —— 10/16 个有
- `easy showAnything` —— 10/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 16 | 8% |
| 采样算法 | sa_solver | - | 16 | 94% |
| 调度器 | beta | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，16 个样本，取值分散，一致性仅 8%
- 采样算法 最常用 sa_solver，16 个样本，一致性 94%
- 调度器 最常用 beta，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、RIFE VFI、SimpleMath+、Text Multiline、easy cleanGpuUsed
