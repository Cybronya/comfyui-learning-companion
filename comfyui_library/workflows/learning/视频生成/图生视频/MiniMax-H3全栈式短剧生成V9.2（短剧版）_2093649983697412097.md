---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V9.2（短剧版）_2093649983697412097.json
name: MiniMax-H3全栈式短剧生成V9.2（短剧版）_2093649983697412097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V9.2（短剧版）_2093649983697412097.json
hash: c9637436a5ae4291
coverage: 0.395349
learned_at: 2026-10-16 23:42:16
nodes: [GetNode, GetNode, GetNode, SetNode, MarkdownNote, GetNode, GetNode, GetImage, GetImage, GetNode, GetImage, ResolutionSelector, YuanTool, SetNode, SetNode, GetNode, SetNode, PrimitiveStringMultiline, ResolutionSelector, SetNode, SetNode, GetNode, MarkdownNote, PrimitiveStringMultiline, GetNode, GetNode, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, StringConcatenate, GetNode, PreviewAudio, ComfyMathExpression, GetNode, GetNode, GetNode, MiniMaxChunkFeedForward, SamplerCustomAdvanced, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, YuanAudioList, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, YUAN_TXTJsonSwitch, SetNode, YUAN_TXTShotDurations, PrimitiveStringMultiline, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, BasicGuider, GetNode, GetNode, SetNode, RandomNoise, BasicGuider, KSamplerSelect, GetNode, ManualSigmas, ManualSigmas, KSamplerSelect, ComfyMathExpression, SetNode, GetNode, ModelAttentionBackend, BasicScheduler, SplitSigmas, YuanAudioSplit, PrimitiveStringMultiline, YUAN_TXTPreviewContent, MiniMaxLowVRAMAttention, SetNode, SetNode, GetNode, PrimitiveBoolean, PrimitiveBoolean, PrimitiveInt, YuanAudioLoad, GetNode, YUAN_TXTJsonExtractor, Lora Loader Stack (rgthree), VAELoader, CLIPLoader, VAELoader, GetNode, SetNode, VAEDecodeAudio, GetNode, GetNode, ComfySwitchNode, GetNode, GetNode, GetNode, GetNode, Yuan_VideoUI, GetNode, GetNode, Yuan_H3Upscale3D, ImageFromBatch, GetNode, MiniMaxH3AddGuide, ComfySwitchNode, GetNode, GetNode, MiniMaxH3AddGuide, ComfySwitchNode, UNETLoader, StringReplace, YuanMultiImage, VAEDecode, SetNode, VHS_VideoCombine, PreviewImage, PrimitiveNode, ComfySwitchNode, Yuan_MiniMaxH3Video]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V9.2（短剧版）_2093649983697412097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V9.2（短剧版）_2093649983697412097.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（129 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `GetNode`
- `GetImage`
- `ResolutionSelector`
- `YuanTool`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `StringConcatenate`
- `GetNode`
- `PreviewAudio`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxChunkFeedForward`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `YuanAudioList`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `YUAN_TXTJsonSwitch`
- `SetNode`
- `YUAN_TXTShotDurations`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `GetNode`
- `GetNode`
- `SetNode`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `ModelAttentionBackend`
- `BasicScheduler`
- `SplitSigmas`
- `YuanAudioSplit`
- `PrimitiveStringMultiline`
- `YUAN_TXTPreviewContent`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `YuanAudioLoad`
- `GetNode`
- `YUAN_TXTJsonExtractor`
- `Lora Loader Stack (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Yuan_VideoUI`
- `GetNode`
- `GetNode`
- `Yuan_H3Upscale3D`
- `ImageFromBatch`
- `GetNode`
- `MiniMaxH3AddGuide`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3AddGuide`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `StringReplace`
- `YuanMultiImage`
- `VAEDecode` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `PrimitiveNode`
- `ComfySwitchNode`
- `Yuan_MiniMaxH3Video`

## 知识

覆盖率 **40%**（51/129）

**有卡**：`GetImage`、`ResolutionSelector`、`YuanTool`、`StringConcatenate`、`PreviewAudio`、`ComfyMathExpression`、`MiniMaxChunkFeedForward`、`SamplerCustomAdvanced`、`YuanAudioList`、`YUAN_TXTJsonSwitch`、`YUAN_TXTShotDurations`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`ModelAttentionBackend`、`BasicScheduler`、`SplitSigmas`、`YuanAudioSplit`、`YUAN_TXTPreviewContent`、`MiniMaxLowVRAMAttention`、`PrimitiveBoolean`、`YuanAudioLoad`、`YUAN_TXTJsonExtractor`、`Lora Loader Stack (rgthree)`、`VAELoader`、`CLIPLoader`、`VAEDecodeAudio`、`Yuan_VideoUI`、`Yuan_H3Upscale3D`、`ImageFromBatch`、`MiniMaxH3AddGuide`、`UNETLoader`、`StringReplace`、`YuanMultiImage`、`VAEDecode`、`VHS_VideoCombine`、`Yuan_MiniMaxH3Video`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
