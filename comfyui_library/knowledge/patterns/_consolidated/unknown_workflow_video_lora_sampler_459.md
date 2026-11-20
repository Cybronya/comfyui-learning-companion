---
name: unknown_workflow_video_lora_sampler_459
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6946
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSamplerAdvanced, LoraLoaderModelOnly, ModelPatchLoader, PainterAV2V, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [数字人/数字人/03-10-13-WAN2.1-数字人-InfiniteTalk-视频AV2V对口型-脸部参考_2019272890222383105.json, 数字人/数字人/InfiniteTalk 视频V2V对口型-轻度换脸OR增强一致性_2018621192965464066.json, 数字人/数字人/【2月】视频唇型同步+一致性加强，更好的支持人物动态_2017966613697404930.json, 数字人/数字人/【官流】数字人音频+视频动态驱动AV2V_2017248198519169026.json, 数字人/数字人/最新infinte视频对口型驱动AV2V_2018926134733312001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_459

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/03-10-13-WAN2.1-数字人-InfiniteTalk-视频AV2V对口型-脸部参考_2019272890222383105.json、数字人/数字人/InfiniteTalk 视频V2V对口型-轻度换脸OR增强一致性_2018621192965464066.json、数字人/数字人/【2月】视频唇型同步+一致性加强，更好的支持人物动态_2017966613697404930.json、数字人/数字人/【官流】数字人音频+视频动态驱动AV2V_2017248198519169026.json、数字人/数字人/最新infinte视频对口型驱动AV2V_2018926134733312001.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PainterAV2V`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 4/5 个有
- `PainterAudioCut` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `TDQwen3TTSModelLoader` —— 2/5 个有
- `TDQwen3TTSVoiceDesign` —— 2/5 个有
- `TTResolutionSelector` —— 2/5 个有
- `Text` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 4 | 5 | 88% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | dpmpp_sde | - | 5 | 100% |
| 重绘幅度 | normal | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 4，5 个样本，取值集中（一致性 88%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，5 个样本，一致性 100%
- 重绘幅度 最常用 normal，5 个样本，一致性 100%
