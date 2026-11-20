---
name: unknown_workflow_video_sampler_vae_197
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.876667
common_nodes: [DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, ImageFromBatch+, ImageMirror, ImageRepeat, ImageResizeKJ, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, OpenposePreprocessor, VHS_LoadVideo, VHS_MergeImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 FusionX-VACE动作迁移加速工作流_1933759507254435841.json, 视频生成/图生视频/Wan2.1-FusionX-VACE动作迁移_1933708885247352833.json, 视频生成/图生视频/视频动作迁移｜高清 720P｜深度+open pose 控制_1937848032371064834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_197

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 FusionX-VACE动作迁移加速工作流_1933759507254435841.json、视频生成/图生视频/Wan2.1-FusionX-VACE动作迁移_1933708885247352833.json、视频生成/图生视频/视频动作迁移｜高清 720P｜深度+open pose 控制_1937848032371064834.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `ImageFromBatch+`
- `ImageMirror`
- `ImageRepeat`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `OpenposePreprocessor`
- `VHS_LoadVideo`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `WanVideoTeaCache` —— 2/3 个有
- `Blend` —— 1/3 个有
- `DF_Integer` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoVACEModelSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
