---
name: unknown_workflow_video_lora_sampler_458
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8136
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, GetImageSizeAndCount, ImageBatch, ImageFromBatch, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SimpleCalculatorKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/03-10-11-WAN2.1-数字人-InfiniteTalk-官方循环无限时长-单人_2019197247455498241.json, 视频生成/图生视频/新Infinite Talk无限时长极速版数字人 无重复动作_2019270368963338242.json, 视频生成/图生视频/（官方版-循环）Infinite Talk动作列表无限时长加速版单人数字人V1_2018734533960540162.json, 视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1 林耀2.6_2019704865835982849.json, 视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1_2018749675796434945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_458

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/03-10-11-WAN2.1-数字人-InfiniteTalk-官方循环无限时长-单人_2019197247455498241.json、视频生成/图生视频/新Infinite Talk无限时长极速版数字人 无重复动作_2019270368963338242.json、视频生成/图生视频/（官方版-循环）Infinite Talk动作列表无限时长加速版单人数字人V1_2018734533960540162.json、视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1 林耀2.6_2019704865835982849.json、视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1_2018749675796434945.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `GetImageSizeAndCount`
- `ImageBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JWFloat` —— 4/5 个有
- `JWInteger` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `easy promptLine` —— 3/5 个有
- `AudioConcat` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `ShowAnything|Mie` —— 2/5 个有
- `AudioCrop` —— 1/5 个有
- `AudioSeparation` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
