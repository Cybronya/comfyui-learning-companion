---
key: 视频生成/图生视频/Wan2.2+VBVR+奖励lora 自动提示词-I2V_2045775730209984513.json
name: Wan2.2+VBVR+奖励lora 自动提示词-I2V_2045775730209984513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+VBVR+奖励lora 自动提示词-I2V_2045775730209984513.json
hash: a073567aa50fc3cc
coverage: 0.820513
learned_at: 2026-10-15 22:36:51
nodes: [CR Prompt Text, RH_LLMAPI_NODE, CR Prompt Text, CLIPTextEncode, easy showAnything, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJv2, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, VAEDecode, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, ModelSamplingSD3, KSamplerAdvanced, Note, easy cleanGpuUsed, JWInteger, VAELoader, SaveImage, SetNode, GetNode, CR Text, CR Prompt Text, ShellAgentPluginOutputText, Note, KSamplerAdvanced, Note, easy showAnything, RH_LLMAPI_Pro_Node, LoadImage, VHS_VideoCombine, JWInteger]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2+VBVR+奖励lora 自动提示词-I2V_2045775730209984513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045775730209984513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CR Prompt Text`
- `RH_LLMAPI_NODE`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `Note`
- `easy cleanGpuUsed`
- `JWInteger`
- `VAELoader`
- `SaveImage`
- `SetNode`
- `GetNode`
- `CR Text`
- `CR Prompt Text`
- `ShellAgentPluginOutputText`
- `Note`
- `KSamplerAdvanced` ★核心
- `Note`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `VHS_VideoCombine`
- `JWInteger`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`CR Prompt Text`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEDecode`、`PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`JWInteger`、`VAELoader`、`SaveImage`、`CR Text`、`ShellAgentPluginOutputText`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、UNETLoader
