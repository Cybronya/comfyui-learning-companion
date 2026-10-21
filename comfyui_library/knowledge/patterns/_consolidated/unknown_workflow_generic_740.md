---
name: unknown_workflow_generic_740
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5385
common_nodes: [ImageLoader, JjkText, MultiTextConcatenate, RH_LLMAPI_Pro_Node, RH_RhartImageG25SunburstImageToImage, SaveImage, Text, easy cleanGpuUsed, easy saveText, easy showAnything, ttN concat]
problems: []
missing: [easy cleanGpuUsed, ttN concat, easy saveText]
members: [图片生成/图生图/2102576863053963265.json, 视频生成/图生视频/全能图片G2.5一键生成专业影视分镜与关键帧全流程提示词-多图版_2101493126711042050.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_740

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2102576863053963265.json、视频生成/图生视频/全能图片G2.5一键生成专业影视分镜与关键帧全流程提示词-多图版_2101493126711042050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageLoader`
- `JjkText`
- `MultiTextConcatenate`
- `RH_LLMAPI_Pro_Node`
- `RH_RhartImageG25SunburstImageToImage`
- `SaveImage`
- `Text`
- `easy cleanGpuUsed`
- `easy saveText`
- `easy showAnything`
- `ttN concat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、ttN concat、easy saveText
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
