---
name: unknown_workflow_generic_651
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.621
common_nodes: [CLIPLoader, LoadAudio, PreviewAny, SaveImage, TextGenerate]
problems: []
missing: []
members: [音频生成/音频生成/llm_gemma4_text_gen666_2066543100402683905.json, 音频生成/音频生成/llm_gemma4_text_gen_2067373155886391297.json, 音频生成/音频生成/llm_gemma4_text_gen_2067600813530370049.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_651

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/llm_gemma4_text_gen666_2066543100402683905.json、音频生成/音频生成/llm_gemma4_text_gen_2067373155886391297.json、音频生成/音频生成/llm_gemma4_text_gen_2067600813530370049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `LoadAudio`
- `PreviewAny`
- `SaveImage`
- `TextGenerate`

**可变部分**（部分 workflow 才有）：
- `1hew_SaveImage` —— 2/3 个有
- `LoadImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
