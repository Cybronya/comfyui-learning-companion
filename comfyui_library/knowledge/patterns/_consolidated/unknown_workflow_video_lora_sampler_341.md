---
name: unknown_workflow_video_lora_sampler_341
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.996571
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, CLIPLoader, CLIPTextEncode, CR Text, ColorMatch, Float to Int, INTConstant, ImageFromBatch, ImageResizeKJv2, KSamplerAdvanced, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelPatchTorchSettings, PainterAI2V, PainterAudioCut, PathchSageAttentionKJ, RHHiddenNodes, RH_GetAudioDuration, SimpleMath+, SomethingToString, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WujiCleaner]
problems: []
missing: []
members: [数字人/数字人/Wan2.2+RCM对口型工作流高动态_2021028256081780738.json, 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017919302799724546.json, 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017944917347147778.json, 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2018324382791245826.json, 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2026965800891981825.json, 视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2027307352143171585.json, 视频生成/图生视频/Wan2.2+RCM+Infinite+Talk官方对口型工作流图生数字人_2019421530488315905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_341

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/Wan2.2+RCM对口型工作流高动态_2021028256081780738.json、视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017919302799724546.json、视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2017944917347147778.json、视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2018324382791245826.json、视频生成/图生视频/Wan2.2+RCM+Infinite Talk官方对口型工作流高动态图生数字人_2026965800891981825.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatch`
- `Float to Int`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `PainterAI2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `RHHiddenNodes`
- `RH_GetAudioDuration`
- `SimpleMath+`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WujiCleaner`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
