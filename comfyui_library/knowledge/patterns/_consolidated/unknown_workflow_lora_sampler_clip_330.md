---
name: unknown_workflow_lora_sampler_clip_330
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9105
common_nodes: [CFGGuider, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, CreateVideo, EmptyLTXVLatentVideo, INTConstant, ImageBatchMultiple+, ImageConcatFromBatch, JjkText, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, PreviewAny, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/Ltx2.3 Licon-MSR全能参考生视频简雨版_2067917092258672641.json, 视频生成/图生视频/高帧率Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2064353517267152898.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_330

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Ltx2.3 Licon-MSR全能参考生视频简雨版_2067917092258672641.json、视频生成/图生视频/高帧率Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2064353517267152898.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageBatchMultiple+`
- `ImageConcatFromBatch`
- `JjkText`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `ManualSigmas`
- `PreviewAny`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageLoader` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LoaderGGUF` —— 1/2 个有
- `LowVRAMCheckpointLoader` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy positive` —— 1/2 个有

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
