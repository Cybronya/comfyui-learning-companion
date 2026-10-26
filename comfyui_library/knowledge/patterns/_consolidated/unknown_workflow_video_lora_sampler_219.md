---
name: unknown_workflow_video_lora_sampler_219
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7738
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, NormalizeAudioLoudness, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/HuMo+InfiniteTalk单人参考数字人口型稳定修正版V3_1968594582734811138.json, 视频生成/图生视频/HuMo单人参考数字人稳定修正版V3_1966929028462600194.json, 视频生成/图生视频/HuMo双图参考数字人V1_1966942457197891585.json, 视频生成/图生视频/HuMo双图参考数字人稳定修正版V3_1968587211782410241.json, 视频生成/图生视频/人物一致口型一致V3版HuMo+InfiniteTalk_1975795002448195586.json, 视频生成/图生视频/祝福视频测试 HUMO_2037863999005532162.json, 视频生成/文生视频/HuMo音频驱动文生数字人V1_1966946187645476866.json, 视频生成/文生视频/HuMo音频驱动文生数字人稳定修正版V3_1968587379978186753.json, 视频生成/文生视频/humo双图参考_1968180863945027585.json, 音频生成/音频生成/数字人HuMo单人参考数字人V1_1967105592944943105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_219

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/HuMo+InfiniteTalk单人参考数字人口型稳定修正版V3_1968594582734811138.json、视频生成/图生视频/HuMo单人参考数字人稳定修正版V3_1966929028462600194.json、视频生成/图生视频/HuMo双图参考数字人V1_1966942457197891585.json、视频生成/图生视频/HuMo双图参考数字人稳定修正版V3_1968587211782410241.json、视频生成/图生视频/人物一致口型一致V3版HuMo+InfiniteTalk_1975795002448195586.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
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
- `CR Prompt Text` —— 9/10 个有
- `GetNode` —— 9/10 个有
- `ImageResizeKJv2` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `ImageBatchMulti` —— 7/10 个有
- `ImageConcatMulti` —— 7/10 个有
- `RMBG` —— 6/10 个有
- `INTConstant` —— 5/10 个有
- `JWInteger` —— 4/10 个有
- `MultiTalkModelLoader` —— 3/10 个有
- `MultiTalkWav2VecEmbeds` —— 3/10 个有
- `WanVideoCombineEmbeds` —— 3/10 个有
- `WanVideoImageToVideoMultiTalk` —— 3/10 个有
- `Wav2VecModelLoader` —— 3/10 个有
- `Int` —— 2/10 个有
- `PDIMAGE_LongerSize` —— 2/10 个有
- `WanVideoTorchCompileSettings` —— 2/10 个有
- `DF_Int_to_Float` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
