---
key: 视频生成/图生视频/Wan2.2- Lightx2v 1030-图生视频_1989613894270414850.json
name: Wan2.2- Lightx2v 1030-图生视频_1989613894270414850.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2- Lightx2v 1030-图生视频_1989613894270414850.json
hash: e4b909f75498fbae
coverage: 1
learned_at: 2026-10-15 22:33:07
nodes: [LoadImage, SimpleMath+, INTConstant, VAELoader, Wan22PromptSelector, LayerUtility: TextJoin, KSamplerAdvanced, VAEDecode, CLIPLoader, ImageResizeKJv2, CR Text, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine, PathchSageAttentionKJ, KSamplerAdvanced, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PainterI2V]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2- Lightx2v 1030-图生视频_1989613894270414850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989613894270414850.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（26 个）：
- `LoadImage`
- `SimpleMath+`
- `INTConstant`
- `VAELoader`
- `Wan22PromptSelector`
- `LayerUtility: TextJoin`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `ImageResizeKJv2`
- `CR Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PainterI2V`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`LoadImage`、`SimpleMath+`、`INTConstant`、`VAELoader`、`Wan22PromptSelector`、`LayerUtility: TextJoin`、`KSamplerAdvanced`、`VAEDecode`、`CLIPLoader`、`ImageResizeKJv2`、`CR Text`、`CLIPTextEncode`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`UNETLoader`、`LoraLoaderModelOnly`、`PainterI2V`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
