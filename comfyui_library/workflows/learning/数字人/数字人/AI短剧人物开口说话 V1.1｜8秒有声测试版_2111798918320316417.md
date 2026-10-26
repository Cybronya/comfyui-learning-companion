---
key: 数字人/数字人/AI短剧人物开口说话 V1.1｜8秒有声测试版_2111798918320316417.json
name: AI短剧人物开口说话 V1.1｜8秒有声测试版_2111798918320316417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI短剧人物开口说话 V1.1｜8秒有声测试版_2111798918320316417.json
hash: 54821bd0d971fdbb
coverage: 0.716049
learned_at: 2026-10-26 01:53:45
nodes: [PrimitiveStringMultiline, ResolutionSelector, MarkdownNote, CLIPLoader, MarkdownNote, VAELoader, VAELoader, BasicGuider, RandomNoise, SamplerCustomAdvanced, PrimitiveFloat, ComfyMathExpression, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AVDecodeT8, MiniMaxH3MultiRateSamplerEXPT8, MarkdownNote, MarkdownNote, MarkdownNote, CLIPLoader, MarkdownNote, VAELoader, VAELoader, BasicGuider, RandomNoise, ComfyMathExpression, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AVDecodeT8, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CLIPLoader, VAELoader, VAELoader, BasicGuider, RandomNoise, SamplerCustomAdvanced, UniBlockSwap, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MultiRateSamplerEXPT8, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, ComfyMathExpression, PrimitiveStringMultiline, VHS_VideoCombine, LoadAudio, MarkdownNote, ResolutionSelector, PrimitiveFloat, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, UNETLoader, UNETLoader, LoraLoaderModelOnly, UniBlockSwap, Fast Groups Bypasser (rgthree), UniBlockSwap, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, SamplerCustomAdvanced, VHS_VideoCombine, MiniMaxH3AudioConditioningT8, PrimitiveFloat, MiniMaxH3MultiRateSamplerEXPT8, ResolutionSelector, MarkdownNote, PrimitiveStringMultiline, LoraLoaderModelOnly, StringFormat, CustomCombo, YuanCustomCombo, YuanCustomCombo, YuanCustomCombo, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/AI短剧人物开口说话 V1.1｜8秒有声测试版_2111798918320316417.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI短剧人物开口说话 V1.1｜8秒有声测试版_2111798918320316417.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（81 个）：
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveFloat`
- `ComfyMathExpression`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `ComfyMathExpression`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AVDecodeT8`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `UniBlockSwap`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `LoadAudio`
- `MarkdownNote`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AudioConditioningT8`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UniBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `UniBlockSwap`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `StringFormat`
- `CustomCombo`
- `YuanCustomCombo`
- `YuanCustomCombo`
- `YuanCustomCombo`
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **72%**（58/81）

**有卡**：`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3MultiRateSamplerEXPT8`、`UniBlockSwap`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LoadImage`、`LoadAudio`、`MiniMaxH3AudioConditioningT8`、`UNETLoader`、`StringFormat`、`CustomCombo`、`YuanCustomCombo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3MultiRateSamplerEXPT8
