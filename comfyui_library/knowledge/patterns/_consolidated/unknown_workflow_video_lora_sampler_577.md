---
name: unknown_workflow_video_lora_sampler_577
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9694
common_nodes: [AudioCrop, AudioSeparation, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, StringToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE&InfiniteTalk-控制+参考+对口型_1958086510564298754.json, 平台全量/VACE&MultiTalk-控制+参考+对口型_1942469885530411010.json, 视频生成/图生视频/VACE&InfiniteTalk-首尾帧+对口型_1958191030833201153.json, 视频生成/图生视频/VACE&MultiTalk-首尾帧+对口型_1942474167965126658.json, 视频生成/图生视频/multitalk-wan-双人-index tts_1941378778566389761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_577

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/VACE&InfiniteTalk-控制+参考+对口型_1958086510564298754.json、平台全量/VACE&MultiTalk-控制+参考+对口型_1942469885530411010.json、视频生成/图生视频/VACE&InfiniteTalk-首尾帧+对口型_1958191030833201153.json、视频生成/图生视频/VACE&MultiTalk-首尾帧+对口型_1942474167965126658.json、视频生成/图生视频/multitalk-wan-双人-index tts_1941378778566389761.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `StringToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `Int` —— 4/5 个有
- `WanVideoEnhanceAVideo` —— 4/5 个有
- `WanVideoExperimentalArgs` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `WanVideoVACEEncode` —— 4/5 个有
- `WanVideoVACEModelSelect` —— 4/5 个有
- `WanVideoVACEStartToEndFrame` —— 4/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `DWPreprocessor` —— 2/5 个有
- `IndexTTSRun` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `String Literal` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `WanVideoClipVisionEncode` —— 2/5 个有
- `MaskPreview` —— 1/5 个有
- `SeparateMasks` —— 1/5 个有
- `WanVideoImageToVideoMultiTalk` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
