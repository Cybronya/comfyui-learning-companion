---
name: unknown_workflow_video_lora_sampler_969
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.699
common_nodes: [Bounded Image Crop, Bounded Image Crop with Mask, DWPreprocessor, GetImageSizeAndCount, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), INTConstant, ImageResizeKJv2, LoadImage, LoadLynxResampler, LynxEncodeFaceIP, PreviewImage, SAMModelLoader (segment anything), SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddLynxEmbeds, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/AI换人术：把你变成舞王，Lynx+ComfyUI工作流实战_1976479645115785218.json, 视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_969

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/AI换人术：把你变成舞王，Lynx+ComfyUI工作流实战_1976479645115785218.json、视频生成/文生视频/Wan_T2V + Lynx + VACE IntTalk Video 课程对应工作流 在线运行版_1978110576863928322.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Bounded Image Crop`
- `Bounded Image Crop with Mask`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadLynxResampler`
- `LynxEncodeFaceIP`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Bjornulf_ShowInt` —— 1/2 个有
- `DownloadAndLoadWav2VecModel` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LynxInsightFaceCrop` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `Mix Color By Mask` —— 1/2 个有
- `MultiTalkModelLoader` —— 1/2 个有
- `MultiTalkWav2VecEmbeds` —— 1/2 个有
- `StringConstantMultiline` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
