---
name: unknown_workflow_video_sampler_vae_92
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.816333
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, INTConstant, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, WanVideoVRAMManagement]
problems: []
missing: []
members: [图片生成/图生图/一切的尽头都是直播-基于Wan的数字人FantasyTalking_1917560010056859650.json, 平台全量/FantasyTalking数字人技术_1921434542698086401.json, 平台全量/迄今为止最方便易玩的数字人项目~fantasytalking结合wan2.1_1917100472711184385.json, 数字人/数字人/FantasyTalking_1918141698793476098.json, 数字人/数字人/小红书电商图数字人一致性+多图组合_1931339062307651586.json, 视频生成/图生视频/FantasyTalking_1919743926129852417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_92

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一切的尽头都是直播-基于Wan的数字人FantasyTalking_1917560010056859650.json、平台全量/FantasyTalking数字人技术_1921434542698086401.json、平台全量/迄今为止最方便易玩的数字人项目~fantasytalking结合wan2.1_1917100472711184385.json、数字人/数字人/FantasyTalking_1918141698793476098.json、数字人/数字人/小红书电商图数字人一致性+多图组合_1931339062307651586.json…）

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
- `WanVideoVRAMManagement`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `ImageResizeKJ` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `AudioCrop` —— 3/6 个有
- `CR Integer To String` —— 3/6 个有
- `CreateCFGScheduleFloatList` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `PreviewAudio` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `WanVideoContextOptions` —— 2/6 个有
- `DF_Image_scale_to_side` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `RH_ComfyFluxKontext` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `easy imageRemBg` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
