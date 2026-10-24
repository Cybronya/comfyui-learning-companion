---
name: unknown_workflow_generic_255
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.865556
common_nodes: [LoadAudio, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple]
problems: []
missing: []
members: [音频生成/音频生成/IndexTTS2-AudioEmo_Multi_Clone_2068685833959469057.json, 音频生成/音频生成/IndexTTS2-AudioEmo_Single_Clone_2068687257116168194.json, 音频生成/音频生成/IndexTTS2-VectorEmo_Multi_Clone_2068687860949143553.json, 音频生成/音频生成/IndexTTS2-VectorEmo_Single_Clone_2068688742629601281.json, 音频生成/音频生成/indextts2基础+情感_2014670620402913282.json, 音频生成/音频生成/indextts2声音模仿+语气情感设置_1981744577625374722.json, 音频生成/音频生成/indextts多人参考+情感_2002383614916608001.json, 音频生成/音频生成/indextts多人参考+情感_2014670668457054209.json, 音频生成/音频生成/indextts多人声音参考+情感_1992213630209028098.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_255

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/IndexTTS2-AudioEmo_Multi_Clone_2068685833959469057.json、音频生成/音频生成/IndexTTS2-AudioEmo_Single_Clone_2068687257116168194.json、音频生成/音频生成/IndexTTS2-VectorEmo_Multi_Clone_2068687860949143553.json、音频生成/音频生成/IndexTTS2-VectorEmo_Single_Clone_2068688742629601281.json、音频生成/音频生成/indextts2基础+情感_2014670620402913282.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadAudio`
- `easy downloadIndexTTSAndLoadModel`
- `easy indexTTSGenerateSimple`

**可变部分**（部分 workflow 才有）：
- `SaveAudioMP3` —— 7/9 个有
- `easy indexTTSEmotionAudio` —— 7/9 个有
- `easy indexTTSEmotionVector` —— 7/9 个有
- `easy indexTTSEmotionMerge` —— 6/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `PreviewAudio` —— 3/9 个有
- `SaveAudio` —— 3/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
