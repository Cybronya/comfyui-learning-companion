---
name: unknown_workflow_video_lora_sampler_151
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.848286
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSamplerAdvanced, LoadAudio, LoraLoaderModelOnly, ModelPatchLoader, PainterAV2V, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/V2V  一键视频换脸     人物口型同步_2016833674750201858.json, 平台全量/（脸部参考）InfiniteTalk 视频V2V对口型V3_2015752297149632514.json, 平台全量/（视频换脸+对口型）InfiniteTalk视频V2V 林耀_2016710127927169026.json, 数字人/数字人/03-10-13-WAN2.1-数字人-InfiniteTalk-视频AV2V对口型-脸部参考_2019272890222383105.json, 数字人/数字人/InfiniteTalk 视频V2V对口型-轻度换脸OR增强一致性_2018621192965464066.json, 数字人/数字人/【2月】视频唇型同步+一致性加强，更好的支持人物动态_2017966613697404930.json, 数字人/数字人/脸部参考InfiniteTalk 对口型V2_2022007193763061762.json, 数字人/数字人/（单人脸部参考）InfiniteTalk 视频V2V对口型forWAN_2019689018878857217.json, 数字人/数字人/（脸部参考）InfiniteTalk 视频对口型_2016703138547376130.json, 视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2064514546374631425.json, 视频生成/图生视频/图生视频 脸部参考 InfiniteTalk+视频 数字人对口型_2075412859504390145.json, 视频生成/图生视频/视频换脸 图生视频+脸部参考替换+InfiniteTalk+视频+数字人对口型_2078010993078263809.json, 音频生成/音频生成/DG_infinite talk 对口型（视频编辑）+脸部参考 （整理T8的）_2016819542332280834.json, 音频生成/音频生成/Digital Avatars Lip-Syncing数字人对口型_2097153340940574722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_151

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/V2V  一键视频换脸     人物口型同步_2016833674750201858.json、平台全量/（脸部参考）InfiniteTalk 视频V2V对口型V3_2015752297149632514.json、平台全量/（视频换脸+对口型）InfiniteTalk视频V2V 林耀_2016710127927169026.json、数字人/数字人/03-10-13-WAN2.1-数字人-InfiniteTalk-视频AV2V对口型-脸部参考_2019272890222383105.json、数字人/数字人/InfiniteTalk 视频V2V对口型-轻度换脸OR增强一致性_2018621192965464066.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PainterAV2V`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 13/14 个有
- `PainterAudioCut` —— 13/14 个有
- `easy cleanGpuUsed` —— 13/14 个有
- `ImageConcatMulti` —— 11/14 个有
- `MathExpression|pysssss` —— 6/14 个有
- `easy showAnything` —— 6/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/14 个有
- `GetNode` —— 2/14 个有
- `ImageFromBatch+` —— 2/14 个有
- `SetNode` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `CRTFirstLastFrameSelector` —— 1/14 个有
- `ImageFromBatch` —— 1/14 个有
- `ImageRepeat` —— 1/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `Int` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 4 | 14 | 92% |
| 采样算法 | 1 | 1 - 1 | 14 | 100% |
| 调度器 | dpmpp_sde | - | 14 | 100% |
| 重绘幅度 | normal | - | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 4，14 个样本，取值集中（一致性 92%）
- 采样算法 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，14 个样本，一致性 100%
- 重绘幅度 最常用 normal，14 个样本，一致性 100%
