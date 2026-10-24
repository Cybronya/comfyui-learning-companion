---
name: unknown_workflow_video_lora_sampler_245
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.953875
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json, 视频生成/图生视频/InfiniteTalk 图片生成单人唱歌视频（不限生成时长）_1957828185982599170.json, 视频生成/图生视频/InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json, 视频生成/图生视频/MultiTalk+IndexTTS+Kontext数字人带货_1937830211084029954.json, 视频生成/图生视频/MultiTalk对口型（万相实现）_1937838193955749889.json, 视频生成/图生视频/开源顶流MultiTalk Kijai版单人工作流_1936154909266055170.json, 视频生成/文生视频/wanvideo_multitalk_test_01g_1978251602106703873.json, 音频生成/音频生成/InfiniteTalk+数字人口播带货_1973224776535814145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_245

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json、视频生成/图生视频/InfiniteTalk 图片生成单人唱歌视频（不限生成时长）_1957828185982599170.json、视频生成/图生视频/InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json、视频生成/图生视频/MultiTalk+IndexTTS+Kontext数字人带货_1937830211084029954.json、视频生成/图生视频/MultiTalk对口型（万相实现）_1937838193955749889.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/8 个有
- `ImageConcanate` —— 4/8 个有
- `IndexTTSRun` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `LayerUtility: PurgeVRAM V2` —— 4/8 个有
- `PreviewAudio` —— 4/8 个有
- `RH_ComfyFluxKontext` —— 4/8 个有
- `RH_Translator` —— 4/8 个有
- `SaveImage` —— 4/8 个有
- `String Literal` —— 4/8 个有
- `WanVideoImageToVideoEncode` —— 4/8 个有
- `WanVideoImageToVideoMultiTalk` —— 4/8 个有
- `CreateCFGScheduleFloatList` —— 3/8 个有
- `WanVideoContextOptions` —— 3/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `WanVideoEncode` —— 2/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/8 个有
- `WanVideoUni3C_embeds` —— 2/8 个有
- `VHS_DuplicateImages` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
