---
name: unknown_workflow_video_lora_sampler_1047
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.896
common_nodes: [CFGGuider, CLIPTextEncode, CR Prompt Text, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, KenChenLLMGeminiBananaImageCollageNode, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, PreviewImage, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, SimpleMath+, VAEDecode, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/MSR继续进化，LTX-2.3 超强多图参考_2076230597940432898.json, 视频生成/文生视频/多参考图与高动态视频生成_ Ltx 2.3 Licon-MSR_2063854107001180161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1047

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MSR继续进化，LTX-2.3 超强多图参考_2076230597940432898.json、视频生成/文生视频/多参考图与高动态视频生成_ Ltx 2.3 Licon-MSR_2063854107001180161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `KenChenLLMGeminiBananaImageCollageNode`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `SimpleMath+`
- `VAEDecode`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | - | 2 | 100% |
| 高度 | 50 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
