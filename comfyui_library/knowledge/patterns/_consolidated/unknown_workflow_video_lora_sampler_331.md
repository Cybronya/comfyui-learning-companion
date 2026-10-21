---
name: unknown_workflow_video_lora_sampler_331
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.842429
common_nodes: [AudioCrop, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1994726030126555137.json, 视频生成/图生视频/1980685750213722114.json, 视频生成/图生视频/1971615313714475009.json, 视频生成/图生视频/1961304716842045442.json, 视频生成/图生视频/1958284606359420930.json, 视频生成/图生视频/1955211129968627714.json, 音频生成/音频生成/对口型数字人Infinite+Talk_1977882176555470849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_331

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1994726030126555137.json、视频生成/图生视频/1980685750213722114.json、视频生成/图生视频/1971615313714475009.json、视频生成/图生视频/1961304716842045442.json、视频生成/图生视频/1958284606359420930.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 5/7 个有
- `CR Prompt Text` —— 4/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `JWInteger` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `ImpactInt` —— 3/7 个有
- `JWIntegerToString` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `GetAudioDurationFromAudio` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `easy convertAnything` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
