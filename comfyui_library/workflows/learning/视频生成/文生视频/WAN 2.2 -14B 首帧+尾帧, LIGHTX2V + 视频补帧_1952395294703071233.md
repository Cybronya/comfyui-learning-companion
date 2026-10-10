---
key: 视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json
name: WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json
hash: 1a16acc995f33293
coverage: 0.818182
learned_at: 2026-10-10 23:05:51
nodes: [INTConstant, INTConstant, Int, INTConstant, UnetLoaderGGUF, CLIPLoader, Int, Int, UnetLoaderGGUF, LoadImage, LoadImage, VAELoader, Power Lora Loader (rgthree), SimpleMath+, Power Lora Loader (rgthree), Note, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, WanFirstLastFrameToVideo, KSamplerAdvanced, Note, VAEDecode, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, SaveImage]
patterns: []
missing: [RIFE VFI, SimpleMath+, Power Lora Loader (rgthree), Power Lora Loader (rgthree)]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN 2.2 -14B 首帧+尾帧, LIGHTX2V + 视频补帧_1952395294703071233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `INTConstant`
- `INTConstant`
- `Int`
- `INTConstant`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `Int`
- `Int`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `Power Lora Loader (rgthree)`
- `SimpleMath+`
- `Power Lora Loader (rgthree)`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `Note`
- `VAEDecode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **82%**（27/33）

**有卡**：`INTConstant`、`Int`、`UnetLoaderGGUF`、`CLIPLoader`、`LoadImage`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`WanFirstLastFrameToVideo`、`VAEDecode`、`VHS_VideoCombine`、`SaveImage`

**缺卡**（4）：`RIFE VFI`、`SimpleMath+`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、SaveImage、Int

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
