---
name: unknown_workflow_video_lora_sampler_661
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.548
common_nodes: [AudioCrop, AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, ColorMatch, GetNode, ImageFromBatch, ImageResizeKJv2, Int, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PainterAI2V, PainterAudioCut, PreviewAudio, SetNode, SimpleMath+, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy promptLine]
problems: []
missing: []
members: [数字人/数字人/【官流】数字人AI2V 图片转数字人_2016740657276129281.json, 视频生成/图生视频/【推荐，图片对口型】单图+音频+提示词驱动数字人_2018019225536831490.json, 视频生成/图生视频/图片转数字人_2045963626250506242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_661

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/【官流】数字人AI2V 图片转数字人_2016740657276129281.json、视频生成/图生视频/【推荐，图片对口型】单图+音频+提示词驱动数字人_2018019225536831490.json、视频生成/图生视频/图片转数字人_2045963626250506242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PainterAI2V`
- `PainterAudioCut`
- `PreviewAudio`
- `SetNode`
- `SimpleMath+`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `PreviewImage` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
