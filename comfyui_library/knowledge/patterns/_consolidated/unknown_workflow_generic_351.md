---
name: unknown_workflow_generic_351
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83825
common_nodes: [CR Prompt Text, LoadAudio, LoadImage, PreviewAny, PreviewAudio, Qwen3ASRLoader_DFT, Qwen3ASRTranscribe_DFT, RunningHubAudio8ModelLoader, RunningHubAudio8Prompt, RunningHubAudio8Sampling, RunningHubAudio8TTS, SaveImage]
problems: []
missing: []
members: [音频生成/音频生成/Audio8 TTS语音克隆-自动翻译语言_2083906154077442049.json, 音频生成/音频生成/Audio8 TTS语音克隆_2083775492569784321.json, 音频生成/音频生成/Audio8 TTS语音克隆_2083854558199107585.json, 音频生成/音频生成/Audio8 TTS语音克隆_2083911488225501186.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_351

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Audio8 TTS语音克隆-自动翻译语言_2083906154077442049.json、音频生成/音频生成/Audio8 TTS语音克隆_2083775492569784321.json、音频生成/音频生成/Audio8 TTS语音克隆_2083854558199107585.json、音频生成/音频生成/Audio8 TTS语音克隆_2083911488225501186.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Prompt Text`
- `LoadAudio`
- `LoadImage`
- `PreviewAny`
- `PreviewAudio`
- `Qwen3ASRLoader_DFT`
- `Qwen3ASRTranscribe_DFT`
- `RunningHubAudio8ModelLoader`
- `RunningHubAudio8Prompt`
- `RunningHubAudio8Sampling`
- `RunningHubAudio8TTS`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `SaveAudioAdvanced` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `LayerUtility: TextJoin` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
