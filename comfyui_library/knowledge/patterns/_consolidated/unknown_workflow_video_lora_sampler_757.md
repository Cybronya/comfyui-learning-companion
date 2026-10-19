---
name: unknown_workflow_video_lora_sampler_757
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9525
common_nodes: [AudioCombine, AudioSeparation, CLIPVisionLoader, CR SDXL Aspect Ratio, DF_Int_to_Float, DownloadAndLoadWav2VecModel, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveInt, RH_GetAudioDuration, RH_Translator, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1957982233535639554.json, 视频生成/图生视频/1988128458423312386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_757

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1957982233535639554.json、视频生成/图生视频/1988128458423312386.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCombine`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR SDXL Aspect Ratio`
- `DF_Int_to_Float`
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveInt`
- `RH_GetAudioDuration`
- `RH_Translator`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 1/2 个有
- `PurgeVRAM_UTK` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
