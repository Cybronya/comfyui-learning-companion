---
name: unknown_workflow_lora_sampler_clip_71
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.822429
common_nodes: [Audio Duration (mtb), AudioEncoderEncode, AudioEncoderLoader, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageBatch, ImageFromBatch, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart]
problems: []
missing: []
members: [视频生成/图生视频/官方循环-infinitetalk_2019285651199369217.json, 视频生成/图生视频/新Infinite Talk无限时长极速版数字人 无重复动作_2019270368963338242.json, 视频生成/图生视频/（官方版-循环）Infinite Talk动作列表无限时长加速版单人数字人V1_2018734533960540162.json, 视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1 林耀2.6_2019704865835982849.json, 视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1_2018749675796434945.json, 视频生成/文生视频/单人InfiniteTalk无限时长原生循环_2018256491320451073.json, 视频生成/文生视频/双人InfiniteTalk无限时长原生循环_2018267797146570753.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/官方循环-infinitetalk_2019285651199369217.json、视频生成/图生视频/新Infinite Talk无限时长极速版数字人 无重复动作_2019270368963338242.json、视频生成/图生视频/（官方版-循环）Infinite Talk动作列表无限时长加速版单人数字人V1_2018734533960540162.json、视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1 林耀2.6_2019704865835982849.json、视频生成/图生视频/（官方版-循环）Infinite Talk无限时长加速版双人数字人V1_2018749675796434945.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `SimpleCalculatorKJ` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `AudioConcat` —— 5/7 个有
- `TrimAudioDuration` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `JWInteger` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `ModelPatchTorchSettings` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `JWFloat` —— 3/7 个有
- `MathExpression|pysssss` —— 3/7 个有
- `PreviewAudio` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `AudioCrop` —— 2/7 个有
- `easy promptLine` —— 2/7 个有
- `AudioSeparation` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `ShowAnything|Mie` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
