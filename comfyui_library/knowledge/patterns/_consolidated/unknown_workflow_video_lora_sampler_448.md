---
name: unknown_workflow_video_lora_sampler_448
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7228
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/文生视频/HuMo音频驱动文生数字人V1_1966946187645476866.json, 视频生成/文生视频/HuMo音频驱动文生数字人稳定修正版V3_1968587379978186753.json, 视频生成/文生视频/humo双图参考_1968180863945027585.json, 视频生成/文生视频/wanvideo_HuMo_音频生成视频_1967497065762840577.json, 音频生成/音频生成/数字人HuMo单人参考数字人V1_1967105592944943105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_448

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/HuMo音频驱动文生数字人V1_1966946187645476866.json、视频生成/文生视频/HuMo音频驱动文生数字人稳定修正版V3_1968587379978186753.json、视频生成/文生视频/humo双图参考_1968180863945027585.json、视频生成/文生视频/wanvideo_HuMo_音频生成视频_1967497065762840577.json、音频生成/音频生成/数字人HuMo单人参考数字人V1_1967105592944943105.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
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
- `GetNode` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `DF_Int_to_Float` —— 1/5 个有
- `Int` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `WanVideoContextOptions` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
