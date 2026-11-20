---
name: unknown_workflow_video_117
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.747
common_nodes: [ACEStepGen, AudioSeparation, CR Text, Float, GenerationParameters, GetNode, ImageCASharpening+, ImpactSwitch, Int, LoadAudio, LoadImage, MultiLineLyrics, MultiLinePromptACES, PreviewAudio, RH_Translator, SaveAudio, SetNode, VHS_LoadVideo, VHS_VideoCombine, workflow>1]
problems: []
missing: []
members: [视频生成/图生视频/【强强联合】ACE-Step音乐生成+SONIC数字人（精准对口型）_1922477274111868929.json, 视频生成/图生视频/【音轨分离重组】ACE-Step音乐生成+Float数字人（精准对口型）_1919189623304818689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_117

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/【强强联合】ACE-Step音乐生成+SONIC数字人（精准对口型）_1922477274111868929.json、视频生成/图生视频/【音轨分离重组】ACE-Step音乐生成+Float数字人（精准对口型）_1919189623304818689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `ACEStepGen`
- `AudioSeparation`
- `CR Text`
- `Float`
- `GenerationParameters`
- `GetNode`
- `ImageCASharpening+`
- `ImpactSwitch`
- `Int`
- `LoadAudio`
- `LoadImage`
- `MultiLineLyrics`
- `MultiLinePromptACES`
- `PreviewAudio`
- `RH_Translator`
- `SaveAudio`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `workflow>1`

**可变部分**（部分 workflow 才有）：
- `FloatProcess` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LoadFloatModels` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SONICSampler` —— 1/2 个有
- `SONICTLoader` —— 1/2 个有
- `SONIC_PreData` —— 1/2 个有
- `unCLIPCheckpointLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
