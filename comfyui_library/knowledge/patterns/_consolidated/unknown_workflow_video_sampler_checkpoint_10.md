---
name: unknown_workflow_video_sampler_checkpoint_10
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.945
common_nodes: [ImageOnlyCheckpointLoader, LoadAudio, LoadImage, NTCosyVoiceCrossLingualSampler, NTCosyVoiceInstruct2Sampler, NTCosyVoiceZeroShotSampler, PreviewAudio, SONICSampler, SONICTLoader, SONIC_PreData, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/图片变数字人（无尺寸限制）+ 语音克隆_1902210757323595777.json, 数字人/数字人/Sonic无比例限制数字人+语音迁移TTS工作流_1893126942764511234.json, 视频生成/图生视频/IndexTTS（跨语种，支持夹子音，新模型）+Sonic无比例限制数字人工作流V2_1915048681744334849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/图片变数字人（无尺寸限制）+ 语音克隆_1902210757323595777.json、数字人/数字人/Sonic无比例限制数字人+语音迁移TTS工作流_1893126942764511234.json、视频生成/图生视频/IndexTTS（跨语种，支持夹子音，新模型）+Sonic无比例限制数字人工作流V2_1915048681744334849.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `LoadAudio`
- `LoadImage`
- `NTCosyVoiceCrossLingualSampler`
- `NTCosyVoiceInstruct2Sampler`
- `NTCosyVoiceZeroShotSampler`
- `PreviewAudio`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `Note _O` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `AudioCleanupNode` —— 1/3 个有
- `IndexTTSNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
