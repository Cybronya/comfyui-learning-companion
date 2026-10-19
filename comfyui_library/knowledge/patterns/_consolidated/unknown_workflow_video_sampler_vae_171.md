---
name: unknown_workflow_video_sampler_vae_171
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.939333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [音频生成/音频生成/InfiniteTalk单人视频到视频_1958736757212753921.json, 音频生成/音频生成/数字人-InfiniteTalk-视频对口型工作流_2051512102539538434.json, 音频生成/音频生成/视频单人对口型_2029818322556035074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_171

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/InfiniteTalk单人视频到视频_1958736757212753921.json、音频生成/音频生成/数字人-InfiniteTalk-视频对口型工作流_2051512102539538434.json、音频生成/音频生成/视频单人对口型_2029818322556035074.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `WanVideoLoraSelectMulti` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `JWIntegerToString` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/3 个有
- `WanVideoUni3C_embeds` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
