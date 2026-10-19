---
name: unknown_workflow_video_lora_sampler_224
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.749889
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, JWInteger, JWIntegerToString, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveFloat, PrimitiveInt, SimpleMath+, TextInput_, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1936701399797501953.json, 视频生成/图生视频/1948784661829492737.json, 视频生成/图生视频/1998945387329282050.json, 视频生成/图生视频/1998778583533412354.json, 视频生成/图生视频/1948782335715094529.json, 视频生成/图生视频/1986856996743876610.json, 视频生成/图生视频/1955533790640836610.json, 视频生成/图生视频/1936815365949149186.json, 视频生成/图生视频/1955521619805421569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_224

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1936701399797501953.json、视频生成/图生视频/1948784661829492737.json、视频生成/图生视频/1998945387329282050.json、视频生成/图生视频/1998778583533412354.json、视频生成/图生视频/1948782335715094529.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `JWIntegerToString`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SimpleMath+`
- `TextInput_`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 8/9 个有
- `ImageResizeKJ` —— 6/9 个有
- `VHS_LoadVideo` —— 6/9 个有
- `WanVideoEncode` —— 6/9 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/9 个有
- `WanVideoUni3C_embeds` —— 6/9 个有
- `AddLabel` —— 2/9 个有
- `CreateCFGScheduleFloatList` —— 2/9 个有
- `EmptyImage` —— 2/9 个有
- `GetImageSizeAndCount` —— 2/9 个有
- `ImageConcatMulti` —— 2/9 个有
- `WanVideoSLG` —— 2/9 个有
- `WanVideoSetBlockSwap` —— 2/9 个有
- `WanVideoSetLoRAs` —— 2/9 个有
- `ColorMatch` —— 1/9 个有
- `FloatToSigmas` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `StringToFloatList` —— 1/9 个有
- `WanVideoEnhanceAVideo` —— 1/9 个有
- `WanVideoExperimentalArgs` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
