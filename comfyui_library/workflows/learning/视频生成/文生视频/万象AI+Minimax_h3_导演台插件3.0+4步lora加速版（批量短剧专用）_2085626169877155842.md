---
key: 视频生成/文生视频/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2085626169877155842.json
name: 万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2085626169877155842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2085626169877155842.json
hash: b0a74ccae3451326
coverage: 0.944444
learned_at: 2026-10-15 22:47:46
nodes: [VAEDecodeAudio, VAEDecode, BasicScheduler, SamplerCustomAdvanced, VHS_VideoCombine, BasicGuider, KSamplerSelect, VAELoader, VAELoader, CLIPLoader, RandomNoise, LoadImage, PrimitiveStringMultiline, SFH3MultimodalDirector, UNETLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2085626169877155842.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2085626169877155842.json`

## 结构

**生成流程**：Model → Sampling → Decode → Other

**节点**（18 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `RandomNoise`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SFH3MultimodalDirector`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`BasicScheduler`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`BasicGuider`、`KSamplerSelect`、`VAELoader`、`CLIPLoader`、`RandomNoise`、`LoadImage`、`SFH3MultimodalDirector`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
