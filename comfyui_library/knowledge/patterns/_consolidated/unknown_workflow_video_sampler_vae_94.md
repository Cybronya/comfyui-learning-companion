---
name: unknown_workflow_video_sampler_vae_94
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.733
common_nodes: [ADE_CameraPoseBasic, GetNode, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoFunCameraEmbeds, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1918711068057866241.json, 视频生成/图生视频/1922871224979046401.json, 视频生成/图生视频/2043494570079559681.json, 视频生成/图生视频/1917857129724575746.json, 视频生成/图生视频/1923702725929070593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_94

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1918711068057866241.json、视频生成/图生视频/1922871224979046401.json、视频生成/图生视频/2043494570079559681.json、视频生成/图生视频/1917857129724575746.json、视频生成/图生视频/1923702725929070593.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 5 个 workflow 都包含：
- `ADE_CameraPoseBasic`
- `GetNode`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoFunCameraEmbeds`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `CameraPoseVisualizer` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ColorMatch` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `RIFE VFI` —— 2/5 个有
- `Text` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
