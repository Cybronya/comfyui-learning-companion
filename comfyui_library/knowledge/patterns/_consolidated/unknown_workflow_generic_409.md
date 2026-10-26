---
name: unknown_workflow_generic_409
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.790143
common_nodes: [AFL:AudioMixStems, AudioSeparation, AudioTrim, LoadAudio, RunningHubRVCVoiceConversion, SaveAudio]
problems: []
missing: [AFL:AudioMixStems, RunningHubRVCModelLoader, RunningHubRVCVoiceConversion, RunningHubRVCZipModelLoader]
members: [音频生成/音频生成/ComfyUI_RH_RVC 基础工作流_2060185145348550658.json, 音频生成/音频生成/ComfyUI_RH_RVC 自传模型工作流_2060752729634590721.json, 音频生成/音频生成/RVC 基础工作流（RH版）_2099657242881646593.json, 音频生成/音频生成/RVC 自传模型工作流_2099657254856388610.json, 音频生成/音频生成/RVC_自传模型工作流_2100406899551330306.json, 音频生成/音频生成/RVC_自传模型工作流_2100494860670291970.json, 音频生成/音频生成/【ComfyUI】RH-RVC基础工作流｜AI变声_声音克隆+全节点注释_2061331767608565762.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_409

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（音频生成/音频生成/ComfyUI_RH_RVC 基础工作流_2060185145348550658.json、音频生成/音频生成/ComfyUI_RH_RVC 自传模型工作流_2060752729634590721.json、音频生成/音频生成/RVC 基础工作流（RH版）_2099657242881646593.json、音频生成/音频生成/RVC 自传模型工作流_2099657254856388610.json、音频生成/音频生成/RVC_自传模型工作流_2100406899551330306.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `AFL:AudioMixStems`
- `AudioSeparation`
- `AudioTrim`
- `LoadAudio`
- `RunningHubRVCVoiceConversion`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `RunningHubRVCZipModelLoader` —— 4/7 个有
- `RunningHubRVCModelLoader` —— 3/7 个有
- `LoadImage` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：AFL:AudioMixStems、RunningHubRVCModelLoader、RunningHubRVCVoiceConversion、RunningHubRVCZipModelLoader
