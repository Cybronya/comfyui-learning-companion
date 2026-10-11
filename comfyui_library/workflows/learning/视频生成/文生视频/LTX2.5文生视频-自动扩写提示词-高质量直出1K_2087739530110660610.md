---
key: 视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json
name: LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json
hash: fa935d6cc4d76dde
coverage: 0.804348
learned_at: 2026-10-11 20:53:38
nodes: [ComfyMathExpression, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, RandomNoise, ComfyMathExpression, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, LTXVAudioVAEDecode, LTXVLatentUpsampler, VAELoader, SamplerCustomAdvanced, LTXVDualCFGGuider, LTXVConditioning, KSamplerSelect, ManualSigmas, CLIPTextEncode, PrimitiveInt, LTXVSeparateAVLatent, CLIPTextEncode, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, PrimitiveInt, ResolutionSelector, PrimitiveInt, PrimitiveInt, SaveVideo, CLIPLoader, LatentUpscaleModelLoader, MarkdownNote, MarkdownNote, CR Prompt Text, ShellAgentPluginOutputText, easy showAnything, RH_LLMAPI_Pro_Node, CR Prompt Text, UNETLoader, VAELoader, LoraLoaderModelOnly]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频-自动扩写提示词-高质量直出1K_2087739530110660610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `ComfyMathExpression`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `RandomNoise`
- `ComfyMathExpression`
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVDualCFGGuider`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `CR Prompt Text`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（37/46）

**有卡**：`ComfyMathExpression`、`LTXVDualCFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RandomNoise`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`VAELoader`、`LTXVConditioning`、`CLIPTextEncode`、`ResolutionSelector`、`SaveVideo`、`CLIPLoader`、`LatentUpscaleModelLoader`、`ShellAgentPluginOutputText`、`RH_LLMAPI_Pro_Node`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
