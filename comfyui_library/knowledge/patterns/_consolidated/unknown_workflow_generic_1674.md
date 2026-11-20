---
name: unknown_workflow_generic_1674
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9445
common_nodes: [FL_CosyVoice3_AudioCrop, FL_CosyVoice3_CrossLingual, FL_CosyVoice3_Dialog, FL_CosyVoice3_ModelLoader, FL_CosyVoice3_VoiceConversion, FL_CosyVoice3_ZeroShot, LoadAudio]
problems: []
missing: [FL_CosyVoice3_Dialog, FL_CosyVoice3_VoiceConversion]
members: [数字人/数字人/音频音色替换_2114332459658727426.json, 音频生成/音频生成/【遇见AI】CosyVoice3语音，声音克隆，音色转换，跨语言，多人对话_2047150124933058562.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1674

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/音频音色替换_2114332459658727426.json、音频生成/音频生成/【遇见AI】CosyVoice3语音，声音克隆，音色转换，跨语言，多人对话_2047150124933058562.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `FL_CosyVoice3_AudioCrop`
- `FL_CosyVoice3_CrossLingual`
- `FL_CosyVoice3_Dialog`
- `FL_CosyVoice3_ModelLoader`
- `FL_CosyVoice3_VoiceConversion`
- `FL_CosyVoice3_ZeroShot`
- `LoadAudio`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SaveAudioAdvanced` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：FL_CosyVoice3_Dialog、FL_CosyVoice3_VoiceConversion
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
