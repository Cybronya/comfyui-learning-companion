---
name: unknown_workflow_video_sampler_vae_97
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8982
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FLF2V首尾帧-wan视频_1913077859026698242.json, 视频生成/图生视频/FLF2V首尾帧图生视频_1913525261151760386.json, 视频生成/图生视频/FLF2V首尾帧高质量视频_1916010425433915394.json, 视频生成/图生视频/Wan2.1-Fun-图生视频_1907320238373756930.json, 视频生成/图生视频/wan姿态控制图生视频_1914987342183002113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_97

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/FLF2V首尾帧-wan视频_1913077859026698242.json、视频生成/图生视频/FLF2V首尾帧图生视频_1913525261151760386.json、视频生成/图生视频/FLF2V首尾帧高质量视频_1916010425433915394.json、视频生成/图生视频/Wan2.1-Fun-图生视频_1907320238373756930.json、视频生成/图生视频/wan姿态控制图生视频_1914987342183002113.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 4/5 个有
- `LoadWanVideoClipTextEncoder` —— 4/5 个有
- `WanVideoExperimentalArgs` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `DF_Integer` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy clearCacheAll` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `Evaluate Integers` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `KepStringLiteral` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/5 个有
- `WanVideoUniAnimatePoseInput` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
