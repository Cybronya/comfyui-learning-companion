---
key: 视频生成/图生视频/QIANSUI+Qwen3.5+Wan2.2图生视频V10_2041867989393346562.json
name: QIANSUI+Qwen3.5+Wan2.2图生视频V10_2041867989393346562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/QIANSUI+Qwen3.5+Wan2.2图生视频V10_2041867989393346562.json
hash: c2b9ff05083299f7
coverage: 0.938776
learned_at: 2026-10-15 22:36:23
nodes: [easy cleanGpuUsed, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, VAELoader, CLIPTextEncode, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, Int, PainterI2V, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, VHS_VideoCombine, easy float, CM_IntToFloat, INTConstant, INTConstant, CLIPTextEncode, llama_cpp_parameters, easy showAnything, easy anythingIndexSwitch, easy cleanGpuUsed, easy showAnything, LoadImage, RIFE VFI, MarkdownNote, VHS_VideoCombine, CR Prompt Text, ShellAgentPluginOutputText, llama_cpp_instruct_adv, easy float, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, UNETLoader, easy int, CR Text, llama_cpp_model_loader, Int, SimpleMath+, easy int, easy int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/QIANSUI+Qwen3.5+Wan2.2图生视频V10_2041867989393346562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041867989393346562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `easy cleanGpuUsed`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `easy float`
- `CM_IntToFloat`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `llama_cpp_parameters`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy showAnything`
- `LoadImage`
- `RIFE VFI`
- `MarkdownNote`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `ShellAgentPluginOutputText`
- `llama_cpp_instruct_adv`
- `easy float`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `easy int`
- `CR Text`
- `llama_cpp_model_loader`
- `Int`
- `SimpleMath+`
- `easy int`
- `easy int`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（46/49）

**有卡**：`easy cleanGpuUsed`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`PainterI2V`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`easy float`、`CM_IntToFloat`、`INTConstant`、`llama_cpp_parameters`、`easy anythingIndexSwitch`、`LoadImage`、`RIFE VFI`、`CR Prompt Text`、`ShellAgentPluginOutputText`、`llama_cpp_instruct_adv`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`UNETLoader`、`easy int`、`CR Text`、`llama_cpp_model_loader`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
