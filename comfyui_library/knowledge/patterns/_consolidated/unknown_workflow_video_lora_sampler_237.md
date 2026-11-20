---
name: unknown_workflow_video_lora_sampler_237
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.789111
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/MultiTalk数字人 加音色克隆_1948371393818832898.json, 数字人/数字人/Multitalk单人数字人_1950219733892251649.json, 数字人/数字人/multitalk_数字人_1964494594597638145.json, 数字人/数字人/multitalk数字人工作流-单人_1945780376977678338.json, 数字人/数字人/数字人对口型（超时长）_2000509474429431809.json, 视频生成/图生视频/KJ加速版-顶流MultiTalk万能数字人_1940583682262413314.json, 视频生成/图生视频/Multitalk 数字人运镜参考版｜稳定运行_1936961854306439170.json, 视频生成/图生视频/Multitalk最强数字人-灵动版_1953292063418814466.json, 视频生成/图生视频/工作流视频篇12-AI图生数字人加运镜参考_2018299977335840769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_237

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/MultiTalk数字人 加音色克隆_1948371393818832898.json、数字人/数字人/Multitalk单人数字人_1950219733892251649.json、数字人/数字人/multitalk_数字人_1964494594597638145.json、数字人/数字人/multitalk数字人工作流-单人_1945780376977678338.json、数字人/数字人/数字人对口型（超时长）_2000509474429431809.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/9 个有
- `AudioSeparation` —— 8/9 个有
- `WanVideoContextOptions` —— 8/9 个有
- `LayerUtility: PurgeVRAM V2` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `WanVideoUni3C_ControlnetLoader` —— 7/9 个有
- `SimpleMath+` —— 6/9 个有
- `VHS_DuplicateImages` —— 6/9 个有
- `WanVideoEncode` —— 6/9 个有
- `WanVideoUni3C_embeds` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `INTConstant` —— 5/9 个有
- `ImageResizeKJ` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `JWIntegerToString` —— 4/9 个有
- `PrimitiveInt` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `RH_Captioner` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `easy anythingIndexSwitch` —— 3/9 个有
- `GetNode` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `Audio Duration (mtb)` —— 1/9 个有
- `IndexTTSRun` —— 1/9 个有
- `Int` —— 1/9 个有
- `Note _O` —— 1/9 个有
- `PreviewAudio` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_GetAudioDuration` —— 1/9 个有
- `String Literal` —— 1/9 个有
- `WanVideoEnhanceAVideo` —— 1/9 个有
- `WanVideoSLG` —— 1/9 个有
- `easy convertAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
