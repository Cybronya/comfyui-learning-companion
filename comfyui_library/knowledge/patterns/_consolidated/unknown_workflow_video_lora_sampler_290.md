---
name: unknown_workflow_video_lora_sampler_290
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.832625
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageConcatMulti, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PainterAV2V, PainterAudioCut, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/脸部参考InfiniteTalk 对口型V2_2022007193763061762.json, 数字人/数字人/（单人脸部参考）InfiniteTalk 视频V2V对口型forWAN_2019689018878857217.json, 数字人/数字人/（脸部参考）InfiniteTalk 视频对口型_2016703138547376130.json, 视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2064514546374631425.json, 视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2075412859504390145.json, 视频生成/图生视频/视频换脸 图生视频+脸部参考替换+InfiniteTalk+视频+数字人对口型_2078010993078263809.json, 音频生成/音频生成/DG_infinite talk 对口型（视频编辑）+脸部参考 （整理T8的）_2016819542332280834.json, 音频生成/音频生成/Digital Avatars Lip-Syncing数字人对口型_2097153340940574722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_290

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/脸部参考InfiniteTalk 对口型V2_2022007193763061762.json、数字人/数字人/（单人脸部参考）InfiniteTalk 视频V2V对口型forWAN_2019689018878857217.json、数字人/数字人/（脸部参考）InfiniteTalk 视频对口型_2016703138547376130.json、视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2064514546374631425.json、视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2075412859504390145.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageConcatMulti`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PainterAV2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `CRTFirstLastFrameSelector` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImageRepeat` —— 1/8 个有
- `Int` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | dpmpp_sde | - | 8 | 100% |
| 重绘幅度 | normal | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，8 个样本，一致性 100%
- 重绘幅度 最常用 normal，8 个样本，一致性 100%
