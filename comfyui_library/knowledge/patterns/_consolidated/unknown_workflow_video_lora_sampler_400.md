---
name: unknown_workflow_video_lora_sampler_400
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9342
common_nodes: [CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json, 视频生成/图生视频/1970484627771170817.json, 视频生成/图生视频/1969431253688721410.json, 视频生成/图生视频/1980902275004678145.json, "音频生成/音频生成/MV,音乐达人，高动态音乐数字人_2046930658349555714.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_400

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json、视频生成/图生视频/1970484627771170817.json、视频生成/图生视频/1969431253688721410.json、视频生成/图生视频/1980902275004678145.json、音频生成/音频生成/MV,音乐达人，高动态音乐数字人_2046930658349555714.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `ToInt`
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
- `AudioCrop` —— 4/5 个有
- `AudioSeparation` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `JWInteger` —— 4/5 个有
- `easy int` —— 4/5 个有
- `Bjornulf_ShowInt` —— 3/5 个有
- `Display Int (rgthree)` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `Bjornulf_ShowFloat` —— 1/5 个有
- `ColorMatch` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `IndexTTS2Run` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `Pick From Batch (mtb)` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `SaveAudio` —— 1/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
