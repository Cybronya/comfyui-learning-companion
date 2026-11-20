---
name: unknown_workflow_controlnet_video_sampler
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.902
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DF_Integer, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_Captioner, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX+Multitalk 数字人_1945004776141807618.json, 视频生成/图生视频/MultiTalk：超6倍加速，超逼真顶流K歌数字人_1936605606658625537.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/FusionX+Multitalk 数字人_1945004776141807618.json、视频生成/图生视频/MultiTalk：超6倍加速，超逼真顶流K歌数字人_1936605606658625537.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DF_Integer`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RH_Captioner`
- `ShowText|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `IndexTTSNode` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `ttN concat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
