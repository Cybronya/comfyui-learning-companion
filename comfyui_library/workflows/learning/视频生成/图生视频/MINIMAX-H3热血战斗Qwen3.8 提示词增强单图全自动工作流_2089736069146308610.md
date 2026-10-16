---
key: 视频生成/图生视频/MINIMAX-H3热血战斗Qwen3.8 提示词增强单图全自动工作流_2089736069146308610.json
name: MINIMAX-H3热血战斗Qwen3.8 提示词增强单图全自动工作流_2089736069146308610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MINIMAX-H3热血战斗Qwen3.8 提示词增强单图全自动工作流_2089736069146308610.json
hash: 757de601a9fdb290
coverage: 0.790698
learned_at: 2026-10-16 22:02:01
nodes: [PT_H3ConcatAVLatent, VAELoader, VAELoader, ComfyMathExpression, BasicGuider, RandomNoise, VAEEncode, BasicGuider, SamplerCustomAdvanced, CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, KSamplerSelect, BasicScheduler, RandomNoise, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, Label (rgthree), MiniMaxH3AVDecodeT8, MiniMaxH3AVDecodeT8, MemoryCleaner, MemoryCleaner, VHS_VideoCombine, Fast Groups Bypasser (rgthree), PreviewAny, llama_cpp_parameters, Text, MiniMaxH3AudioConditioningT8, llama_cpp_model_loader, LoraLoaderBypassModelOnly, Label (rgthree), SamplerCustomAdvanced, LoadImage, PrimitiveStringMultiline, llama_cpp_instruct_adv, PrimitiveFloat, ResolutionSelector, Note, Note, Note, easy saveText, PrimitiveStringMultiline, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/MINIMAX-H3热血战斗Qwen3.8 提示词增强单图全自动工作流_2089736069146308610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MINIMAX-H3热血战斗Qwen3.8 提示词增强单图全自动工作流_2089736069146308610.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Output → Other

**节点**（43 个）：
- `PT_H3ConcatAVLatent`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `BasicGuider`
- `RandomNoise`
- `VAEEncode` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `Label (rgthree)`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AVDecodeT8`
- `MemoryCleaner`
- `MemoryCleaner`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `llama_cpp_parameters`
- `Text`
- `MiniMaxH3AudioConditioningT8`
- `llama_cpp_model_loader`
- `LoraLoaderBypassModelOnly` ★核心
- `Label (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `PrimitiveFloat`
- `ResolutionSelector`
- `Note`
- `Note`
- `Note`
- `easy saveText`
- `PrimitiveStringMultiline`
- `MarkdownNote`

## 知识

覆盖率 **79%**（34/43）

**有卡**：`PT_H3ConcatAVLatent`、`VAELoader`、`ComfyMathExpression`、`BasicGuider`、`RandomNoise`、`VAEEncode`、`SamplerCustomAdvanced`、`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`KSamplerSelect`、`BasicScheduler`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`Label (rgthree)`、`MiniMaxH3AVDecodeT8`、`MemoryCleaner`、`llama_cpp_parameters`、`Text`、`MiniMaxH3AudioConditioningT8`、`llama_cpp_model_loader`、`LoraLoaderBypassModelOnly`、`LoadImage`、`llama_cpp_instruct_adv`、`ResolutionSelector`、`easy saveText`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
