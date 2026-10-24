---
name: unknown_workflow_video_lora_sampler_471
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.942
common_nodes: [CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json, 视频生成/图生视频/Infinite Talk 双人数字人_1970484627771170817.json, 视频生成/图生视频/爆火的西游记人物唱歌 ， Infinite talk 数字人（循环流不爆显存）除非到了平台的时长限制_1980902275004678145.json, "音频生成/音频生成/MV,音乐达人，高动态音乐数字人_2046930658349555714.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_471

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/高动态口播数字人 InfiniteTalk+IndexTTS2 （Lightx2v+Rcm）_2090261460101459969.json、视频生成/图生视频/Infinite Talk 双人数字人_1970484627771170817.json、视频生成/图生视频/爆火的西游记人物唱歌 ， Infinite talk 数字人（循环流不爆显存）除非到了平台的时长限制_1980902275004678145.json、音频生成/音频生成/MV,音乐达人，高动态音乐数字人_2046930658349555714.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
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
- `AudioCrop` —— 3/4 个有
- `AudioSeparation` —— 3/4 个有
- `Bjornulf_ShowInt` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `easy int` —— 3/4 个有
- `Bjornulf_ShowFloat` —— 1/4 个有
- `ColorMatch` —— 1/4 个有
- `Display Int (rgthree)` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `IndexTTS2Run` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `Pick From Batch (mtb)` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SaveAudio` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
