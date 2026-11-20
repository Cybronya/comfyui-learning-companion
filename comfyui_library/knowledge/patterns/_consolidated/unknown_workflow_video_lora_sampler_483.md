---
name: unknown_workflow_video_lora_sampler_483
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.699167
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/AI替身术：把武打片的主角换成你 换人方案：Stand-In + VACE组合_1957727910406844417.json, 平台全量/🔥AI易容术：把电影主角换成你！Stand In + ComfyUI完美换人🎬_1957363456569700354.json, 数字人/数字人/wanvideo_Stand-In_高级用法_1956565549708967937.json, 视频生成/图生视频/AI变身术：把主角换成你：Stand-In+VACE组合_1966014870305017857.json, 视频生成/图生视频/AI替身术：把视频的主角换成另外一个人-视频 换人方案：Stand-In + VACE组合_1963979940653842434.json, 视频生成/图生视频/【gen全能视频Si】🔥ai易容术stand-in一键换人_1961411519911280642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_483

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/AI替身术：把武打片的主角换成你 换人方案：Stand-In + VACE组合_1957727910406844417.json、平台全量/🔥AI易容术：把电影主角换成你！Stand In + ComfyUI完美换人🎬_1957363456569700354.json、数字人/数字人/wanvideo_Stand-In_高级用法_1956565549708967937.json、视频生成/图生视频/AI变身术：把主角换成你：Stand-In+VACE组合_1966014870305017857.json、视频生成/图生视频/AI替身术：把视频的主角换成另外一个人-视频 换人方案：Stand-In + VACE组合_1963979940653842434.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FaceOnlyModeSwitch` —— 5/6 个有
- `HfImageToRGB` —— 5/6 个有
- `Label (rgthree)` —— 5/6 个有
- `VideoFramePreprocessor` —— 5/6 个有
- `VideoInputPreprocessor` —— 5/6 个有
- `WanVideoVACEEncode` —— 4/6 个有
- `WanVideoVACEModelSelect` —— 4/6 个有
- `DWPreprocessor` —— 3/6 个有
- `GetImageRangeFromBatch` —— 3/6 个有
- `ImageCombine` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `RepeatImageBatch` —— 3/6 个有
- `AudioSeparation` —— 2/6 个有
- `DownloadAndLoadWav2VecModel` —— 2/6 个有
- `MultiTalkModelLoader` —— 2/6 个有
- `MultiTalkWav2VecEmbeds` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `WanVideoEmptyEmbeds` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `PreViewVideo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
