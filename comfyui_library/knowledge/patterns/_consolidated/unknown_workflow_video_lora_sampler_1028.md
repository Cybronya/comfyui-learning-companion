---
name: unknown_workflow_video_lora_sampler_1028
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.904
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, FL_RIFE, INTConstant, Int, JjkText, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MMAudioFeatureUtilsLoader, MMAudioModelLoader, MMAudioSampler, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, PreviewAudio, PreviewImage, RH_Captioner, RH_Prompter, RH_Translator, SaveAudio, TextCombinerTwo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy showAnything, intToFloat _O]
problems: []
missing: []
members: [视频生成/文生视频/全自动-万能视频—高品质版_2060323027333763073.json, 视频生成/文生视频/全自动-万能视频—高品质版_2069427871608827905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1028

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/全自动-万能视频—高品质版_2060323027333763073.json、视频生成/文生视频/全自动-万能视频—高品质版_2069427871608827905.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `FL_RIFE`
- `INTConstant`
- `Int`
- `JjkText`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `MMAudioSampler`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PreviewAudio`
- `PreviewImage`
- `RH_Captioner`
- `RH_Prompter`
- `RH_Translator`
- `SaveAudio`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`
- `intToFloat _O`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
