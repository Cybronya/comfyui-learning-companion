---
name: unknown_workflow_video_lora_sampler_359
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.907571
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Multitalk多人对话极速优化版 数字人对口型_1952655521791819778.json, 视频生成/图生视频/Multitalk最强数字人运镜参考版 运行加强版_1952724785534070786.json, 视频生成/图生视频/Wan2.1 InfiniteTalk 单人版_1990298374261927937.json, 视频生成/图生视频/Wan双人对口型不需要遮罩_2042473229025021954.json, 视频生成/图生视频/最强图生双人数字人万相2.1+Infinite Talk_1958149674144321538.json, 视频生成/图生视频/👾【大炮数字人】MultiTalk双人对口型加速版👾_1941429442441015297.json, 音频生成/音频生成/Multitalk单人唱歌数字人_1952348321673359361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_359

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Multitalk多人对话极速优化版 数字人对口型_1952655521791819778.json、视频生成/图生视频/Multitalk最强数字人运镜参考版 运行加强版_1952724785534070786.json、视频生成/图生视频/Wan2.1 InfiniteTalk 单人版_1990298374261927937.json、视频生成/图生视频/Wan双人对口型不需要遮罩_2042473229025021954.json、视频生成/图生视频/最强图生双人数字人万相2.1+Infinite Talk_1958149674144321538.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 6/7 个有
- `Int` —— 6/7 个有
- `LoadWanVideoT5TextEncoder` —— 6/7 个有
- `WanVideoImageToVideoMultiTalk` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `LayerUtility: PurgeVRAM V2` —— 4/7 个有
- `SaveAudio` —— 4/7 个有
- `SeparateMasks` —— 4/7 个有
- `MaskPreview+` —— 3/7 个有
- `WanVideoContextOptions` —— 3/7 个有
- `Audio Duration (mtb)` —— 2/7 个有
- `RH_GetAudioDuration` —— 2/7 个有
- `ToInt` —— 2/7 个有
- `AudioCombine` —— 1/7 个有
- `DF_Image_scale_to_side` —— 1/7 个有
- `Float to Int` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `WanVideoImageToVideoEncode` —— 1/7 个有
- `WanVideoTextEncodeCached` —— 1/7 个有
- `easy convertAnything` —— 1/7 个有
- `kkGetImage` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
