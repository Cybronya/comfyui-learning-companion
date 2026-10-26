---
key: 数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频生成数字人@ys_1911668041246277634.json
name: LatentSync新版1.5+CosyVoice2 TTS视频生成数字人@ys_1911668041246277634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频生成数字人@ys_1911668041246277634.json
hash: eebf184414b75c49
coverage: 0.875
learned_at: 2026-10-26 01:56:17
nodes: [ShellAgentPluginSaveAudio, ShellAgentPluginSaveAudio, LoadAudio, LoadAudio, NTCosyVoiceInstruct2Sampler, NTCosyVoiceCrossLingualSampler, VHS_LoadVideo, Note, JWImageResizeByLongerSide, VideoLengthAdjuster, LatentSyncNode, VHS_VideoCombine, PreviewAudio, PreviewAudio, LoadAudio, Fast Groups Muter (rgthree)]
patterns: []
missing: []
---

# 数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频生成数字人@ys_1911668041246277634.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频生成数字人@ys_1911668041246277634.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（16 个）：
- `ShellAgentPluginSaveAudio`
- `ShellAgentPluginSaveAudio`
- `LoadAudio`
- `LoadAudio`
- `NTCosyVoiceInstruct2Sampler` ★核心
- `NTCosyVoiceCrossLingualSampler` ★核心
- `VHS_LoadVideo`
- `Note`
- `JWImageResizeByLongerSide`
- `VideoLengthAdjuster`
- `LatentSyncNode`
- `VHS_VideoCombine`
- `PreviewAudio`
- `PreviewAudio`
- `LoadAudio`
- `Fast Groups Muter (rgthree)`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`ShellAgentPluginSaveAudio`、`LoadAudio`、`NTCosyVoiceInstruct2Sampler`、`NTCosyVoiceCrossLingualSampler`、`VHS_LoadVideo`、`JWImageResizeByLongerSide`、`VideoLengthAdjuster`、`LatentSyncNode`、`VHS_VideoCombine`、`PreviewAudio`

**用到的条目**：NTCosyVoiceCrossLingualSampler、NTCosyVoiceInstruct2Sampler、LatentSyncNode、JWImageResizeByLongerSide、PreviewAudio、ShellAgentPluginSaveAudio、LoadAudio、VHS_LoadVideo
