---
name: unknown_workflow_generic_1268
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.623
common_nodes: [CLIPLoader, GetVideoComponents, LoadAudio, LoadImage, LoadVideo, PreviewAny, TextGenerate]
problems: []
missing: []
members: [comfyui-workflow-templates-json/llm_gemma4_text_gen.json, 图片生成/反推提示词/图片、视频、声音反推提示词_gemma4_2063052146509176834.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1268

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/llm_gemma4_text_gen.json、图片生成/反推提示词/图片、视频、声音反推提示词_gemma4_2063052146509176834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `GetVideoComponents`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `PreviewAny`
- `TextGenerate`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
