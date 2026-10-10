---
key: 视频生成/文生视频/Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频结构清晰版_1954923648895389698.json
name: Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频结构清晰版_1954923648895389698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频结构清晰版_1954923648895389698.json
hash: 5591a85454051305
coverage: 0.8125
learned_at: 2026-10-10 23:07:08
nodes: [CLIPTextEncode, CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, RIFE VFI, Int, VAEDecode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, CLIPLoader, VAELoader, WanImageToVideo, INTConstant, INTConstant, Note, SaveImage, KSamplerAdvanced, KSamplerAdvanced, WanVideoNAG, UnetLoaderGGUF, UnetLoaderGGUF, Note, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Note, INTConstant, LoadImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: [RIFE VFI, Power Lora Loader (rgthree), Power Lora Loader (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频结构清晰版_1954923648895389698.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-I2V + Lightx_2V 【新版2.2-4步加速Lora】图生视频结构清晰版_1954923648895389698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（32 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `ModelSamplingSD3`
- `RIFE VFI`
- `Int`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `WanImageToVideo`
- `INTConstant`
- `INTConstant`
- `Note`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `Note`
- `INTConstant`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`CLIPTextEncode`、`WanVideoNAG`、`ModelSamplingSD3`、`Int`、`VAEDecode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`WanImageToVideo`、`INTConstant`、`SaveImage`、`KSamplerAdvanced`、`UnetLoaderGGUF`、`LoadImage`、`VHS_VideoCombine`

**缺卡**（3）：`RIFE VFI`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、SaveImage、Int

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
