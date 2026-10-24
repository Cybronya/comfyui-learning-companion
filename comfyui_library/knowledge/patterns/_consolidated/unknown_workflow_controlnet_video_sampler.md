---
name: unknown_workflow_controlnet_video_sampler
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.937833
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX+Multitalk 数字人_1945004776141807618.json, 视频生成/图生视频/MultiTalk 单人+运镜_1936573145107304450.json, 视频生成/图生视频/MultiTalk 唱歌数字人｜KJ加速版_1936694256662908929.json, 视频生成/图生视频/MultiTalk-动态数字人天花板 单图KJ版-StarAI_1936454016199200770.json, 视频生成/图生视频/Multitalk万能数字人- 真人-卡通- 动物--生成超长视频_1939669350049878017.json, 视频生成/图生视频/Multitalk双人对话--生成超长视频_1948575951367090178.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_sampler

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/FusionX+Multitalk 数字人_1945004776141807618.json、视频生成/图生视频/MultiTalk 单人+运镜_1936573145107304450.json、视频生成/图生视频/MultiTalk 唱歌数字人｜KJ加速版_1936694256662908929.json、视频生成/图生视频/MultiTalk-动态数字人天花板 单图KJ版-StarAI_1936454016199200770.json、视频生成/图生视频/Multitalk万能数字人- 真人-卡通- 动物--生成超长视频_1939669350049878017.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 5/6 个有
- `RH_Captioner` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `Text Concatenate` —— 4/6 个有
- `Text Multiline` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `INTConstant` —— 3/6 个有
- `Int` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `Note Plus (mtb)` —— 3/6 个有
- `VHS_DuplicateImages` —— 3/6 个有
- `Audio Duration (mtb)` —— 2/6 个有
- `CreateCFGScheduleFloatList` —— 2/6 个有
- `LayerUtility: PurgeVRAM` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `Primitive integer [Crystools]` —— 2/6 个有
- `SaveAudio` —— 2/6 个有
- `WanVideoSLG` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `DF_Integer` —— 1/6 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/6 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `Image To Mask` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `IndexTTSNode` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `MaskToImage` —— 1/6 个有
- `RH_Prompter` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `SAMLoader` —— 1/6 个有
- `Separate Mask Components` —— 1/6 个有
- `SeparateMasks` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有
- `ttN concat` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
