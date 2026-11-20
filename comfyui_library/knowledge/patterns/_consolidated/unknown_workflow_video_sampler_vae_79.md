---
name: unknown_workflow_video_sampler_vae_79
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.665
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Fun-V1.1-InP首尾帧(Wan2.1)_1905144833516965890.json, 视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json, 视频生成/图生视频/Wan VACE视频编辑参考双图出视频-KJ版_1908555077475573761.json, 视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json, 视频生成/图生视频/Wan万相VACE首尾帧_1908722738436186113.json, 视频生成/图生视频/通义万相最新VACE超级无限循环首尾帧图生视频_1908024871404904449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_79

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Fun-V1.1-InP首尾帧(Wan2.1)_1905144833516965890.json、视频生成/图生视频/WAN2.1 首尾帧 生成视频_1919985178293239809.json、视频生成/图生视频/Wan VACE视频编辑参考双图出视频-KJ版_1908555077475573761.json、视频生成/图生视频/Wan2.1-KJ首尾帧图生视频_1911321308582608897.json、视频生成/图生视频/Wan万相VACE首尾帧_1908722738436186113.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `ImageResizeKJ` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `LoadWanVideoClipTextEncoder` —— 3/6 个有
- `WanVideoClipVisionEncode` —— 3/6 个有
- `WanVideoImageToVideoEncode` —— 3/6 个有
- `WanVideoVACEEncode` —— 3/6 个有
- `WanVideoVRAMManagement` —— 3/6 个有
- `MaskPreview+` —— 2/6 个有
- `WanVideoVACEStartToEndFrame` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `ImageBatch` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy imageScaleDownToSize` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
