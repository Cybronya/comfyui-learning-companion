---
name: unknown_workflow_generic_2121
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.828
common_nodes: [Fast Groups Bypasser (rgthree), LoadAudio, PreviewAudio, SaveAudio, easy downloadIndexTTSAndLoadModel, easy indexTTSEmotionVector, easy indexTTSGenerateSimple]
problems: []
missing: []
members: [音频生成/音频生成/IndexTTS2 多人对话_2042951687509385218.json, 音频生成/音频生成/TTS2声音克隆+情感参考-老祺_2028309428746850306.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_2121

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/IndexTTS2 多人对话_2042951687509385218.json、音频生成/音频生成/TTS2声音克隆+情感参考-老祺_2028309428746850306.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `PreviewAudio`
- `SaveAudio`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSEmotionVector`
- `easy indexTTSGenerateSimple`

**可变部分**（部分 workflow 才有）：
- `Textbox` —— 1/2 个有
- `easy indexTTSEmotionMerge` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
