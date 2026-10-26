---
name: unknown_workflow_video_lora_sampler_591
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.67925
common_nodes: [CreateCFGScheduleFloatList, GetNode, HuMoEmbeds, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/wanvideo_HuMo_图片+音频生成视频_1967466923598417921.json, 视频生成/图生视频/wanvideo_HuMo_多参考图生成视频_1967487607431159809.json, 视频生成/图生视频/👽HuMo单人数字人参考+音频👽_1969237169846034433.json, 视频生成/文生视频/wanvideo_HuMo_音频生成视频_1967497065762840577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_591

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wanvideo_HuMo_图片+音频生成视频_1967466923598417921.json、视频生成/图生视频/wanvideo_HuMo_多参考图生成视频_1967487607431159809.json、视频生成/图生视频/👽HuMo单人数字人参考+音频👽_1969237169846034433.json、视频生成/文生视频/wanvideo_HuMo_音频生成视频_1967497065762840577.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetNode`
- `HuMoEmbeds`
- `LoadAudio`
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
- `INTConstant` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `WanVideoContextOptions` —— 2/4 个有
- `Audio Duration (mtb)` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
