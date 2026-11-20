---
key: 平台全量/wan2.1爆发能量光柱_1948954559285735425.json
name: wan2.1爆发能量光柱_1948954559285735425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.1爆发能量光柱_1948954559285735425.json
hash: 9d2a0de890de64e6
coverage: 1
learned_at: 2026-11-14 01:19:13
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoTeaCache, WanVideoSLG, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoImageClipEncode, WanVideoSampler, WanVideoExperimentalArgs, VHS_VideoCombine, WanVideoDecode, LoadImage, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoTextEncode, RH_Translator]
patterns: []
missing: []
---

# 平台全量/wan2.1爆发能量光柱_1948954559285735425.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.1爆发能量光柱_1948954559285735425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（16 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadImage`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `RH_Translator`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTeaCache`、`WanVideoSLG`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`RH_Translator`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
