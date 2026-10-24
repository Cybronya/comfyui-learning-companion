---
name: unknown_workflow_video_sampler_vae_82
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.821833
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, INTConstant, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/一切的尽头都是直播-基于Wan的数字人FantasyTalking_1917560010056859650.json, 视频生成/图生视频/(修复版)FantasyTalking阿里数字人对口型框架(wan2.1)_1917005137418850305.json, 视频生成/图生视频/FantasyTalking WAN2.1 数字人口播，完美对嘴型_1917980090234241025.json, 视频生成/图生视频/FantasyTalking wan数字人工作流（静态肖像→超拟真说话视频）_1916975987429408770.json, 视频生成/图生视频/FantasyTalking_1919743926129852417.json, 视频生成/图生视频/FantasyTalking对口型_1917403331021438977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_82

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一切的尽头都是直播-基于Wan的数字人FantasyTalking_1917560010056859650.json、视频生成/图生视频/(修复版)FantasyTalking阿里数字人对口型框架(wan2.1)_1917005137418850305.json、视频生成/图生视频/FantasyTalking WAN2.1 数字人口播，完美对嘴型_1917980090234241025.json、视频生成/图生视频/FantasyTalking wan数字人工作流（静态肖像→超拟真说话视频）_1916975987429408770.json、视频生成/图生视频/FantasyTalking_1919743926129852417.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `INTConstant`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
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
- `CreateCFGScheduleFloatList` —— 4/6 个有
- `ImageResizeKJ` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `WanVideoContextOptions` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `WanVideoVRAMManagement` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `Primitive integer [Crystools]` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `CR Integer To String` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `WanVideoEnhanceAVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
