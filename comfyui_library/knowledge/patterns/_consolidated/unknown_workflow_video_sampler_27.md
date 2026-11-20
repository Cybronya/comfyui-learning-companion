---
name: unknown_workflow_video_sampler_27
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9375
common_nodes: [JWImageResizeByLongerSide, LatentSyncNode, LoadAudio, NTCosyVoiceCrossLingualSampler, NTCosyVoiceInstruct2Sampler, PreviewAudio, ShellAgentPluginSaveAudio, VHS_LoadVideo, VHS_VideoCombine, VideoLengthAdjuster]
problems: []
missing: []
members: [数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频数字人（超清+超速+加长）V2_1902618231192891393.json, 数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频生成数字人@ys_1911668041246277634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频数字人（超清+超速+加长）V2_1902618231192891393.json、数字人/数字人/LatentSync新版1.5+CosyVoice2 TTS视频生成数字人@ys_1911668041246277634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `JWImageResizeByLongerSide`
- `LatentSyncNode`
- `LoadAudio`
- `NTCosyVoiceCrossLingualSampler`
- `NTCosyVoiceInstruct2Sampler`
- `PreviewAudio`
- `ShellAgentPluginSaveAudio`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VideoLengthAdjuster`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `NTCosyVoiceZeroShotSampler` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `Note _O` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
