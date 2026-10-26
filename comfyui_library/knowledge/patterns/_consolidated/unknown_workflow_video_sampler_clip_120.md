---
name: unknown_workflow_video_sampler_clip_120
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5778
common_nodes: [CLIPTextEncode, CLIPVisionEncode, DrawViTPose, GetNode, ImageResizeKJv2, KSampler, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, SetNode, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json, "视频生成/图生视频/完美动作迁移,(换！！)_2031965334302892033.json", 视频生成/图生视频/完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json, 视频生成/图生视频/完美视频人物替换  V3_2007121113012248578.json, 视频生成/图生视频/视频主体替换可切镜头Wan-Animate_1974073338375090178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/完美人物替换Animate 新3.2（真人替换）_1972999507698913281.json、视频生成/图生视频/完美动作迁移,(换！！)_2031965334302892033.json、视频生成/图生视频/完美动作迁移Animate 新 3.0（极致稳定+表情迁移）_1972602081016217602.json、视频生成/图生视频/完美视频人物替换  V3_2007121113012248578.json、视频生成/图生视频/视频主体替换可切镜头Wan-Animate_1974073338375090178.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有
- `ImpactSwitch` —— 4/5 个有
- `JjkText` —— 4/5 个有
- `Primitive integer [Crystools]` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `VHS_VideoInfoSource` —— 4/5 个有
- `BlockifyMask` —— 3/5 个有
- `CLIPLoader` —— 3/5 个有
- `DrawMaskOnImage` —— 3/5 个有
- `ImageBlend` —— 3/5 个有
- `RHHiddenNodes` —— 3/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/5 个有
- `EmptyImage` —— 2/5 个有
- `GIMMVFI_interpolate` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `OnnxDetectionModelLoader` —— 2/5 个有
- `wanBlockSwap` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GGUFLoaderKJ` —— 1/5 个有
- `GrowMask` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `ImageRemoveBackground+` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `RemBGSession+` —— 1/5 个有
- `Sam2Segmentation` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `WanVideoBlockSwap` —— 1/5 个有
- `WanVideoClipVisionEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 4 | 5 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | sa_solver | - | 5 | 80% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
