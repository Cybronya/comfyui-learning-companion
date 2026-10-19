---
name: unknown_workflow_video_sampler_checkpoint_6
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.956
common_nodes: [FloatProcess, GenerationParameters, ImageOnlyCheckpointLoader, LayerUtility: PurgeVRAM, LoadAudio, LoadFloatModels, LoadImage, MultiLineLyrics, MultiLinePromptACES, Note Plus (mtb), Note _O, PrimitiveFloat, SONICSampler, SONICTLoader, SONIC_PreData, SaveAudio, VHS_VideoCombine]
problems: []
missing: []
members: [音频生成/音频生成/AceStep声音、音乐局部编辑+数字人V1_1920523899745013761.json, 音频生成/音频生成/AceStep声音、音乐局部重绘+数字人V1_1920523940387819522.json, 音频生成/音频生成/AceStep声音、音乐扩展+数字人V1_1920523923002163201.json, 音频生成/音频生成/AceStep音乐生成稳定版+数字人V1_1920523877670391809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/AceStep声音、音乐局部编辑+数字人V1_1920523899745013761.json、音频生成/音频生成/AceStep声音、音乐局部重绘+数字人V1_1920523940387819522.json、音频生成/音频生成/AceStep声音、音乐扩展+数字人V1_1920523923002163201.json、音频生成/音频生成/AceStep音乐生成稳定版+数字人V1_1920523877670391809.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `FloatProcess`
- `GenerationParameters`
- `ImageOnlyCheckpointLoader`
- `LayerUtility: PurgeVRAM`
- `LoadAudio`
- `LoadFloatModels`
- `LoadImage`
- `MultiLineLyrics`
- `MultiLinePromptACES`
- `Note Plus (mtb)`
- `Note _O`
- `PrimitiveFloat`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SaveAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ACEStepEdit` —— 1/4 个有
- `ACEStepExtend` —— 1/4 个有
- `ACEStepGen` —— 1/4 个有
- `ACEStepRepainting` —— 1/4 个有
- `TrimAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
