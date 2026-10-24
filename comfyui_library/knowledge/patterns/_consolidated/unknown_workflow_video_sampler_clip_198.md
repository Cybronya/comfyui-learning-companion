---
name: unknown_workflow_video_sampler_clip_198
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.950667
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【最新】万相首尾帧FunInP版_1915338819028324353.json, 视频生成/图生视频/【首尾帧】通义万相WAN2.1 首尾帧视频动画生成_1912089601203236866.json, 视频生成/文生视频/最新wan2.1万相首尾帧FunInP版万相首尾帧FunInP版_1918947827957825538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_198

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【最新】万相首尾帧FunInP版_1915338819028324353.json、视频生成/图生视频/【首尾帧】通义万相WAN2.1 首尾帧视频动画生成_1912089601203236866.json、视频生成/文生视频/最新wan2.1万相首尾帧FunInP版万相首尾帧FunInP版_1918947827957825538.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageListToImageBatch` —— 2/3 个有
- `ImageUpscaleWithModelBatched` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
