---
name: unknown_workflow_video_lora_sampler_849
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.517667
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetNode, ImageFromBatch+, ImageResizeKJv2, KSamplerAdvanced, LoraLoaderModelOnly, ModelPatchLoader, PainterAV2V, PainterAudioCut, SetNode, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [数字人/数字人/【官流】数字人音频+视频动态驱动AV2V_2017248198519169026.json, 数字人/数字人/【推荐，视频对口型】视频+音频+提示词驱动数字人_2018014180963520514.json, 数字人/数字人/最新infinte视频对口型驱动AV2V_2018926134733312001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_849

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/【官流】数字人音频+视频动态驱动AV2V_2017248198519169026.json、数字人/数字人/【推荐，视频对口型】视频+音频+提示词驱动数字人_2018014180963520514.json、数字人/数字人/最新infinte视频对口型驱动AV2V_2018926134733312001.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetNode`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PainterAV2V`
- `PainterAudioCut`
- `SetNode`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `TDQwen3TTSModelLoader` —— 2/3 个有
- `TDQwen3TTSVoiceDesign` —— 2/3 个有
- `Text` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `Int` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | dpmpp_sde | - | 3 | 100% |
| 重绘幅度 | normal | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，3 个样本，一致性 100%
- 重绘幅度 最常用 normal，3 个样本，一致性 100%
