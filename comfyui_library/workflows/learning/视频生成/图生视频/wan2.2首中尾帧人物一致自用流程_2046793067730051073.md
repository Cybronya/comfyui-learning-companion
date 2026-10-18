---
key: 视频生成/图生视频/wan2.2首中尾帧人物一致自用流程_2046793067730051073.json
name: wan2.2首中尾帧人物一致自用流程_2046793067730051073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2首中尾帧人物一致自用流程_2046793067730051073.json
hash: ad1821f66f46ef9c
coverage: 0.923077
learned_at: 2026-10-15 22:37:00
nodes: [CLIPTextEncode, CLIPTextEncode, WanVideoNAG, ModelSamplingSD3, RIFE VFI, Int, VAEDecode, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, CLIPLoader, VAELoader, Note, SaveImage, KSamplerAdvanced, KSamplerAdvanced, WanVideoNAG, UnetLoaderGGUF, UnetLoaderGGUF, Note, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Note, VHS_VideoCombine, VHS_VideoCombine, ImageScale, ImageScale, WanFirstMiddleLastFrameToVideo, LoadImage, LoadImage, LoadImage, ImageScale, CLIPVisionLoader, LoadImage, CLIPVisionEncode, CLIPVisionEncode, CLIPVisionEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2首中尾帧人物一致自用流程_2046793067730051073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046793067730051073.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageScale`
- `ImageScale`
- `WanFirstMiddleLastFrameToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageScale`
- `CLIPVisionLoader`
- `LoadImage`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPVisionEncode`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`CLIPTextEncode`、`WanVideoNAG`、`ModelSamplingSD3`、`RIFE VFI`、`Int`、`VAEDecode`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`VAELoader`、`SaveImage`、`KSamplerAdvanced`、`UnetLoaderGGUF`、`Power Lora Loader (rgthree)`、`VHS_VideoCombine`、`ImageScale`、`WanFirstMiddleLastFrameToVideo`、`LoadImage`、`CLIPVisionLoader`、`CLIPVisionEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CLIPVisionEncode、Power Lora Loader (rgthree)
