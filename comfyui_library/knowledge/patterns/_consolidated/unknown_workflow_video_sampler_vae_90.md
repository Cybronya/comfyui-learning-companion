---
name: unknown_workflow_video_sampler_vae_90
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.824
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, INTConstant, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/一切的尽头都是直播-基于Wan的数字人FantasyTalking_1917560010056859650.json, 数字人/数字人/FantasyTalking_1918141698793476098.json, 数字人/数字人/小红书电商图数字人一致性+多图组合_1931339062307651586.json, 数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json, 视频生成/图生视频/FantasyTalking_1919743926129852417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_90

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一切的尽头都是直播-基于Wan的数字人FantasyTalking_1917560010056859650.json、数字人/数字人/FantasyTalking_1918141698793476098.json、数字人/数字人/小红书电商图数字人一致性+多图组合_1931339062307651586.json、数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json、视频生成/图生视频/FantasyTalking_1919743926129852417.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

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
- `CreateCFGScheduleFloatList` —— 4/5 个有
- `ImageResizeKJ` —— 4/5 个有
- `WanVideoEnhanceAVideo` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `WanVideoVRAMManagement` —— 4/5 个有
- `AudioCrop` —— 3/5 个有
- `CR Integer To String` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `PreviewAudio` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `WanVideoContextOptions` —— 2/5 个有
- `DF_Image_scale_to_side` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `RH_ComfyFluxKontext` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `WanVideoExperimentalArgs` —— 1/5 个有
- `WanVideoSLG` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
