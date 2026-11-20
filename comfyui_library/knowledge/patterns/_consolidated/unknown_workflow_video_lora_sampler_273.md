---
name: unknown_workflow_video_lora_sampler_273
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9217
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Aiwood-首发Multitalk多人对话_1940854355119730690.json, 数字人/数字人/Multitalk多人对话（超级版）_1941152199026307073.json, 数字人/数字人/数字人图片对口型_2027596633734647810.json, 数字人/数字人/数字人对口型-infinitetalk_1969380544364617729.json, 数字人/数字人/超自然图片数字人对口型（根叔）_1977237089068687361.json, 视频生成/图生视频/CCC的InfiniteTalk数字人_2026963272511000578.json, 视频生成/图生视频/INF双人对话_1971453748994359297.json, 视频生成/图生视频/IndexTTS2+InfiniteTalk图生数字人单人-B站UP主@好奇漫步!音频数字人同时生成_1983563401169444866.json, 视频生成/图生视频/Multitalk多人对话极速优化版 数字人对口型_1952655521791819778.json, 视频生成/图生视频/Multitalk最强数字人运镜参考版 运行加强版_1952724785534070786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_273

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/Aiwood-首发Multitalk多人对话_1940854355119730690.json、数字人/数字人/Multitalk多人对话（超级版）_1941152199026307073.json、数字人/数字人/数字人图片对口型_2027596633734647810.json、数字人/数字人/数字人对口型-infinitetalk_1969380544364617729.json、数字人/数字人/超自然图片数字人对口型（根叔）_1977237089068687361.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
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
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `AudioCrop` —— 8/10 个有
- `AudioSeparation` —— 8/10 个有
- `WanVideoTextEncode` —— 8/10 个有
- `SimpleMath+` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `Int` —— 5/10 个有
- `MaskPreview+` —— 5/10 个有
- `SeparateMasks` —— 5/10 个有
- `ToInt` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `SaveAudio` —— 3/10 个有
- `Audio Duration (mtb)` —— 2/10 个有
- `EsesImageEffectBloom` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `RH_GetAudioDuration` —— 2/10 个有
- `SaveAudioMP3` —— 2/10 个有
- `WanVideoApplyNAG` —— 2/10 个有
- `WanVideoContextOptions` —— 2/10 个有
- `WanVideoTextEncodeSingle` —— 2/10 个有
- `INTConstant` —— 1/10 个有
- `IndexTTS2_Emotion` —— 1/10 个有
- `PreviewAudio` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
