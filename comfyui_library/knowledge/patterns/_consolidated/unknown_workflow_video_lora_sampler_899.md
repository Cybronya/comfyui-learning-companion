---
name: unknown_workflow_video_lora_sampler_899
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7615
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, ImageStitch, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, PreviewAny, PreviewImage, RH_Translator, RIFE VFI, RMBG, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/1988519913356746753.json, 视频生成/图生视频/1990436665472802817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_899

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1988519913356746753.json、视频生成/图生视频/1990436665472802817.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageStitch`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PreviewImage`
- `RH_Translator`
- `RIFE VFI`
- `RMBG`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `CR Text Input Switch (4 way)` —— 1/2 个有
- `CombinationText` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `ZML_AnyTypeSwitchFive` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | lcm | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
