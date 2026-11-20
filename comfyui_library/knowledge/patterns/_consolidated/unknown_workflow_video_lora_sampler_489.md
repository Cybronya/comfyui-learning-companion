---
name: unknown_workflow_video_lora_sampler_489
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8386
common_nodes: [AudioCrop, AudioEncoderEncode, AudioEncoderLoader, DWPreprocessor, Display Int (rgthree), INTConstant, ImageConcanate, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, PreviewImage, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddS2VEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/S2V+控制+Framepack+ContextWindow长视频工作流_1961914192292986881.json, 视频生成/图生视频/wan2.2  S2V+Controlnet完美声音生成视频  整合版_1962093681132113922.json, 视频生成/图生视频/【gen全能视频Si】s2v数字人+动作控制长视频工作流_1963163594022170625.json, 视频生成/图生视频/图片+音频+参考动作视频=mtv(无限时长音乐数字人）_1962043447869902849.json, 视频生成/图生视频/声音+图片+视频动作，S2V+控制+Framepack+ContextWindow长视频工作流_1964517302806921217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_489

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/S2V+控制+Framepack+ContextWindow长视频工作流_1961914192292986881.json、视频生成/图生视频/wan2.2  S2V+Controlnet完美声音生成视频  整合版_1962093681132113922.json、视频生成/图生视频/【gen全能视频Si】s2v数字人+动作控制长视频工作流_1963163594022170625.json、视频生成/图生视频/图片+音频+参考动作视频=mtv(无限时长音乐数字人）_1962043447869902849.json、视频生成/图生视频/声音+图片+视频动作，S2V+控制+Framepack+ContextWindow长视频工作流_1964517302806921217.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `DWPreprocessor`
- `Display Int (rgthree)`
- `INTConstant`
- `ImageConcanate`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `PreviewImage`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `ToInt`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddS2VEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 4/5 个有
- `GIMMVFI_interpolate` —— 4/5 个有
- `ImageFlip+` —— 4/5 个有
- `DepthAnythingPreprocessor` —— 1/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `WanVideoLoraSelect` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
