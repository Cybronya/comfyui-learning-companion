---
key: 视频生成/图生视频/LTX2.3+BFS+MSR2.0_2080951858130153474.json
name: LTX2.3+BFS+MSR2.0_2080951858130153474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3+BFS+MSR2.0_2080951858130153474.json
hash: 63029dc3c304a6f1
coverage: 0.745455
learned_at: 2026-10-15 22:42:19
nodes: [SetNode, SetNode, UNETLoader, ComfyMathExpression, LTXVSeparateAVLatent, BasicScheduler, LTXVCropGuides, VAEDecode, ImageResizeKJv2, ComfyMathExpression, ComfySwitchNode, StringConcatenate, StringConcatenate, PreviewAny, TextGenerate, PreviewAny, SimpleCalculatorKJ, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, CLIPTextEncode, SaveVideo, ComfySwitchNode, LTXVConditioning, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, PrimitiveNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CFGGuider, SamplerCustomAdvanced, LTXVAudioVAEDecode, SaveVideo, LoraLoaderModelOnly, CreateVideo, PrimitiveFloat, PrimitiveInt, ComfyNumberConvert, LTX2_NAG, LTXIdentityOverlapConditioning, SaveVideo, SaveVideo, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, CLIPTextEncode, PrimitiveFloat, PrimitiveInt, SaveVideo, SaveVideo, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3+BFS+MSR2.0_2080951858130153474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080951858130153474.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `BasicScheduler`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `StringConcatenate`
- `StringConcatenate`
- `PreviewAny`
- `TextGenerate`
- `PreviewAny`
- `SimpleCalculatorKJ`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `ComfySwitchNode`
- `LTXVConditioning`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ComfyNumberConvert`
- `LTX2_NAG`
- `LTXIdentityOverlapConditioning`
- `SaveVideo`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveVideo`
- `SaveVideo`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（41/55）

**有卡**：`UNETLoader`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`BasicScheduler`、`LTXVCropGuides`、`VAEDecode`、`ImageResizeKJv2`、`StringConcatenate`、`TextGenerate`、`SimpleCalculatorKJ`、`VAELoaderKJ`、`DualCLIPLoader`、`CLIPTextEncode`、`SaveVideo`、`LTXVConditioning`、`RandomNoise`、`KSamplerSelect`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LoraLoaderModelOnly`、`CreateVideo`、`ComfyNumberConvert`、`LTX2_NAG`、`LTXIdentityOverlapConditioning`、`LTXICLoRALoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
