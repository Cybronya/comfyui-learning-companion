---
name: unknown_workflow_video_sampler_vae_56
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.797
common_nodes: [DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, ImageFromBatch+, ImageMirror, ImageRepeat, ImageResizeKJ, ImpactSwitch, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, OpenposePreprocessor, VHS_LoadVideo, VHS_MergeImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX controlnet控制稳定双倍加速版视频转绘_1933785528938450945.json, 视频生成/图生视频/FusionX+VACE深度_姿势控制稳定双倍加速版视频转绘V1_1933557560941395970.json, 视频生成/图生视频/VACE 1.3B正式版双重引导姿势_深度稳定加速版V1_1924678755254456322.json, 视频生成/图生视频/VACE 14B图像参考双重引导姿势及深度控制视频生视频V2_1922710757258006529.json, 视频生成/图生视频/VACE图像参考双重引导姿势及深度控制视频生视频V1_1907443729060532226.json, 视频生成/图生视频/Wan2.1 FusionX-VACE动作迁移加速工作流_1933759507254435841.json, 视频生成/图生视频/Wan2.1-FusionX-VACE动作迁移_1933708885247352833.json, 视频生成/图生视频/视频动作迁移｜高清 720P｜深度+open pose 控制_1937848032371064834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_56

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/FusionX controlnet控制稳定双倍加速版视频转绘_1933785528938450945.json、视频生成/图生视频/FusionX+VACE深度_姿势控制稳定双倍加速版视频转绘V1_1933557560941395970.json、视频生成/图生视频/VACE 1.3B正式版双重引导姿势_深度稳定加速版V1_1924678755254456322.json、视频生成/图生视频/VACE 14B图像参考双重引导姿势及深度控制视频生视频V2_1922710757258006529.json、视频生成/图生视频/VACE图像参考双重引导姿势及深度控制视频生视频V1_1907443729060532226.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `ImageFromBatch+`
- `ImageMirror`
- `ImageRepeat`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JWInteger`
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
- `PreviewImage` —— 7/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `WanVideoTeaCache` —— 6/8 个有
- `DF_Integer` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `Note Plus (mtb)` —— 4/8 个有
- `WanVideoVACEModelSelect` —— 3/8 个有
- `Blend` —— 2/8 个有
- `Note _O` —— 2/8 个有
- `WanVideoLoraSelect` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `ImageBlend` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
