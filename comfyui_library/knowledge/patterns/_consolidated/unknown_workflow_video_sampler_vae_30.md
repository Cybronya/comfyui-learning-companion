---
name: unknown_workflow_video_sampler_vae_30
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.945917
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958754013288296450.json, 视频生成/图生视频/1957818036982050817.json, 视频生成/图生视频/1957827307850530818.json, 视频生成/图生视频/1957977430084481025.json, 视频生成/图生视频/2070420975967100929.json, 视频生成/图生视频/1969944110868164610.json, 视频生成/图生视频/1958082253886803970.json, 视频生成/图生视频/1936573145107304450.json, 视频生成/图生视频/1936694256662908929.json, 视频生成/图生视频/1936454016199200770.json, 视频生成/图生视频/1939669350049878017.json, 视频生成/图生视频/1948575951367090178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1958754013288296450.json、视频生成/图生视频/1957818036982050817.json、视频生成/图生视频/1957827307850530818.json、视频生成/图生视频/1957977430084481025.json、视频生成/图生视频/2070420975967100929.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 11/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `LoadImage` —— 10/12 个有
- `WanVideoTorchCompileSettings` —— 10/12 个有
- `AudioCrop` —— 9/12 个有
- `VHS_LoadVideo` —— 7/12 个有
- `WanVideoImageToVideoMultiTalk` —— 7/12 个有
- `WanVideoEncode` —— 6/12 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/12 个有
- `WanVideoUni3C_embeds` —— 6/12 个有
- `INTConstant` —— 5/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/12 个有
- `Text Multiline` —— 5/12 个有
- `WanVideoContextOptions` —— 5/12 个有
- `WanVideoImageToVideoEncode` —— 5/12 个有
- `MathExpression|pysssss` —— 4/12 个有
- `RH_Captioner` —— 4/12 个有
- `Text Concatenate` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `Int` —— 3/12 个有
- `Note Plus (mtb)` —— 3/12 个有
- `VHS_DuplicateImages` —— 3/12 个有
- `Audio Duration (mtb)` —— 2/12 个有
- `CreateCFGScheduleFloatList` —— 2/12 个有
- `LayerUtility: PurgeVRAM` —— 2/12 个有
- `PreviewAudio` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `Primitive integer [Crystools]` —— 2/12 个有
- `PrimitiveInt` —— 2/12 个有
- `WanVideoSLG` —— 2/12 个有
- `easy anythingIndexSwitch` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `GetImageSizeAndCount` —— 1/12 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/12 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/12 个有
- `GrowMaskWithBlur` —— 1/12 个有
- `Image To Mask` —— 1/12 个有
- `ImpactSwitch` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `JWIntegerToString` —— 1/12 个有
- `MaskPreview+` —— 1/12 个有
- `MaskToImage` —— 1/12 个有
- `SAMLoader` —— 1/12 个有
- `SaveAudio` —— 1/12 个有
- `Separate Mask Components` —— 1/12 个有
- `SeparateMasks` —— 1/12 个有
- `WanVideoLoraSelectMulti` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy clearCacheAll` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
