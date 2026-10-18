---
key: 视频生成/文生视频/ComfyOrg混元文生视频hunyuan_video_1870164228891123714.json
name: ComfyOrg混元文生视频hunyuan_video_1870164228891123714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ComfyOrg混元文生视频hunyuan_video_1870164228891123714.json
hash: 3693b7445b31e820
coverage: 0.894737
learned_at: 2026-10-15 22:43:19
nodes: [KSamplerSelect, BasicGuider, ModelSamplingSD3, Note, VAELoader, FluxGuidance, CLIPTextEncode, RandomNoise, EmptyHunyuanLatentVideo, DualCLIPLoader, RH_Prompter, SamplerCustomAdvanced, BasicScheduler, UNETLoader, VAEDecodeTiled, Note, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed]
patterns: []
missing: []
---

# 视频生成/文生视频/ComfyOrg混元文生视频hunyuan_video_1870164228891123714.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1870164228891123714.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ModelSamplingSD3`
- `Note`
- `VAELoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `EmptyHunyuanLatentVideo`
- `DualCLIPLoader`
- `RH_Prompter`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ModelSamplingSD3`、`VAELoader`、`FluxGuidance`、`CLIPTextEncode`、`RandomNoise`、`EmptyHunyuanLatentVideo`、`DualCLIPLoader`、`RH_Prompter`、`SamplerCustomAdvanced`、`BasicScheduler`、`UNETLoader`、`VAEDecodeTiled`、`VAEDecode`、`VHS_VideoCombine`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled
