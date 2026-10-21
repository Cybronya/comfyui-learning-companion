---
name: unknown_workflow_video_lora_sampler_693
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.914333
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/AI Video Studio PR插件专用 数字人口播(照片)工作流_2094330406354120705.json, 视频生成/文生视频/Wan2_1+infinite+数字人唱歌对口型_2064331203859279874.json, 视频生成/文生视频/数字人带货视频 数字人口播 美妆模特 主播 静态图一键生成带货_2074320987222528002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_693

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/AI Video Studio PR插件专用 数字人口播(照片)工作流_2094330406354120705.json、视频生成/文生视频/Wan2_1+infinite+数字人唱歌对口型_2064331203859279874.json、视频生成/文生视频/数字人带货视频 数字人口播 美妆模特 主播 静态图一键生成带货_2074320987222528002.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `Float to Int` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `RH_GetAudioDuration` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `Int` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `SoundFlow_TrimAudio` —— 1/3 个有
- `intToFloat _O` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
