---
name: unknown_workflow_video_lora_sampler_186
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8434
common_nodes: [AudioCrop, AudioCropProcessUTK, CLIPVisionLoader, CM_FloatUnaryOperation, CM_IntToFloat, CR Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, HuMoEmbeds, INTConstant, ImageFromBatch+, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, NormalizeAudioLoudness, PrimitiveString, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2031633089117560834.json, 视频生成/图生视频/1999689343231029250.json, 视频生成/图生视频/2048943364548071425.json, 视频生成/图生视频/2049741218380300290.json, 视频生成/图生视频/2053646758080720898.json, 视频生成/图生视频/1980829225919926273.json, 视频生成/图生视频/1973235123128807426.json, 视频生成/图生视频/1991795582006145025.json, 视频生成/图生视频/1995394218111774721.json, 视频生成/图生视频/1956547537161388033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_186

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2031633089117560834.json、视频生成/图生视频/1999689343231029250.json、视频生成/图生视频/2048943364548071425.json、视频生成/图生视频/2049741218380300290.json、视频生成/图生视频/2053646758080720898.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioCropProcessUTK`
- `CLIPVisionLoader`
- `CM_FloatUnaryOperation`
- `CM_IntToFloat`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `HuMoEmbeds`
- `INTConstant`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `NormalizeAudioLoudness`
- `PrimitiveString`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoCombineEmbeds`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 9/10 个有
- `ImageBatch` —— 7/10 个有
- `LazySwitch1way` —— 7/10 个有
- `SoundFlow_Concatenator` —— 7/10 个有
- `easy boolean` —— 7/10 个有
- `ImpactSwitch` —— 6/10 个有
- `easy compare` —— 6/10 个有
- `ControlNextGetPoses` —— 3/10 个有
- `LayerUtility: Seed` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `Primitive integer [Crystools]` —— 3/10 个有
- `RHHiddenNodes` —— 3/10 个有
- `RH_Captioner` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `WanVideoApplyNAG` —— 3/10 个有
- `WanVideoControlEmbeds` —— 3/10 个有
- `WanVideoEncode` —— 3/10 个有
- `WanVideoImageToVideoEncode` —— 3/10 个有
- `WanVideoSLG` —— 3/10 个有
- `WanVideoTextEncodeSingle` —— 3/10 个有
- `WanVideoVACEModelSelect` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `easy clearCacheAll` —— 3/10 个有
- `ttN concat` —— 3/10 个有
- `Anything Everywhere` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 2/10 个有
- `FlashVSRNode` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `SeedVR2BlockSwap` —— 2/10 个有
- `SeedVR2ExtraArgs` —— 2/10 个有
- `SeedVR2GGUF` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `VideoTransitionNode` —— 2/10 个有
- `MuterSwitcher` —— 1/10 个有
- `🎈GroupDetector` —— 1/10 个有
- `🎈StateTransfer` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
