---
key: 视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json
name: Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json
hash: 3937f37ce9197d3e
coverage: 0.742857
learned_at: 2026-10-15 22:47:10
nodes: [PrimitiveInt, ModelPatchTorchSettings, PathchSageAttentionKJ, wanBlockSwap, ModelSamplingSD3, PathchSageAttentionKJ, wanBlockSwap, ModelSamplingSD3, CLIPLoader, UNETLoader, UNETLoader, ModelPatchTorchSettings, CLIPTextEncode, CLIPTextEncode, MathExpression|pysssss, WanImageToVideo, KSamplerAdvanced, RH_LLMAPI_NODE, RH_LLMAPI_NODE, VHS_VideoCombine, VHS_VideoCombine, RIFE VFI, KSamplerAdvanced, VAELoader, VAEDecode, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, Note, Wan22PromptSelector, ImpactSwitch, PrimitiveInt, PrimitiveInt, Text Concatenate, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（35 个）：
- `PrimitiveInt`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RIFE VFI`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Note`
- `Wan22PromptSelector`
- `ImpactSwitch`
- `PrimitiveInt`
- `PrimitiveInt`
- `Text Concatenate`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（26/35）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`wanBlockSwap`、`ModelSamplingSD3`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`MathExpression|pysssss`、`WanImageToVideo`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`VHS_VideoCombine`、`RIFE VFI`、`VAELoader`、`VAEDecode`、`Wan22PromptSelector`、`Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Wan22PromptSelector、ModelPatchTorchSettings
