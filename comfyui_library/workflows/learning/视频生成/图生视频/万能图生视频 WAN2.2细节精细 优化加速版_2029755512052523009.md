---
key: 视频生成/图生视频/万能图生视频 WAN2.2细节精细 优化加速版_2029755512052523009.json
name: 万能图生视频 WAN2.2细节精细 优化加速版_2029755512052523009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2029755512052523009.json
hash: 0121019449d73d01
coverage: 0.44
learned_at: 2026-10-15 22:35:23
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Reroute, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Note, CLIPTextEncode, Reroute, LoraLoaderModelOnly, PreviewImage, INTConstant, INTConstant, Resize, GetImageSizeRatio, INTConstant, VHS_VideoCombine, CR Text, Fast Groups Bypasser (rgthree), VHS_VideoCombine, LoadImage, FL_RIFE]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/万能图生视频 WAN2.2细节精细 优化加速版_2029755512052523009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029755512052523009.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VAELoader`
- `Note`
- `CLIPLoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Reroute`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Reroute`
- `Note`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelSamplingSD3`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `VAEDecode` ★核心
- `Note`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `Resize`
- `GetImageSizeRatio`
- `INTConstant`
- `VHS_VideoCombine`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `LoadImage`
- `FL_RIFE`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **44%**（33/75）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Resize`、`GetImageSizeRatio`、`VHS_VideoCombine`、`CR Text`、`LoadImage`、`FL_RIFE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
