---
name: unknown_workflow_video_9
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7435
common_nodes: [CR Text Concatenate, GetVideoComponents, LayerUtility: PurgeVRAM V2, LoadImage, RH_Nano_Banana_Image2Image, RH_Sora2_I2V, RH_Translator, SaveImage, VHS_VideoCombine]
problems: []
missing: [CR Text Concatenate, LayerUtility: PurgeVRAM V2, Text Multiline]
members: [视频生成/图生视频/1971594660068192257.json, 视频生成/图生视频/1996087892659355650.json, 视频生成/图生视频/1996742691948044289.json, 视频生成/图生视频/1990982073487925249.json, 视频生成/图生视频/1985112947292852226.json, 视频生成/文生视频/1971594660068192257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_9

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1971594660068192257.json、视频生成/图生视频/1996087892659355650.json、视频生成/图生视频/1996742691948044289.json、视频生成/图生视频/1990982073487925249.json、视频生成/图生视频/1985112947292852226.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Text Concatenate`
- `GetVideoComponents`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `RH_Sora2_I2V`
- `RH_Translator`
- `SaveImage`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 5/6 个有
- `RHHiddenNodes` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `easy ifElse` —— 5/6 个有
- `ProcessString` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `ShellAgentPluginOutputText` —— 2/6 个有
- `easy promptLine` —— 2/6 个有
- `easy showAnything` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、LayerUtility: PurgeVRAM V2、Text Multiline
