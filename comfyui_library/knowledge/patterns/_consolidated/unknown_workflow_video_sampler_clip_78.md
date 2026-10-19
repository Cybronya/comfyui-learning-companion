---
name: unknown_workflow_video_sampler_clip_78
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.565714
common_nodes: [CLIPTextEncode, CLIPVisionEncode, DrawViTPose, GetNode, ImageConcatMulti, ImageResizeKJv2, KSampler, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, PoseAndFaceDetection, SetNode, SimpleMath+, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2005510283697291266.json, 视频生成/图生视频/2031965334302892033.json, 视频生成/图生视频/1972602081016217602.json, 视频生成/图生视频/2007121113012248578.json, 视频生成/图生视频/2066142073039970306.json, 视频生成/图生视频/1987427784719011841.json, 视频生成/图生视频/2065766712460533761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_78

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2005510283697291266.json、视频生成/图生视频/2031965334302892033.json、视频生成/图生视频/1972602081016217602.json、视频生成/图生视频/2007121113012248578.json、视频生成/图生视频/2066142073039970306.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DrawViTPose`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `SetNode`
- `SimpleMath+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 6/7 个有
- `CLIPVisionLoader` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `OnnxDetectionModelLoader` —— 5/7 个有
- `UnetLoaderGGUF` —— 5/7 个有
- `wanBlockSwap` —— 5/7 个有
- `DF_Integer` —— 4/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `Int` —— 4/7 个有
- `StringToInt` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `easy sleep` —— 4/7 个有
- `ImpactSwitch` —— 3/7 个有
- `JjkText` —— 3/7 个有
- `ModelPatchTorchSettings` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `Primitive integer [Crystools]` —— 3/7 个有
- `VHS_VideoInfoSource` —— 3/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `BlockifyMask` —— 1/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `DrawMaskOnImage` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `ImageBlend` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 4 | 7 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | sa_solver | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 4，7 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
