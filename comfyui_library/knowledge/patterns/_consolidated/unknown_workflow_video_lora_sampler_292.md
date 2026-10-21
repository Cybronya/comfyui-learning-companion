---
name: unknown_workflow_video_lora_sampler_292
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.808429
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageFromBatch+, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple]
problems: []
missing: []
members: [视频生成/图生视频/1975430744082395137.json, 视频生成/图生视频/1975181120914460673.json, 视频生成/图生视频/1989714955807150082.json, 视频生成/图生视频/1989717889194315777.json, 视频生成/图生视频/1990279000503275522.json, 视频生成/图生视频/2029535256906309633.json, 视频生成/文生视频/多重参考生视频（WAN_BindWeave+TTS+MULTITALK）_1990350029464498177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_292

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1975430744082395137.json、视频生成/图生视频/1975181120914460673.json、视频生成/图生视频/1989714955807150082.json、视频生成/图生视频/1989717889194315777.json、视频生成/图生视频/1990279000503275522.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSGenerateSimple`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `CLIPLoader` —— 5/7 个有
- `CR Prompt Text` —— 5/7 个有
- `DrawMaskOnImage` —— 5/7 个有
- `ImageBatchMulti` —— 5/7 个有
- `InvertMask` —— 5/7 个有
- `MaskBatchMulti` —— 5/7 个有
- `MathExpression|pysssss` —— 5/7 个有
- `PreviewAny` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `SaveAudio` —— 5/7 个有
- `SolidMask` —— 5/7 个有
- `TextImageEncodeQwenVL` —— 5/7 个有
- `WanVideoAddBindweaveEmbeds` —— 5/7 个有
- `WanVideoEncodeLatentBatch` —— 5/7 个有
- `WanVideoTextEncodeCached` —— 5/7 个有
- `easy imageRemBg` —— 5/7 个有
- `LayerUtility: PurgeVRAM` —— 4/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `ImageRemoveBackground+` —— 3/7 个有
- `Int` —— 3/7 个有
- `PrimitiveFloat` —— 3/7 个有
- `TextInput_` —— 3/7 个有
- `TransparentBGSession+` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `CreateCFGScheduleFloatList` —— 2/7 个有
- `Float` —— 2/7 个有
- `INTConstant` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `ImagePadKJ` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `MaskPreview+` —— 2/7 个有
- `Primitive integer [Crystools]` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `WanVideoScheduler` —— 2/7 个有
- `WanVideoSigmaToStep` —— 2/7 个有
- `WanVideoContextOptions` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
