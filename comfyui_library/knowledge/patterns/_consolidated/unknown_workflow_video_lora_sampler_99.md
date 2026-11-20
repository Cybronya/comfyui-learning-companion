---
name: unknown_workflow_video_lora_sampler_99
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.606625
common_nodes: [AudioCrop, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/AI代码侠土豆-情感表达高动效-单张图生成数字人_2007331723943612417.json, 数字人/数字人/AI代码侠土豆-超自然数字人-单张图生成数字人_2006237787544100866.json, 数字人/数字人/InfiniteTalk-GGUF.自用_1961661222749978625.json, 数字人/数字人/InfiniteTalk数字人-图片单人版_1963995655213563906.json, 数字人/数字人/InfiniteTalk数字人-基础视频生成_1997693369113579522.json, 数字人/数字人/InfiniteTalk数字人（AAA）_1962351398337888258.json, 数字人/数字人/单张图生成数字人-自然版_2012138583209021442.json, 数字人/数字人/单张图生成数字人-高情绪高动态_2012139784826789890.json, 数字人/数字人/情感表达-图生成数字人_2008995730203090945.json, 数字人/数字人/西洲 InfiniteTalk数字人长视频（唱歌-对口型）_1969409119033716738.json, 数字人/数字人/语音克隆、双人版wanvideo_infinitetalk_工作流_1960735901263564801.json, 数字人/数字人/超自然数字人-图生成数字人_2009002607687241730.json, 视频生成/图生视频/InfiniteTalk数字人-基础视频生成_1975057390238306306.json, 视频生成/图生视频/infiniteTalk（音色克隆+音频生成）_1970143422839463937.json, 视频生成/文生视频/图片唱歌_2007669635780448258.json, 音频生成/音频生成/infiniteTalk（音色克隆+音频生成）_1970169527449382913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_99

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（数字人/数字人/AI代码侠土豆-情感表达高动效-单张图生成数字人_2007331723943612417.json、数字人/数字人/AI代码侠土豆-超自然数字人-单张图生成数字人_2006237787544100866.json、数字人/数字人/InfiniteTalk-GGUF.自用_1961661222749978625.json、数字人/数字人/InfiniteTalk数字人-图片单人版_1963995655213563906.json、数字人/数字人/InfiniteTalk数字人-基础视频生成_1997693369113579522.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 16 个 workflow 都包含：
- `AudioCrop`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/16 个有
- `SetNode` —— 14/16 个有
- `WanVideoTorchCompileSettings` —— 13/16 个有
- `WanVideoTextEncodeCached` —— 12/16 个有
- `Audio Duration (mtb)` —— 10/16 个有
- `SimpleMath+` —— 10/16 个有
- `AudioSeparation` —— 9/16 个有
- `LayerUtility: PurgeVRAM V2` —— 9/16 个有
- `Text` —— 8/16 个有
- `QZ_ResolutionPreset` —— 7/16 个有
- `CR Text` —— 5/16 个有
- `GetImageSizeAndCount` —— 5/16 个有
- `PreviewAudio` —— 5/16 个有
- `LoadWanVideoT5TextEncoder` —— 4/16 个有
- `WanVideoTextEncode` —— 4/16 个有
- `INTConstant` —— 3/16 个有
- `ImageFromBatch+` —— 3/16 个有
- `PreviewAny` —— 3/16 个有
- `ImpactSwitch` —— 2/16 个有
- `IndexTTS2Run` —— 2/16 个有
- `JWInteger` —— 2/16 个有
- `MegaTTS3` —— 2/16 个有
- `PrimitiveInt` —— 2/16 个有
- `RH_Translator` —— 2/16 个有
- `IndexTTSNode` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
