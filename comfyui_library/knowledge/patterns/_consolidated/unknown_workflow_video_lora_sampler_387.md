---
name: unknown_workflow_video_lora_sampler_387
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.82
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatch, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingSD3, PainterAI2V, PainterAudioCut, PathchSageAttentionKJ, PreviewAny, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/2019801194713059330.json, 视频生成/图生视频/2019054926323781634.json, 视频生成/图生视频/2017275905328029697.json, 视频生成/图生视频/2017275219941003265.json, 视频生成/图生视频/2017267666708340738.json, 音频生成/音频生成/影视新闻数字人--真人感LongCat声音克隆--高动态Infinite Talk_2041718640755613698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_387

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2019801194713059330.json、视频生成/图生视频/2019054926323781634.json、视频生成/图生视频/2017275905328029697.json、视频生成/图生视频/2017275219941003265.json、视频生成/图生视频/2017267666708340738.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ColorMatch`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingSD3`
- `PainterAI2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CastAnyToIntStringFloat` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `RH_GetAudioDuration` —— 4/6 个有
- `RIFE VFI` —— 4/6 个有
- `SaveAudio` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `FB_Qwen3TTSCustomVoice` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/6 个有
- `LongCatVoiceCloneTTS` —— 1/6 个有
- `NormalizeAudioLoudness` —— 1/6 个有
- `Qwen3ASRLoader` —— 1/6 个有
- `Qwen3ASRTranscribe` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | dpmpp_sde | - | 6 | 67% |
| 重绘幅度 | normal | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，6 个样本，一致性 67%
- 重绘幅度 最常用 normal，6 个样本，一致性 100%
