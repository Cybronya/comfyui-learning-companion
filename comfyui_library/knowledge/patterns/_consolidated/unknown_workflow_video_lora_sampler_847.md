---
name: unknown_workflow_video_lora_sampler_847
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.47
common_nodes: [Any Switch (rgthree), BatchImagesNode, CFGGuider, CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, ExtractLinesByIndex, Fast Groups Bypasser (rgthree), GetNode, INTConstant, JjkText, KSamplerSelect, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LoraLoaderModelOnly, ManualSigmas, PreviewAny, PreviewImage, PrimitiveStringMultiline, ProcessString, PromptRelayEncode, PurgeVRAM_UTK, RandomNoise, SamplerCustomAdvanced, SetNode, SomethingToString, VAEDecode, VAELoaderKJ, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3-MSR V2参考生视频-参考音色-自定义音频-全自动版-V1.1_2080476788374986754.json, 视频生成/图生视频/LTX-2.3-MSR_V2参考生视频调优版-自动提示词-V1.1_2078270565433044994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_847

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3-MSR V2参考生视频-参考音色-自定义音频-全自动版-V1.1_2080476788374986754.json、视频生成/图生视频/LTX-2.3-MSR_V2参考生视频调优版-自动提示词-V1.1_2078270565433044994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：47%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BatchImagesNode`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ExtractLinesByIndex`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `JjkText`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ProcessString`
- `PromptRelayEncode`
- `PurgeVRAM_UTK`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SomethingToString`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AudioBeforeAfterSilence` —— 1/2 个有
- `CM_IntToFloat` —— 1/2 个有
- `FB_Qwen3TTSDialogueInference` —— 1/2 个有
- `FB_Qwen3TTSRoleBank` —— 1/2 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 1/2 个有
- `JoinStringMulti` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVAudioVideoMask` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `TextGenerateLTX2Prompt` —— 1/2 个有
- `VRAMReserver` —— 1/2 个有
- `WhisperSTT` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 145 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 145，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
