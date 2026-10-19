---
name: unknown_workflow_video_lora_sampler_220
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.869
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1990595971572785153.json, 视频生成/图生视频/1990339469129732098.json, 视频生成/图生视频/2037816256153264129.json, 视频生成/图生视频/1957825819450208257.json, 视频生成/图生视频/1988918406697070593.json, 视频生成/图生视频/2026180704601645057.json, 视频生成/文生视频/对口型数字人Infinite talk_2013508435370840066.json, 音频生成/音频生成/对口型数字人Infinite+Talk_1977882176555470849.json, 音频生成/音频生成/数字人对口型数字人最新Infinite Talk_1975402889982119938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_220

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1990595971572785153.json、视频生成/图生视频/1990339469129732098.json、视频生成/图生视频/2037816256153264129.json、视频生成/图生视频/1957825819450208257.json、视频生成/图生视频/1988918406697070593.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 7/9 个有
- `WanVideoBlockSwap` —— 7/9 个有
- `GetImageSizeAndCount` —— 5/9 个有
- `PreviewAny` —— 5/9 个有
- `JWFloat` —— 4/9 个有
- `MathExpression|pysssss` —— 4/9 个有
- `Frames Slice` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `SoundFlow_GetLength` —— 2/9 个有
- `AudioToFPS` —— 1/9 个有
- `Bjornulf_ShowInt` —— 1/9 个有
- `Int` —— 1/9 个有
- `LoadLynxResampler` —— 1/9 个有
- `LynxEncodeFaceIP` —— 1/9 个有
- `LynxInsightFaceCrop` —— 1/9 个有
- `WanVideoAddLynxEmbeds` —— 1/9 个有
- `WanVideoExtraModelSelect` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
