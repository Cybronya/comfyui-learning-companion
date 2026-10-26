---
name: unknown_workflow_video_lora_sampler_283
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.94525
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk-超长时长数字人_1958367702521954306.json, 数字人/数字人/Infinitetalk_单人图片对口型_1961266591587614722.json, 数字人/数字人/Infinitetalk单人对口型数字人_1958118629235707906.json, 数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json, 数字人/数字人/LLM+MultiTalk+IndexTTS数字人_1942407637285679105.json, 视频生成/图生视频/InfiniteTalk 数字人 图生视频 视频配音_1998698671518666753.json, 视频生成/图生视频/InfiniteTalk图生数字人单人-B站UP主@好奇漫步_1982650082937978882.json, 视频生成/图生视频/InfiniteTalk图生数字人双人-B站UP主@好奇漫步_1982712177004027905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_283

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Infinitetalk-超长时长数字人_1958367702521954306.json、数字人/数字人/Infinitetalk_单人图片对口型_1961266591587614722.json、数字人/数字人/Infinitetalk单人对口型数字人_1958118629235707906.json、数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json、数字人/数字人/LLM+MultiTalk+IndexTTS数字人_1942407637285679105.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `WanVideoImageToVideoMultiTalk` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `Audio Duration (mtb)` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Int` —— 4/8 个有
- `ToInt` —— 4/8 个有
- `PreviewAudio` —— 3/8 个有
- `String Literal` —— 3/8 个有
- `IndexTTSRun` —— 2/8 个有
- `LLMLoader` —— 2/8 个有
- `LLMSampler` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `ShowText` —— 2/8 个有
- `ttN int` —— 2/8 个有
- `AudioCombine` —— 1/8 个有
- `CR Integer To String` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `SaveAudio` —— 1/8 个有
- `WanVideoImageToVideoEncode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
