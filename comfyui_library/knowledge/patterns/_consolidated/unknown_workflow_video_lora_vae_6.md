---
name: unknown_workflow_video_lora_vae_6
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.920375
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/最强数字人InfiniteTalk_1981009825838546946.json, 数字人/数字人/空白工作流_1942131715920052225.json, 数字人/数字人/语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801.json, 视频生成/图生视频/Aiwood-infinitetalk双人对话_1957826997610446849.json, 视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json, 视频生成/图生视频/InfiniteTalk+IndexTTS+Kontext数字人带货_1958084173951094786.json, 视频生成/图生视频/MultiTalk+IndexTTS+Kontext数字人带货_1937830211084029954.json, 音频生成/音频生成/InfiniteTalk+数字人口播带货_1973224776535814145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_6

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/最强数字人InfiniteTalk_1981009825838546946.json、数字人/数字人/空白工作流_1942131715920052225.json、数字人/数字人/语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801.json、视频生成/图生视频/Aiwood-infinitetalk双人对话_1957826997610446849.json、视频生成/图生视频/Digital Avatars for E-commerce InfiniteTalk +数字人带货_2095704577696948225.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTalkWav2VecEmbeds` —— 7/8 个有
- `PreviewAudio` —— 7/8 个有
- `WanVideoSampler` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `WanVideoTorchCompileSettings` —— 6/8 个有
- `IndexTTSRun` —— 5/8 个有
- `LayerUtility: PurgeVRAM V2` —— 5/8 个有
- `String Literal` —— 5/8 个有
- `WanVideoImageToVideoMultiTalk` —— 5/8 个有
- `ImageConcanate` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `RH_ComfyFluxKontext` —— 4/8 个有
- `RH_Translator` —— 4/8 个有
- `SaveImage` —— 4/8 个有
- `WanVideoImageToVideoEncode` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `IndexTTSNode` —— 1/8 个有
- `MaskPreview+` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `SeparateMasks` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
