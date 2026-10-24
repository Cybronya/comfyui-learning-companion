---
name: unknown_workflow_video_lora_sampler_918
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9155
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy anythingIndexSwitch]
problems: []
missing: []
members: [视频生成/文生视频/AI Video Studio PR插件专用 数字人口播(照片)工作流_2094330406354120705.json, 视频生成/文生视频/数字人带货视频 数字人口播 美妆模特 主播 静态图一键生成带货_2074320987222528002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_918

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/AI Video Studio PR插件专用 数字人口播(照片)工作流_2094330406354120705.json、视频生成/文生视频/数字人带货视频 数字人口播 美妆模特 主播 静态图一键生成带货_2074320987222528002.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_GetAudioDuration` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
