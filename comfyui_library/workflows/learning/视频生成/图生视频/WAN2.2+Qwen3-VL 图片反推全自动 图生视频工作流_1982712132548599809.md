---
key: 视频生成/图生视频/WAN2.2+Qwen3-VL 图片反推全自动 图生视频工作流_1982712132548599809.json
name: WAN2.2+Qwen3-VL 图片反推全自动 图生视频工作流_1982712132548599809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2+Qwen3-VL 图片反推全自动 图生视频工作流_1982712132548599809.json
hash: 74e8e25f7c1aef78
coverage: 0.804878
learned_at: 2026-10-15 22:32:42
nodes: [PathchSageAttentionKJ, ModelPatchTorchSettings, wanBlockSwap, wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, WanImageToVideo, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, Note, Fast Groups Bypasser (rgthree), PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, UNETLoader, VAELoader, CLIPLoader, INTConstant, INTConstant, Note, Int, Int, ImageLoader, Note, Qwen3_VQA, LayerUtility: ImageScaleByAspectRatio V2, MultiplePathsInput, PreviewImage, VHS_VideoCombine, Note, Note, easy showAnything, VHS_VideoCombine, RIFE VFI]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2+Qwen3-VL 图片反推全自动 图生视频工作流_1982712132548599809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982712132548599809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `INTConstant`
- `INTConstant`
- `Note`
- `Int`
- `Int`
- `ImageLoader`
- `Note`
- `Qwen3_VQA`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MultiplePathsInput`
- `PreviewImage`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `easy showAnything`
- `VHS_VideoCombine`
- `RIFE VFI`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **80%**（33/41）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`wanBlockSwap`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`WanImageToVideo`、`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`INTConstant`、`Int`、`ImageLoader`、`Qwen3_VQA`、`LayerUtility: ImageScaleByAspectRatio V2`、`MultiplePathsInput`、`VHS_VideoCombine`、`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Int
