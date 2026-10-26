---
name: unknown_workflow_generic_1661
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.835
common_nodes: [Audio To Text (mtb), CR Prompt Text, FishS2VoiceCloneTTS, Load Whisper (mtb), LoadAudio, LoadImage, PrimitiveStringMultiline, RH_GetAudioDuration, RH_LLMAPI_Pro_Node, RH_MagiHumanGenerate, RH_MagiHumanModelLoader, SaveVideo, StringConcat|Mie, ToInt]
problems: []
missing: []
members: [数字人/数字人/daVinci-MagiHuman数字人=台本+图片_2038453298851745794.json, 视频生成/图生视频/MagiHuman数字人_2039711659421343746.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1661

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/daVinci-MagiHuman数字人=台本+图片_2038453298851745794.json、视频生成/图生视频/MagiHuman数字人_2039711659421343746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio To Text (mtb)`
- `CR Prompt Text`
- `FishS2VoiceCloneTTS`
- `Load Whisper (mtb)`
- `LoadAudio`
- `LoadImage`
- `PrimitiveStringMultiline`
- `RH_GetAudioDuration`
- `RH_LLMAPI_Pro_Node`
- `RH_MagiHumanGenerate`
- `RH_MagiHumanModelLoader`
- `SaveVideo`
- `StringConcat|Mie`
- `ToInt`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PurgeVRAM_UTK` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Textbox` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
