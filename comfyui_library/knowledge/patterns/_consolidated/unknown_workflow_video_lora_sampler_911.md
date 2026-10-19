---
name: unknown_workflow_video_lora_sampler_911
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.652
common_nodes: [Any Switch (rgthree), AudioSeparation, CLIPVisionLoader, CR String To Number, CR Text, DownloadAndLoadWav2VecModel, Fast Groups Muter (rgthree), GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJv2, Int, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SaveAudio, SetNode, SparkTTSClone, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/音频文本驱动生成数字人对口型数字人视频生成支持动物说话视频生成声音克隆视频生成_2011517441985220610.json, 音频生成/音频生成/数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_911

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/音频文本驱动生成数字人对口型数字人视频生成支持动物说话视频生成声音克隆视频生成_2011517441985220610.json、音频生成/音频生成/数字人音频_文本驱动 带音色模仿 支持动物Q版 卡通角色 InfiniteTalk-Wan2.2_1999708121922760705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR String To Number`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `Fast Groups Muter (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SaveAudio`
- `SetNode`
- `SparkTTSClone`
- `Text Multiline`
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
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Integer To String` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `Random Number` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
