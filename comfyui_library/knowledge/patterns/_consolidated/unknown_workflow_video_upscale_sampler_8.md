---
name: unknown_workflow_video_upscale_sampler_8
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9415
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageUpscaleWithModel, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/自拍转视频_1919610093690884097.json, 视频生成/图生视频/趴地转视频_1918873507273576450.json, 视频生成/图生视频/通义万相Teacache加速图生视频_1896425086226726914.json, 视频生成/文生视频/图生视频_大摆锤舞蹈_1965243729651093506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/自拍转视频_1919610093690884097.json、视频生成/图生视频/趴地转视频_1918873507273576450.json、视频生成/图生视频/通义万相Teacache加速图生视频_1896425086226726914.json、视频生成/文生视频/图生视频_大摆锤舞蹈_1965243729651093506.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `Bjornulf_FreeVRAM` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `LayerUtility: TextJoin` —— 2/4 个有
- `TextInputBasic` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `WanVideoSLG` —— 2/4 个有
- `INTConstant` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
