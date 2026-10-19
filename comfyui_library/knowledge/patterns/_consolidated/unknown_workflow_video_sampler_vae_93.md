---
name: unknown_workflow_video_sampler_vae_93
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8442
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, INTConstant, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1917005137418850305.json, 视频生成/图生视频/1917980090234241025.json, 视频生成/图生视频/1916975987429408770.json, 视频生成/图生视频/1917158732864884738.json, 视频生成/图生视频/1917403331021438977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_93

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1917005137418850305.json、视频生成/图生视频/1917980090234241025.json、视频生成/图生视频/1916975987429408770.json、视频生成/图生视频/1917158732864884738.json、视频生成/图生视频/1917403331021438977.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `INTConstant`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 4/5 个有
- `ImageResizeKJ` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `Primitive integer [Crystools]` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `WanVideoContextOptions` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `IndexTTSNode` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有
- `WanVideoVRAMManagement` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
