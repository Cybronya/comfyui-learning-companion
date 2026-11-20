---
name: unknown_workflow_video_sampler_vae_78
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.694714
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/AI一镜到底（FusionX_VACE_首尾帧）_2017158248306057218.json, 视频生成/图生视频/AI一镜到底（FusionX_VACE_首尾帧）_1936791366078746626.json, 视频生成/图生视频/Vace首尾帧工作流修复版_1913425967614783490.json, 视频生成/图生视频/Wan VACE视频编辑参考双图出视频-KJ版_1908555077475573761.json, 视频生成/图生视频/Wan万相VACE首尾帧_1908722738436186113.json, 视频生成/图生视频/多帧精细动作控制Wan2.1进阶工作流V1_1913228889936855042.json, 视频生成/图生视频/通义万相最新VACE超级首尾帧图生视频_1908024334332342274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_78

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/AI一镜到底（FusionX_VACE_首尾帧）_2017158248306057218.json、视频生成/图生视频/AI一镜到底（FusionX_VACE_首尾帧）_1936791366078746626.json、视频生成/图生视频/Vace首尾帧工作流修复版_1913425967614783490.json、视频生成/图生视频/Wan VACE视频编辑参考双图出视频-KJ版_1908555077475573761.json、视频生成/图生视频/Wan万相VACE首尾帧_1908722738436186113.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `WanVideoVACEStartToEndFrame` —— 6/7 个有
- `WanVideoTeaCache` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `ImageBatchMulti` —— 3/7 个有
- `JWImageExtractFromBatch` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `WanVideoVRAMManagement` —— 2/7 个有
- `easy batchAnything` —— 2/7 个有
- `easy forLoopEnd` —— 2/7 个有
- `easy forLoopStart` —— 2/7 个有
- `ImageConcanate` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `easy imageScaleDownToSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
