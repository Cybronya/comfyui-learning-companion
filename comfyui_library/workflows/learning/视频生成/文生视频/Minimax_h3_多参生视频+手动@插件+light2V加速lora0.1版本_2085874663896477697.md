---
key: 视频生成/文生视频/Minimax_h3_多参生视频+手动@插件+light2V加速lora0.1版本_2085874663896477697.json
name: Minimax_h3_多参生视频+手动@插件+light2V加速lora0.1版本_2085874663896477697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax_h3_多参生视频+手动@插件+light2V加速lora0.1版本_2085874663896477697.json
hash: 9374cbe6c809f82e
coverage: 0.964286
learned_at: 2026-10-11 20:53:46
nodes: [ImageResizeKJv2, easy clearCacheAll, GetImageRangeFromBatch, LoadImage, LoadImage, LoadImage, CreateVideo, LoadAudio, LoadAudio, LoadAudio, MiniMaxH3EasyOutput, MiniMaxH3AVDecodeT8, VHS_VideoCombine, RandomNoise, MiniMaxH3EasyLoader, BasicGuider, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, MiniMaxH3Easy, LoraLoaderModelOnly, SamplerCustomAdvanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8]
patterns: []
missing: [easy clearCacheAll]
discoveries: [次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Minimax_h3_多参生视频+手动@插件+light2V加速lora0.1版本_2085874663896477697.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax_h3_多参生视频+手动@插件+light2V加速lora0.1版本_2085874663896477697.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `ImageResizeKJv2`
- `easy clearCacheAll`
- `GetImageRangeFromBatch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CreateVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `RandomNoise`
- `MiniMaxH3EasyLoader`
- `BasicGuider`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `MiniMaxH3Easy`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心

## 知识

覆盖率 **96%**（27/28）

**有卡**：`ImageResizeKJv2`、`GetImageRangeFromBatch`、`LoadImage`、`CreateVideo`、`LoadAudio`、`MiniMaxH3EasyOutput`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`RandomNoise`、`MiniMaxH3EasyLoader`、`BasicGuider`、`VHS_LoadVideo`、`MiniMaxH3Easy`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3MultiRateSamplerEXPT8`

**缺卡**（1）：`easy clearCacheAll`

**用到的条目**：LoraLoaderModelOnly、LoadImage、SamplerCustomAdvanced、MiniMaxH3MultiRateSamplerEXPT8、MiniMaxH3AVDecodeT8、ImageResizeKJv2、MiniMaxH3EasyOutput、BasicGuider

## 学习发现

- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
