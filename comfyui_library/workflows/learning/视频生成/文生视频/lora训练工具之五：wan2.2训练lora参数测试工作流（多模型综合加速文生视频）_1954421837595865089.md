---
key: 视频生成/文生视频/lora训练工具之五：wan2.2训练lora参数测试工作流（多模型综合加速文生视频）_1954421837595865089.json
name: lora训练工具之五：wan2.2训练lora参数测试工作流（多模型综合加速文生视频）_1954421837595865089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/lora训练工具之五：wan2.2训练lora参数测试工作流（多模型综合加速文生视频）_1954421837595865089.json
hash: 112c3c22f169542e
coverage: 0.983333
learned_at: 2026-10-15 22:43:39
nodes: [MarkdownNote, CLIPTextEncode, UNETLoader, UnetLoaderGGUF, CLIPLoader, VAELoader, HunyuanImageToVideo, ShellAgentPluginInputImage, CFGZeroStar, ModelSamplingSD3, KSamplerAdvanced, EmptyHunyuanLatentVideo, WanVideoNAG, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, KSamplerAdvanced, CFGZeroStar, ModelSamplingSD3, KSamplerAdvanced, WanVideoNAG, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, CFGZeroStar, ModelSamplingSD3, KSamplerAdvanced, WanVideoNAG, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, KSamplerAdvanced, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo, CFGZeroStar, ModelSamplingSD3, KSamplerAdvanced, WanVideoNAG, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, KSamplerAdvanced, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo, CLIPTextEncode, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/lora训练工具之五：wan2.2训练lora参数测试工作流（多模型综合加速文生视频）_1954421837595865089.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1954421837595865089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（60 个）：
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `HunyuanImageToVideo`
- `ShellAgentPluginInputImage`
- `CFGZeroStar`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CFGZeroStar`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `CFGZeroStar`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `CFGZeroStar`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `WanVideoNAG`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **98%**（59/60）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`HunyuanImageToVideo`、`ShellAgentPluginInputImage`、`CFGZeroStar`、`ModelSamplingSD3`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`WanVideoNAG`、`PathchSageAttentionKJ`、`VAEDecode`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStar
