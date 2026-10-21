---
name: unknown_workflow_video_sampler_clip_21
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.933765
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ColorMatch, GetImageSizeAndCount, ImageFromBatch, ImageResizeKJv2, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MathExpression|pysssss, ModelPatchLoader, ModelSamplingSD3, PainterAI2V, PainterAudioCut, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2021116257344430081.json, 视频生成/图生视频/2015752366074634241.json, 视频生成/图生视频/2016752673365696514.json, 视频生成/图生视频/2033541040463941633.json, 视频生成/图生视频/2042479951521259521.json, 视频生成/图生视频/2073309220157607937.json, 视频生成/图生视频/2016709781737709569.json, 视频生成/图生视频/2020750694147432450.json, 视频生成/图生视频/2019071015162224642.json, 视频生成/图生视频/2034894867540742145.json, 视频生成/图生视频/2042659956331122690.json, 视频生成/图生视频/2017835237677469697.json, 视频生成/图生视频/2016520007626268673.json, 视频生成/图生视频/2027630721145249794.json, 视频生成/图生视频/2016877597203894274.json, 音频生成/音频生成/Infinite+Talk首尾帧数字人_2021412401467367425.json, "音频生成/音频生成/首尾帧对口型数字人,Qwen3TTS,InfiniTetalk_2019627610392760322.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2021116257344430081.json、视频生成/图生视频/2015752366074634241.json、视频生成/图生视频/2016752673365696514.json、视频生成/图生视频/2033541040463941633.json、视频生成/图生视频/2042479951521259521.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 17 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `ModelSamplingSD3`
- `PainterAI2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 16/17 个有
- `PreviewAny` —— 16/17 个有
- `ImageConcanate` —— 15/17 个有
- `LoraLoaderModelOnly` —— 15/17 个有
- `JWInteger` —— 14/17 个有
- `Qwen3TTSModelLoader` —— 13/17 个有
- `Qwen3TTSVoiceClone` —— 13/17 个有
- `SaveAudioMP3` —— 13/17 个有
- `PrimitiveStringMultiline` —— 10/17 个有
- `Audio Duration (mtb)` —— 2/17 个有
- `AudioInfo` —— 2/17 个有
- `AudioSeparation` —— 2/17 个有
- `JjkText` —— 2/17 个有
- `ModelPatchTorchSettings` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `ShowAnything|Mie` —— 2/17 个有
- `easy showAnything` —— 2/17 个有
- `wanBlockSwap` —— 2/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 17 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 17 | 100% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | euler | - | 17 | 100% |
| 重绘幅度 | simple | - | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，17 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，17 个样本，一致性 100%
- 重绘幅度 最常用 simple，17 个样本，一致性 100%
