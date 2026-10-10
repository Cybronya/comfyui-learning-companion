---
key: 视频生成/文生视频/Wan2.2无损加速工作流_1977282385228242946.json
name: Wan2.2无损加速工作流_1977282385228242946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2无损加速工作流_1977282385228242946.json
hash: f85fa77df483cffd
coverage: 0.941176
learned_at: 2026-10-10 23:08:06
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, SplitSigmas, TorchCompileModelWanVideoV2, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, PathchSageAttentionKJ, SamplerCustom, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, CLIPTextEncode, CLIPTextEncode, VAEDecode, VAEDecode, LoraLoaderModelOnly, Label (rgthree), Label (rgthree), VHS_VideoCombine, VHS_VideoCombine, FSampler, FSampler, wanBlockSwap, wanBlockSwap, ModelSamplingSD3, ModelSamplingSD3, SamplerCustom, KSamplerSelect, VAELoader, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, CLIPLoader]
patterns: []
missing: [Label (rgthree), Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2无损加速工作流_1977282385228242946.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2无损加速工作流_1977282385228242946.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（34 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SplitSigmas`
- `TorchCompileModelWanVideoV2`
- `TorchCompileModelWanVideoV2`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FSampler` ★核心
- `FSampler` ★核心
- `wanBlockSwap`
- `wanBlockSwap`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `CLIPLoader`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`LoraLoaderModelOnly`、`BasicScheduler`、`SplitSigmas`、`TorchCompileModelWanVideoV2`、`PathchSageAttentionKJ`、`SamplerCustom`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`FSampler`、`wanBlockSwap`、`ModelSamplingSD3`、`KSamplerSelect`、`VAELoader`、`DiffusionModelLoaderKJ`、`CLIPLoader`

**缺卡**（2）：`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、KSamplerSelect、SamplerCustom、FSampler

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
