---
name: unknown_workflow_video_sampler_clip_151
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.954
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1913080907685687298.json, 视频生成/图生视频/1915338819028324353.json, 视频生成/图生视频/1912089601203236866.json, 视频生成/文生视频/1918947827957825538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1913080907685687298.json、视频生成/图生视频/1915338819028324353.json、视频生成/图生视频/1912089601203236866.json、视频生成/文生视频/1918947827957825538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ImageListToImageBatch` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `ImageUpscaleWithModelBatched` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `easy int` —— 2/4 个有
- `easy positive` —— 2/4 个有
- `CR Upscale Image` —— 1/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `Int` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
