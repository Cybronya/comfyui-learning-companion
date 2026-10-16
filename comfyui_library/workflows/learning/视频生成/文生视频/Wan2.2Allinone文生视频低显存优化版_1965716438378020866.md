---
key: 视频生成/文生视频/Wan2.2Allinone文生视频低显存优化版_1965716438378020866.json
name: Wan2.2Allinone文生视频低显存优化版_1965716438378020866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1965716438378020866.json
hash: 9b624f7bf87ca6a9
coverage: 0.954545
learned_at: 2026-10-15 22:43:44
nodes: [wanBlockSwap, TorchCompileModelWanVideoV2, ModelSamplingSD3, LayerUtility: PurgeVRAM, VAEDecodeTiled, CheckpointLoaderKJ, EmptyHunyuanLatentVideo, VHS_VideoCombine, KSampler, RIFE VFI, CLIPTextEncode, CLIPTextEncode, CR Prompt Text, CR Prompt Text, Int, Int, Int, Int, Float, Operation, Operation, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1063235649394010, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/Wan2.2Allinone文生视频低显存优化版_1965716438378020866.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1965716438378020866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `wanBlockSwap`
- `TorchCompileModelWanVideoV2`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `CheckpointLoaderKJ` ★核心
- `EmptyHunyuanLatentVideo`
- `VHS_VideoCombine`
- `KSampler` ★核心
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `Int`
- `Int`
- `Int`
- `Int`
- `Float`
- `Operation`
- `Operation`
- `Note`

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v10.safetensors`
- `seed` = `1063235649394010`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`wanBlockSwap`、`TorchCompileModelWanVideoV2`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM`、`VAEDecodeTiled`、`CheckpointLoaderKJ`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`、`KSampler`、`RIFE VFI`、`CLIPTextEncode`、`CR Prompt Text`、`Int`、`Float`、`Operation`

**用到的条目**：KSampler、CLIPTextEncode、VAEDecodeTiled、EmptyHunyuanLatentVideo、CheckpointLoaderKJ、CR Prompt Text、Int、ModelSamplingSD3

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
