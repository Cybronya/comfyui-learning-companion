---
name: unknown_workflow_video_sampler_checkpoint_14
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.436
common_nodes: [CR String To Boolean, ConvertAny2Float, Echo_LoadModel, Echo_Sampler, Florence2ModelLoader, Florence2Run, GetNode, ImageCrop+, ImageOnlyCheckpointLoader, ImageScale, JjkText, LoadAudio, LoadImage, MaskToSEGS, NTCosyVoiceInstruct2Sampler, NTCosyVoiceZeroShotSampler, PreviewImage, SEGSToImageList, SONICSampler, SONICTLoader, SONIC_PreData, SetNode, ShellAgentPluginSaveVideoVHS, VHS_VideoCombine, easy ifElse, easy imageSizeByLongerSide]
problems: []
missing: []
members: [数字人/数字人/路哥-数字人口播 V2_2019286526210871297.json, 视频生成/图生视频/数字人口播（sonic+cosyvoice2）_1895135793772429313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/路哥-数字人口播 V2_2019286526210871297.json、视频生成/图生视频/数字人口播（sonic+cosyvoice2）_1895135793772429313.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
- `CR String To Boolean`
- `ConvertAny2Float`
- `Echo_LoadModel`
- `Echo_Sampler`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `ImageCrop+`
- `ImageOnlyCheckpointLoader`
- `ImageScale`
- `JjkText`
- `LoadAudio`
- `LoadImage`
- `MaskToSEGS`
- `NTCosyVoiceInstruct2Sampler`
- `NTCosyVoiceZeroShotSampler`
- `PreviewImage`
- `SEGSToImageList`
- `SONICSampler`
- `SONICTLoader`
- `SONIC_PreData`
- `SetNode`
- `ShellAgentPluginSaveVideoVHS`
- `VHS_VideoCombine`
- `easy ifElse`
- `easy imageSizeByLongerSide`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
