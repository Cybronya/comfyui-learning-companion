---
key: 音频生成/音频生成/YUE2.0 完整版_2099410162128875521.json
name: YUE2.0 完整版_2099410162128875521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/YUE2.0 完整版_2099410162128875521.json
hash: 01edead3d6a8f4e6
coverage: 0.764706
learned_at: 2026-10-18 17:45:46
nodes: [Note, SheetSage2AudioToABC, YuE2GenerateABC, AudioEncoderLoader, LoadAudio, PrimitiveStringMultiline, YuE2GenerateMusic, VAEDecodeAudioTiled, VAEDecodeAudio, KSampler, EmptyYuE2LatentAudio, SaveAudioAdvanced, CheckpointLoaderSimple, DF_Text_Box, DF_Text_Box, ImpactSwitch, PreviewAny]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1.1, "checkpoint": "yue2_3b_bf16.safetensors", "denoise": 1, "sampler_name": "dpm_2", "scheduler": "sgm_uniform", "seed": 828508824615986, "steps": 32}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 音频生成/音频生成/YUE2.0 完整版_2099410162128875521.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/YUE2.0 完整版_2099410162128875521.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（17 个）：
- `Note`
- `SheetSage2AudioToABC`
- `YuE2GenerateABC`
- `AudioEncoderLoader`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `YuE2GenerateMusic`
- `VAEDecodeAudioTiled` ★核心
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `EmptyYuE2LatentAudio`
- `SaveAudioAdvanced`
- `CheckpointLoaderSimple` ★核心
- `DF_Text_Box`
- `DF_Text_Box`
- `ImpactSwitch`
- `PreviewAny`

## 关键参数

- `seed` = `828508824615986`
- `steps` = `32`
- `cfg` = `1.1`
- `sampler_name` = `dpm_2`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `yue2_3b_bf16.safetensors`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`SheetSage2AudioToABC`、`YuE2GenerateABC`、`AudioEncoderLoader`、`LoadAudio`、`YuE2GenerateMusic`、`VAEDecodeAudioTiled`、`VAEDecodeAudio`、`KSampler`、`EmptyYuE2LatentAudio`、`SaveAudioAdvanced`、`CheckpointLoaderSimple`、`DF_Text_Box`

**用到的条目**：KSampler、CheckpointLoaderSimple、VAEDecodeAudio、AudioEncoderLoader、EmptyYuE2LatentAudio、VAEDecodeAudioTiled、SaveAudioAdvanced、DF_Text_Box

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
