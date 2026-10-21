---
name: unknown_workflow_video_lora_sampler_301
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.805857
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, GetNode, HuMoEmbeds, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/1968594582734811138.json, 视频生成/图生视频/1966929028462600194.json, 视频生成/图生视频/1966942457197891585.json, 视频生成/图生视频/1968587211782410241.json, 视频生成/图生视频/1975795002448195586.json, 视频生成/图生视频/2037863999005532162.json, 视频生成/图生视频/1969237169846034433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_301

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1968594582734811138.json、视频生成/图生视频/1966929028462600194.json、视频生成/图生视频/1966942457197891585.json、视频生成/图生视频/1968587211782410241.json、视频生成/图生视频/1975795002448195586.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `HuMoEmbeds`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `NormalizeAudioLoudness`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `RMBG` —— 5/7 个有
- `JWInteger` —— 3/7 个有
- `MultiTalkModelLoader` —— 3/7 个有
- `MultiTalkWav2VecEmbeds` —— 3/7 个有
- `WanVideoCombineEmbeds` —— 3/7 个有
- `WanVideoImageToVideoMultiTalk` —— 3/7 个有
- `Wav2VecModelLoader` —— 3/7 个有
- `INTConstant` —— 2/7 个有
- `PDIMAGE_LongerSize` —— 2/7 个有
- `ImpactInt` —— 1/7 个有
- `Int` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `easy imageRemBg` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
