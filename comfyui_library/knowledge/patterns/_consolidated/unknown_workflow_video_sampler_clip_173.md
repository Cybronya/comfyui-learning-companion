---
name: unknown_workflow_video_sampler_clip_173
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.591
common_nodes: [CLIPTextEncode, CLIPVisionEncode, DrawViTPose, GetNode, ImageConcatMulti, ImageResizeKJv2, ImpactSwitch, JjkText, KSampler, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, Primitive integer [Crystools], RHHiddenNodes, SetNode, SimpleMath+, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, WanAnimateToVideo, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json, 视频生成/图生视频/完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json, 视频生成/图生视频/完美视频人物替换  V3_2007121113012248578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_173

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json、视频生成/图生视频/完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json、视频生成/图生视频/完美视频人物替换  V3_2007121113012248578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DrawViTPose`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `SetNode`
- `SimpleMath+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `WanAnimateToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `ImageBlend` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `Sam2Segmentation` —— 1/3 个有
- `WanVideoBlockSwap` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 1 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 67% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
