---
name: unknown_workflow_video_lora_sampler_833
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.618
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Display Int (rgthree), DrawMaskOnImage, DrawViTPose, GetImageRangeFromBatch, GetNode, GrowMask, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PoseDetectionOneToAllAnimation, PreviewImage, Primitive integer [Crystools], RH_Translator, SDPoseOODLoader, SDPoseOODProcessor, SetNode, SimpleMath+, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, YOLOModelLoader, easy float, easy sam3ModelLoader, easy sam3VideoSegmentation, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Animate人物替全能版_2009039132361756673.json, 视频生成/图生视频/（换背景+人物替换_2039239856160772097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_833

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Animate人物替全能版_2009039132361756673.json、视频生成/图生视频/（换背景+人物替换_2039239856160772097.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Display Int (rgthree)`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMask`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RH_Translator`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `SimpleMath+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `YOLOModelLoader`
- `easy float`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CM_IntToFloat` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `GroundingDinoModelLoader_SDPose` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `Text` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `easy convertAnything` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 63 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 63，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 63，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
