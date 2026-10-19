---
name: unknown_workflow_video_sampler_vae_56
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8605
common_nodes: [ImageResizeKJ, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1922660439551873025.json, 视频生成/图生视频/1934429538858266626.json, 视频生成/图生视频/1926978789408952322.json, 视频生成/图生视频/1909879938038624257.json, 视频生成/图生视频/1908555077475573761.json, 视频生成/图生视频/2057296595577823234.json, 视频生成/图生视频/1911760861873274882.json, 视频生成/图生视频/1908024871404904449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_56

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1922660439551873025.json、视频生成/图生视频/1934429538858266626.json、视频生成/图生视频/1926978789408952322.json、视频生成/图生视频/1909879938038624257.json、视频生成/图生视频/1908555077475573761.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `WanVideoBlockSwap` —— 7/8 个有
- `WanVideoExperimentalArgs` —— 7/8 个有
- `WanVideoSLG` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `WanVideoVACEModelSelect` —— 5/8 个有
- `AIO_Preprocessor` —— 4/8 个有
- `AddLabel` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `TextInput_` —— 4/8 个有
- `WanVideoEnhanceAVideo` —— 4/8 个有
- `EmptyImage` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `INTConstant` —— 2/8 个有
- `ImageConcanate` —— 2/8 个有
- `MaskPreview+` —— 2/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `ImageBatch` —— 1/8 个有
- `ImagePadKJ` —— 1/8 个有
- `WanVideoVACEStartToEndFrame` —— 1/8 个有
- `WanVideoVRAMManagement` —— 1/8 个有
- `easy imageRemBg` —— 1/8 个有
- `easy imageScaleDownToSize` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
