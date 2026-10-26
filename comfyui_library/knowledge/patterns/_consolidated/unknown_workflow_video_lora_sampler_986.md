---
name: unknown_workflow_video_lora_sampler_986
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6375
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/童装动作迁移（一致性、表情、手部优化48G版）Wan2.2-Animate-V2_2033744399707934721.json, 视频生成/图生视频/超稳定 720x1280P Wan2.2超清 美女跳舞 动作迁移 表情+口型复刻_2017778215057629185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_986

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/童装动作迁移（一致性、表情、手部优化48G版）Wan2.2-Animate-V2_2033744399707934721.json、视频生成/图生视频/超稳定 720x1280P Wan2.2超清 美女跳舞 动作迁移 表情+口型复刻_2017778215057629185.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Display Int (rgthree)` —— 1/2 个有
- `DownloadAndLoadNLFModel` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `Float` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `NLFPredict` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PoseDetectionVitPoseToDWPose` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `RenderNLFPoses` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
