---
name: unknown_workflow_video_sampler_vae_34
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.722818
common_nodes: [EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/AI一镜到底（FusionX_VACE_首尾帧）_2017158248306057218.json, 视频生成/图生视频/1936791366078746626.json, 视频生成/图生视频/1951187088609882114.json, 视频生成/图生视频/1948561964491517953.json, 视频生成/图生视频/1945679647550132225.json, 视频生成/图生视频/1945794498888658946.json, 视频生成/图生视频/1922637708198559745.json, 视频生成/图生视频/1922829567898304514.json, 视频生成/图生视频/1913425967614783490.json, 视频生成/图生视频/1908722738436186113.json, 视频生成/图生视频/1936038942514794498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_34

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/AI一镜到底（FusionX_VACE_首尾帧）_2017158248306057218.json、视频生成/图生视频/1936791366078746626.json、视频生成/图生视频/1951187088609882114.json、视频生成/图生视频/1948561964491517953.json、视频生成/图生视频/1945679647550132225.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 11 个 workflow 都包含：
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
- `AddLabel` —— 10/11 个有
- `MaskPreview+` —— 10/11 个有
- `PreviewImage` —— 10/11 个有
- `GetNode` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `WanVideoTeaCache` —— 9/11 个有
- `WanVideoVACEModelSelect` —— 7/11 个有
- `WanVideoTorchCompileSettings` —— 6/11 个有
- `WanVideoLoraSelect` —— 5/11 个有
- `MathExpression|pysssss` —— 3/11 个有
- `easy batchAnything` —— 3/11 个有
- `ImageBatchMulti` —— 2/11 个有
- `JWImageExtractFromBatch` —— 2/11 个有
- `JjkText` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `WanVideoVRAMManagement` —— 2/11 个有
- `easy forLoopEnd` —— 2/11 个有
- `easy forLoopStart` —— 2/11 个有
- `GetImageRangeFromBatch` —— 1/11 个有
- `Int` —— 1/11 个有
- `MimicMotionGetPoses` —— 1/11 个有
- `TextInput_` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
