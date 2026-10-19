---
name: unknown_workflow_video_lora_sampler_173
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.838182
common_nodes: [CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1965504800706187266.json, 视频生成/图生视频/2005591443018317826.json, 视频生成/图生视频/1961400191553355778.json, 视频生成/图生视频/1963526752599511041.json, 视频生成/图生视频/1958284606359420930.json, 视频生成/图生视频/1955211129968627714.json, 视频生成/图生视频/1959825457199919105.json, 视频生成/图生视频/1977593107141283841.json, 视频生成/文生视频/(正面）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2035404909490741250.json, 视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json, 音频生成/音频生成/AA--声音克隆数字人-InfiniteTalk对口型图生视频（情感控制）_2030212385763495938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_173

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1965504800706187266.json、视频生成/图生视频/2005591443018317826.json、视频生成/图生视频/1961400191553355778.json、视频生成/图生视频/1963526752599511041.json、视频生成/图生视频/1958284606359420930.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/11 个有
- `CR Prompt Text` —— 9/11 个有
- `DownloadAndLoadWav2VecModel` —— 9/11 个有
- `LoadAudio` —— 9/11 个有
- `MultiTalkWav2VecEmbeds` —— 9/11 个有
- `AudioSeparation` —— 8/11 个有
- `GetImageSizeAndCount` —— 8/11 个有
- `JWInteger` —— 8/11 个有
- `PreviewAny` —— 6/11 个有
- `CR Text` —— 3/11 个有
- `SimpleMath+` —— 3/11 个有
- `ImpactInt` —— 2/11 个有
- `JWFloat` —— 2/11 个有
- `JWIntegerToString` —— 2/11 个有
- `MultiTalkSilentEmbeds` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `1hew_AudioDuration` —— 1/11 个有
- `Float to Int` —— 1/11 个有
- `IndexTTS2Run` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `SaveAudio` —— 1/11 个有
- `SoundFlow_GetLength` —— 1/11 个有
- `WanVideoTorchCompileSettings` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
