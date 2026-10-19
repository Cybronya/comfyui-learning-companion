---
name: unknown_workflow_video_sampler_vae_36
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7242
common_nodes: [EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936791366078746626.json, 视频生成/图生视频/1951187088609882114.json, 视频生成/图生视频/1948561964491517953.json, 视频生成/图生视频/1945679647550132225.json, 视频生成/图生视频/1945794498888658946.json, 视频生成/图生视频/1922637708198559745.json, 视频生成/图生视频/1922829567898304514.json, 视频生成/图生视频/1913425967614783490.json, 视频生成/图生视频/1908722738436186113.json, 视频生成/图生视频/1936038942514794498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_36

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1936791366078746626.json、视频生成/图生视频/1951187088609882114.json、视频生成/图生视频/1948561964491517953.json、视频生成/图生视频/1945679647550132225.json、视频生成/图生视频/1945794498888658946.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 10 个 workflow 都包含：
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 9/10 个有
- `MaskPreview+` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `WanVideoTeaCache` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `WanVideoVACEModelSelect` —— 7/10 个有
- `WanVideoLoraSelect` —— 5/10 个有
- `WanVideoTorchCompileSettings` —— 5/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `WanVideoVRAMManagement` —— 2/10 个有
- `easy batchAnything` —— 2/10 个有
- `GetImageRangeFromBatch` —— 1/10 个有
- `ImageBatchMulti` —— 1/10 个有
- `Int` —— 1/10 个有
- `JWImageExtractFromBatch` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `MimicMotionGetPoses` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `TextInput_` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `easy forLoopEnd` —— 1/10 个有
- `easy forLoopStart` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
