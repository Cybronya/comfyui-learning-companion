---
name: unknown_workflow_video_sampler_vae_36
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.831545
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1996999462549655554.json, 视频生成/图生视频/1988898686707044353.json, 视频生成/图生视频/2026900959795879938.json, 视频生成/图生视频/2028672160373415937.json, 视频生成/图生视频/1960048260402589698.json, 视频生成/图生视频/2037816256153264129.json, 视频生成/图生视频/1984094280551694338.json, 视频生成/图生视频/2025798781039546370.json, 视频生成/图生视频/2041353094105141250.json, 视频生成/图生视频/2026920632201515010.json, 音频生成/音频生成/(歌曲数字人)全流程精准口型高强动作V4_1989287142675369986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_36

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1996999462549655554.json、视频生成/图生视频/1988898686707044353.json、视频生成/图生视频/2026900959795879938.json、视频生成/图生视频/2028672160373415937.json、视频生成/图生视频/1960048260402589698.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/11 个有
- `JWInteger` —— 10/11 个有
- `MultiTalkModelLoader` —— 10/11 个有
- `PreviewAny` —— 10/11 个有
- `WanVideoLoraSelect` —— 10/11 个有
- `WanVideoModelLoader` —— 10/11 个有
- `GetImageSizeAndCount` —— 9/11 个有
- `Int` —— 5/11 个有
- `JWFloat` —— 4/11 个有
- `RH_GetAudioDuration` —— 4/11 个有
- `SimpleMath+` —— 4/11 个有
- `ToInt` —— 4/11 个有
- `easy showAnything` —— 3/11 个有
- `Label (rgthree)` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `Comfly_api_set` —— 1/11 个有
- `Comfly_suno_custom` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有
- `SaveAudio` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
