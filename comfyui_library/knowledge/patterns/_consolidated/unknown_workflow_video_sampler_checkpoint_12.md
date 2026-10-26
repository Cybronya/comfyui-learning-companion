---
name: unknown_workflow_video_sampler_checkpoint_12
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9425
common_nodes: [ImageOnlyCheckpointLoader, LayerUtility: PurgeVRAM, LoadAudio, LoadImage, NTCosyVoiceCrossLingualSampler, NTCosyVoiceInstruct2Sampler, NTCosyVoiceZeroShotSampler, Note Plus (mtb), Note _O, PreviewAudio, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/Sonic无比例限制数字人+语音迁移TTS工作流_1893126942764511234.json, 视频生成/图生视频/IndexTTS（跨语种，支持夹子音，新模型）+Sonic无比例限制数字人工作流V2_1915048681744334849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/Sonic无比例限制数字人+语音迁移TTS工作流_1893126942764511234.json、视频生成/图生视频/IndexTTS（跨语种，支持夹子音，新模型）+Sonic无比例限制数字人工作流V2_1915048681744334849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadImage`
- `NTCosyVoiceCrossLingualSampler`
- `NTCosyVoiceInstruct2Sampler`
- `NTCosyVoiceZeroShotSampler`
- `Note Plus (mtb)`
- `Note _O`
- `PreviewAudio`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioCleanupNode` —— 1/2 个有
- `IndexTTSNode` —— 1/2 个有
- `SaveAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
