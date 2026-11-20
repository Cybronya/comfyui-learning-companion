---
name: unknown_workflow_video_lora_sampler_949
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9735
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DrawViTPose, ImageResizeKJv2, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy getNode, easy int, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["视频生成/图生视频/【推荐,动态增强】Wan-animate动作迁移_视频转绘_2009846390779809793.json", "视频生成/图生视频/【推荐,动态增强】Wan-animate角色替换_2009846422258065410.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_949

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【推荐,动态增强】Wan-animate动作迁移_视频转绘_2009846390779809793.json、视频生成/图生视频/【推荐,动态增强】Wan-animate角色替换_2009846422258065410.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DrawViTPose`
- `ImageResizeKJv2`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy getNode`
- `easy int`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 1/2 个有
- `DrawMaskOnImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `Int` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy framesEditor` —— 1/2 个有
- `easy sam3ModelLoader` —— 1/2 个有
- `easy sam3VideoSegmentation` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
