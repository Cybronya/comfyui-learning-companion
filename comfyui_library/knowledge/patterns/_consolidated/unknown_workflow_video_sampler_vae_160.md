---
name: unknown_workflow_video_sampler_vae_160
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.983667
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1951958322155081729.json, 视频生成/图生视频/1916742861977751553.json, 视频生成/图生视频/1922989414665154562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_160

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1951958322155081729.json、视频生成/图生视频/1916742861977751553.json、视频生成/图生视频/1922989414665154562.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LayerUtility: TextBox` —— 2/3 个有
- `VHS_SelectEveryNthImage` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
