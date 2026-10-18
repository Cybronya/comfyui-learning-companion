---
key: 视频生成/文生视频/Wan2.1再进化，6G显存就能跑！GGUF量化版Wan2.1模型全攻略_1945700815371739138.json
name: Wan2.1再进化，6G显存就能跑！GGUF量化版Wan2.1模型全攻略_1945700815371739138.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1再进化，6G显存就能跑！GGUF量化版Wan2.1模型全攻略_1945700815371739138.json
hash: 84616ec64922056a
coverage: 1
learned_at: 2026-10-15 22:43:31
nodes: [LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoTeaCache, WanVideoEnhanceAVideo, WanVideoEmptyEmbeds, WanVideoVAELoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1再进化，6G显存就能跑！GGUF量化版Wan2.1模型全攻略_1945700815371739138.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1945700815371739138.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（13 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `WanVideoEmptyEmbeds`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `Label (rgthree)`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoTextEncode`、`Label (rgthree)`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、VHS_VideoCombine、WanVideoBlockSwap、WanVideoModelLoader
