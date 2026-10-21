---
name: unknown_workflow_video_sampler_clip_234
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9515
common_nodes: [FaceAnalysisModels, FaceBoundingBox, ImageConcanate, ImagePadForOutpaint, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LaMa, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy imageConcat]
problems: []
missing: []
members: [视频生成/图生视频/1898044425526792194.json, 视频生成/图生视频/1902149239143555073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_234

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1898044425526792194.json、视频生成/图生视频/1902149239143555073.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `ImageConcanate`
- `ImagePadForOutpaint`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LaMa`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
