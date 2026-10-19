---
name: unknown_workflow_video_117
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7595
common_nodes: [Any To Any, CR Prompt Text, GetVideoComponents, LoadVideo, Qwen3_VQA, RunningHubControlFoleyGenerator, RunningHubControlFoleyModelLoader, SaveVideo, VHS_SelectFilename, VHS_VideoCombine, easy showAnything]
problems: []
missing: [RunningHubControlFoleyGenerator, RunningHubControlFoleyModelLoader]
members: [音频生成/音频生成/ControlFoley视频配音效（提示词增强）_2054796403783806977.json, 音频生成/音频生成/ControlFoley视频音效生成V1 林耀5.6_2051933897461641217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_117

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/ControlFoley视频配音效（提示词增强）_2054796403783806977.json、音频生成/音频生成/ControlFoley视频音效生成V1 林耀5.6_2051933897461641217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Any To Any`
- `CR Prompt Text`
- `GetVideoComponents`
- `LoadVideo`
- `Qwen3_VQA`
- `RunningHubControlFoleyGenerator`
- `RunningHubControlFoleyModelLoader`
- `SaveVideo`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `Int` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：RunningHubControlFoleyGenerator、RunningHubControlFoleyModelLoader
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
