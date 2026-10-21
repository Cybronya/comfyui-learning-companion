---
name: unknown_workflow_upscale_latent_upscale_lora_62
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8825
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2043280274267574273.json, 视频生成/图生视频/2069594232695902209.json, 视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json, 视频生成/文生视频/LTX 2.3  首中尾三图+多图_2035272794954539010.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_62

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2043280274267574273.json、视频生成/图生视频/2069594232695902209.json、视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json、视频生成/文生视频/LTX 2.3  首中尾三图+多图_2035272794954539010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `FloatConstant` —— 2/4 个有
- `JoinStrings` —— 2/4 个有
- `LTXVImgToVideoInplaceKJ` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `easy imageScaleDown` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `llama_cpp_unload_model` —— 2/4 个有
- `Bjornulf_LoopBasicBatch` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `MinNode` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/4 个有
- `SaveImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
