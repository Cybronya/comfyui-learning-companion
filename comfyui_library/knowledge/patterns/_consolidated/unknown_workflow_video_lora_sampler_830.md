---
name: unknown_workflow_video_lora_sampler_830
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.855
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageFromBatch, ImageResizeKJv2, Int, JjkText, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/视频对口型 声画自用_1992930416395042818.json, 数字人/数字人/视频对口型 infinite talk_1959510782524469249.json, 数字人/数字人/视频对口型，效果完美_1972132760125173761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_830

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频对口型 声画自用_1992930416395042818.json、数字人/数字人/视频对口型 infinite talk_1959510782524469249.json、数字人/数字人/视频对口型，效果完美_1972132760125173761.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/3 个有
- `AILab_MiniCPM_4_V` —— 1/3 个有
- `GroundingDinoModelLoader (segment anything2)` —— 1/3 个有
- `GroundingDinoSAM2Segment (segment anything2)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SAM2ModelLoader (segment anything2)` —— 1/3 个有
- `VHS_VideoInfo` —— 1/3 个有
- `WanVideoVACEModelSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
