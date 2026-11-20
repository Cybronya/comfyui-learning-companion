---
name: unknown_workflow_video_sampler_vae_98
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.816833
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json, 视频生成/图生视频/(修复版)FantasyTalking阿里数字人对口型框架(wan2.1)_1917005137418850305.json, 视频生成/图生视频/FantasyTalking WAN2.1 数字人口播，完美对嘴型_1917980090234241025.json, 视频生成/图生视频/FantasyTalking+Cosyvoice2数字人4倍加速优化版V2（base）_1917274525388705794.json, 视频生成/图生视频/FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json, 视频生成/图生视频/FantasyTalking对口型_1917403331021438977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_98

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/逼真自然数字人-图像+音频驱动-FantasyTalking-Wan2.1_1918301411795472385.json、视频生成/图生视频/(修复版)FantasyTalking阿里数字人对口型框架(wan2.1)_1917005137418850305.json、视频生成/图生视频/FantasyTalking WAN2.1 数字人口播，完美对嘴型_1917980090234241025.json、视频生成/图生视频/FantasyTalking+Cosyvoice2数字人4倍加速优化版V2（base）_1917274525388705794.json、视频生成/图生视频/FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json…）

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
- `CreateCFGScheduleFloatList` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `ImageResizeKJ` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `WanVideoContextOptions` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `NTCosyVoiceCrossLingualSampler` —— 2/6 个有
- `NTCosyVoiceInstruct2Sampler` —— 2/6 个有
- `NTCosyVoiceZeroShotSampler` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `Primitive integer [Crystools]` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `WanVideoEnhanceAVideo` —— 2/6 个有
- `WanVideoExperimentalArgs` —— 2/6 个有
- `WanVideoSLG` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `WanVideoVRAMManagement` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
