---
name: unknown_workflow_video_sampler_vae_146
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.941333
common_nodes: [DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, ImageResizeKJ, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1917046861591678978.json, 视频生成/图生视频/1917159345606295553.json, 视频生成/图生视频/1934084180739280897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_146

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1917046861591678978.json、视频生成/图生视频/1917159345606295553.json、视频生成/图生视频/1934084180739280897.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `ImageResizeKJ`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `DF_Integer` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `LoadWanVideoClipTextEncoder` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `SeargeFloatConstant` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
