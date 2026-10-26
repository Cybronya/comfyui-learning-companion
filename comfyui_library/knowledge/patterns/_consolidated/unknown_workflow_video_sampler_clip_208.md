---
name: unknown_workflow_video_sampler_clip_208
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.965333
common_nodes: [AIO_Preprocessor, ImageResizeKJ, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【跳舞视频 】最新wan2.1上传图片生成跳舞视频_1912765246451216385.json, 视频生成/图生视频/通义万相Wan2.1-Fun-图生视频转绘_1907644066044252162.json, 视频生成/文生视频/WAN FAN首尾帧工作流_1906315512241131522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_208

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【跳舞视频 】最新wan2.1上传图片生成跳舞视频_1912765246451216385.json、视频生成/图生视频/通义万相Wan2.1-Fun-图生视频转绘_1907644066044252162.json、视频生成/文生视频/WAN FAN首尾帧工作流_1906315512241131522.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `JanusImageUnderstanding` —— 2/3 个有
- `JanusModelLoader` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `ImageBlend` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `Int` —— 1/3 个有
- `KepStringLiteral` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
