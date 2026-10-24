---
name: unknown_workflow_video_sampler_vae_84
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.72
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/AI一镜到底（FusionX_VACE_首尾帧）_2017158248306057218.json, 视频生成/图生视频/AI一镜到底（FusionX_VACE_首尾帧）_1936791366078746626.json, 视频生成/图生视频/VACE-14B首尾视频生成_1922637708198559745.json, 视频生成/图生视频/VACE-14B首尾视频生成_1922829567898304514.json, 视频生成/图生视频/Vace 14B非对称逆推理尾帧参考FLF2V图生视频V1_1924821785194524673.json, 视频生成/图生视频/多帧精细动作控制Wan2.1进阶工作流V1_1913228889936855042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_84

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/AI一镜到底（FusionX_VACE_首尾帧）_2017158248306057218.json、视频生成/图生视频/AI一镜到底（FusionX_VACE_首尾帧）_1936791366078746626.json、视频生成/图生视频/VACE-14B首尾视频生成_1922637708198559745.json、视频生成/图生视频/VACE-14B首尾视频生成_1922829567898304514.json、视频生成/图生视频/Vace 14B非对称逆推理尾帧参考FLF2V图生视频V1_1924821785194524673.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
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
- `MaskPreview+` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `WanVideoTeaCache` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `ImageBatchMulti` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `WanVideoVACEModelSelect` —— 3/6 个有
- `easy batchAnything` —— 3/6 个有
- `JWImageExtractFromBatch` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `Note Plus (mtb)` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `easy forLoopEnd` —— 2/6 个有
- `easy forLoopStart` —— 2/6 个有
- `Image Blank` —— 1/6 个有
- `ImageFromBatch+` —— 1/6 个有
- `LayerMask: MaskPreview` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
