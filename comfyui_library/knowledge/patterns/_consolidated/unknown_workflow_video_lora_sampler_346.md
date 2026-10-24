---
name: unknown_workflow_video_lora_sampler_346
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.770833
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PainterAV2V, PainterAudioCut, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/Infinite Talk视频对口型_2073309420112662529.json, 视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2064514546374631425.json, 视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2075412859504390145.json, 视频生成/图生视频/视频换脸 图生视频+脸部参考替换+InfiniteTalk+视频+数字人对口型_2078010993078263809.json, 音频生成/音频生成/DG_infinite talk 对口型（视频编辑）+脸部参考 （整理T8的）_2016819542332280834.json, 音频生成/音频生成/Digital Avatars Lip-Syncing数字人对口型_2097153340940574722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_346

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Infinite Talk视频对口型_2073309420112662529.json、视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2064514546374631425.json、视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2075412859504390145.json、视频生成/图生视频/视频换脸 图生视频+脸部参考替换+InfiniteTalk+视频+数字人对口型_2078010993078263809.json、音频生成/音频生成/DG_infinite talk 对口型（视频编辑）+脸部参考 （整理T8的）_2016819542332280834.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
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

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ColorMatch` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | dpmpp_sde | - | 6 | 83% |
| 重绘幅度 | normal | - | 6 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，6 个样本，一致性 83%
- 重绘幅度 最常用 normal，6 个样本，一致性 83%
