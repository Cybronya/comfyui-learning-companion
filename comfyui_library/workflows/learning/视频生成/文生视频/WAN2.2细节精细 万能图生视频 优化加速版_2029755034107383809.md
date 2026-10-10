---
key: 视频生成/文生视频/WAN2.2细节精细 万能图生视频 优化加速版_2029755034107383809.json
name: WAN2.2细节精细 万能图生视频 优化加速版_2029755034107383809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2细节精细 万能图生视频 优化加速版_2029755034107383809.json
hash: 2f2667df5490eb90
coverage: 0.435897
learned_at: 2026-10-11 03:16:49
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, VAELoader, Note, CLIPLoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Reroute, UNETLoader, Fast Groups Bypasser (rgthree), Reroute, Reroute, Note, Reroute, ModelSamplingSD3, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Reroute, Reroute, ModelSamplingSD3, Reroute, easy cleanGpuUsed, Reroute, Reroute, VAEDecode, Note, KSamplerAdvanced, KSamplerAdvanced, INTConstant, INTConstant, Reroute, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Note, CLIPTextEncode, Reroute, LoraLoaderModelOnly, PreviewImage, INTConstant, INTConstant, Resize, GetImageSizeRatio, INTConstant, FL_RIFE, VHS_VideoCombine, VHS_VideoCombine, DWPreprocessor, SaveImage, LoadImage, LoadImage, CR Text, Fast Groups Bypasser (rgthree)]
patterns: []
missing: [CR Text, easy cleanGpuUsed]
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/WAN2.2细节精细 万能图生视频 优化加速版_2029755034107383809.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2细节精细 万能图生视频 优化加速版_2029755034107383809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
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
- `FL_RIFE`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **44%**（34/78）

**有卡**：`PathchSageAttentionKJ`、`CLIPTextEncode`、`ModelPatchTorchSettings`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`VAEDecode`、`KSamplerAdvanced`、`INTConstant`、`Resize`、`GetImageSizeRatio`、`FL_RIFE`、`VHS_VideoCombine`、`DWPreprocessor`、`SaveImage`、`LoadImage`

**缺卡**（2）：`CR Text`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
