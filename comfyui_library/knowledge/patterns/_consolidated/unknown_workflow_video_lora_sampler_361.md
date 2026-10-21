---
name: unknown_workflow_video_lora_sampler_361
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.5815
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, LowVRAMCheckpointLoader, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2065971442394689538.json, 视频生成/图生视频/2067900124038254593.json, 视频生成/图生视频/2068177667341508609.json, 视频生成/图生视频/2067174173994213378.json, 视频生成/图生视频/2076230597940432898.json, 视频生成/文生视频/多参考图与高动态视频生成_ Ltx 2.3 Licon-MSR_2063854107001180161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_361

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2065971442394689538.json、视频生成/图生视频/2067900124038254593.json、视频生成/图生视频/2068177667341508609.json、视频生成/图生视频/2067174173994213378.json、视频生成/图生视频/2076230597940432898.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
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
- `LiconMSR`
- `LoadImage`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `LTXVAddGuideMulti` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `SimpleMath+` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `KenChenLLMGeminiBananaImageCollageNode` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `llama_cpp_instruct_adv` —— 2/6 个有
- `llama_cpp_model_loader` —— 2/6 个有
- `llama_cpp_parameters` —— 2/6 个有
- `孤海注释` —— 2/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 145 | 145 - 241 | 6 | 74% |
| 高度 | 24 | 24 - 50 | 6 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 145，观测区间 145 - 241，6 个样本
- 高度 中位数 24，观测区间 24 - 50，6 个样本
