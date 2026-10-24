---
name: unknown_workflow_video_sampler_vae_152
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.773333
common_nodes: [CLIPVisionLoader, CreateCFGScheduleFloatList, DownloadAndLoadWav2VecModel, FantasyTalkingModelLoader, FantasyTalkingWav2VecEmbeds, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FantasyTalking+Cosyvoice2数字人4倍加速优化版V2（base）_1917274525388705794.json, 视频生成/图生视频/FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json, 视频生成/图生视频/终极数字人 FantasyTalking_1933459219561500673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_152

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/FantasyTalking+Cosyvoice2数字人4倍加速优化版V2（base）_1917274525388705794.json、视频生成/图生视频/FantasyTalking+Cosyvoice数字人Skyreels v2 I2V稳定加速版V2_1917039782952632322.json、视频生成/图生视频/终极数字人 FantasyTalking_1933459219561500673.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadWav2VecModel`
- `FantasyTalkingModelLoader`
- `FantasyTalkingWav2VecEmbeds`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
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
- `JWInteger` —— 2/3 个有
- `NTCosyVoiceCrossLingualSampler` —— 2/3 个有
- `NTCosyVoiceInstruct2Sampler` —— 2/3 个有
- `NTCosyVoiceZeroShotSampler` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `LayerUtility: TextBox` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有
- `WanVideoVRAMManagement` —— 1/3 个有
- `easy textSwitch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
