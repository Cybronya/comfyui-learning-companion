---
key: 视频生成/文生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193.json
name: Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193.json
hash: 15114922b8dbafba
coverage: 0.442857
learned_at: 2026-10-15 22:47:11
nodes: [Note, easy showAnything, Any To Any, MultiplePathsInput, VHS_SelectFilename, LayerUtility: PurgeVRAM V2, Reroute, PathchSageAttentionKJ, PathchSageAttentionKJ, Reroute, Reroute, Note, Note, Note, Reroute, ModelPatchTorchSettings, Reroute, ModelPatchTorchSettings, Reroute, Reroute, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, WanImageToVideo, Reroute, Reroute, Reroute, Note, Int, INTConstant, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPLoader, CLIPTextEncode, WanMoeKSampler, wanBlockSwap, VAEDecode, LayerUtility: PurgeVRAM V2, RIFE VFI, Reroute, Reroute, Note, Fast Groups Bypasser (rgthree), Note, easy float, Reroute, Reroute, Reroute, Reroute, VHS_VideoCombine, Reroute, LoraLoaderModelOnly, VAELoader, UnetLoaderGGUF, UNETLoader, wanBlockSwap, Int, Int, VHS_VideoCombine, HunyuanVideoFoley, Qwen3_VQA]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（70 个）：
- `Note`
- `easy showAnything`
- `Any To Any`
- `MultiplePathsInput`
- `VHS_SelectFilename`
- `LayerUtility: PurgeVRAM V2`
- `Reroute`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `Reroute`
- `Reroute`
- `Note`
- `Note`
- `Note`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanImageToVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Note`
- `Int`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `WanMoeKSampler` ★核心
- `wanBlockSwap`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `RIFE VFI`
- `Reroute`
- `Reroute`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `easy float`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `wanBlockSwap`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `HunyuanVideoFoley`
- `Qwen3_VQA`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **44%**（31/70）

**有卡**：`Any To Any`、`MultiplePathsInput`、`VHS_SelectFilename`、`LayerUtility: PurgeVRAM V2`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`WanImageToVideo`、`Int`、`INTConstant`、`CLIPLoader`、`WanMoeKSampler`、`wanBlockSwap`、`VAEDecode`、`RIFE VFI`、`easy float`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`VAELoader`、`UnetLoaderGGUF`、`UNETLoader`、`HunyuanVideoFoley`、`Qwen3_VQA`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、Int
