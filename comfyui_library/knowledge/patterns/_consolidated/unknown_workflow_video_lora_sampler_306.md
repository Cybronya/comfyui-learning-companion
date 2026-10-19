---
name: unknown_workflow_video_lora_sampler_306
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.932143
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958754013288296450.json, 视频生成/图生视频/1957818036982050817.json, 视频生成/图生视频/1936573145107304450.json, 视频生成/图生视频/1936694256662908929.json, 视频生成/图生视频/1936454016199200770.json, 视频生成/图生视频/1939669350049878017.json, 视频生成/图生视频/1948575951367090178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_306

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1958754013288296450.json、视频生成/图生视频/1957818036982050817.json、视频生成/图生视频/1936573145107304450.json、视频生成/图生视频/1936694256662908929.json、视频生成/图生视频/1936454016199200770.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 6/7 个有
- `WanVideoEncode` —— 6/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/7 个有
- `WanVideoUni3C_embeds` —— 6/7 个有
- `AudioCrop` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `Text Multiline` —— 5/7 个有
- `WanVideoContextOptions` —— 5/7 个有
- `WanVideoImageToVideoEncode` —— 5/7 个有
- `MathExpression|pysssss` —— 4/7 个有
- `RH_Captioner` —— 4/7 个有
- `Text Concatenate` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `INTConstant` —— 3/7 个有
- `Int` —— 3/7 个有
- `Note Plus (mtb)` —— 3/7 个有
- `VHS_DuplicateImages` —— 3/7 个有
- `Audio Duration (mtb)` —— 2/7 个有
- `CreateCFGScheduleFloatList` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `Primitive integer [Crystools]` —— 2/7 个有
- `WanVideoImageToVideoMultiTalk` —— 2/7 个有
- `WanVideoSLG` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/7 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `Image To Mask` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `JWIntegerToString` —— 1/7 个有
- `MaskPreview+` —— 1/7 个有
- `MaskToImage` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `SAMLoader` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `Separate Mask Components` —— 1/7 个有
- `SeparateMasks` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
