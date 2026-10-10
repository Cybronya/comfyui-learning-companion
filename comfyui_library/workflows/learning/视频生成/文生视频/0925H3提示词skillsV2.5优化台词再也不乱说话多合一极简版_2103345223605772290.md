---
key: 视频生成/文生视频/0925H3提示词skillsV2.5优化台词再也不乱说话多合一极简版_2103345223605772290.json
name: 0925H3提示词skillsV2.5优化台词再也不乱说话多合一极简版_2103345223605772290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/0925H3提示词skillsV2.5优化台词再也不乱说话多合一极简版_2103345223605772290.json
hash: b33ca5b457de1e44
coverage: 0.892857
learned_at: 2026-10-10 22:58:11
nodes: [BasicGuider, RandomNoise, KSamplerSelect, MiniMaxH3EasyOutput, LoadVideo, SamplerCustomAdvanced, 忽略多组孤海, MiniMaxH3EasyLoader, BasicScheduler, VAEDecode, VAEDecodeAudio, LoraLoaderModelOnly, ModelAttentionBackend, SamplerCustomAdvanced, ModelPreviewOverrideKJ, VHS_VideoCombine, MiniMaxH3EasyMediaLoader, PrimitiveStringMultiline, LoadImage, SplitSigmas, VAEDecodeAudio, VAEDecode, VHS_VideoCombine, LTXVSeparateAVLatent, LTXVConcatAVLatent, MinimaxH3LatentUpscaler3D, PrimitiveStringMultiline, MiniMaxH3Easy]
patterns: []
missing: [忽略多组孤海]
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/0925H3提示词skillsV2.5优化台词再也不乱说话多合一极简版_2103345223605772290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/0925H3提示词skillsV2.5优化台词再也不乱说话多合一极简版_2103345223605772290.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Other

**节点**（28 个）：
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `MiniMaxH3EasyOutput`
- `LoadVideo`
- `SamplerCustomAdvanced` ★核心
- `忽略多组孤海`
- `MiniMaxH3EasyLoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SamplerCustomAdvanced` ★核心
- `ModelPreviewOverrideKJ`
- `VHS_VideoCombine`
- `MiniMaxH3EasyMediaLoader`
- `PrimitiveStringMultiline`
- `LoadImage`
- `SplitSigmas`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveStringMultiline`
- `MiniMaxH3Easy`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`MiniMaxH3EasyOutput`、`LoadVideo`、`SamplerCustomAdvanced`、`MiniMaxH3EasyLoader`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`ModelPreviewOverrideKJ`、`VHS_VideoCombine`、`MiniMaxH3EasyMediaLoader`、`LoadImage`、`SplitSigmas`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`MinimaxH3LatentUpscaler3D`、`MiniMaxH3Easy`

**缺卡**（1）：`忽略多组孤海`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、LoadImage、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent、MinimaxH3LatentUpscaler3D

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
