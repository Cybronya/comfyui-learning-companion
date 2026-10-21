---
name: unknown_workflow_video_lora_sampler_499
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88825
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1935517982800150530.json, 视频生成/图生视频/1944781306624397314.json, 视频生成/图生视频/1941396132272750594.json, 视频生成/图生视频/1914987342183002113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_499

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1935517982800150530.json、视频生成/图生视频/1944781306624397314.json、视频生成/图生视频/1941396132272750594.json、视频生成/图生视频/1914987342183002113.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `DF_Integer` —— 2/4 个有
- `EmptyImage` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `WanVideoSLG` —— 2/4 个有
- `WanVideoTeaCache` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/4 个有
- `WanVideoUniAnimatePoseInput` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
