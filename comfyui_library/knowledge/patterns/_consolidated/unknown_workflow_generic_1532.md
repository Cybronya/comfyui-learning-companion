---
name: unknown_workflow_generic_1532
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7445
common_nodes: [CR Prompt Text, JjkText, LoadImage, PreviewAny, RH_Grok_Video3, RH_Sora2_I2V, RH_Sora2_I2V_PRO, RH_Veo3_Image2Video, SaveVideo, ShellAgentPluginOutputText, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/4.视频生成_2031763163913392130.json, 视频生成/文生视频/AI动画 VIDEO - Workflow V1.0_2028430413558976513.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1532

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/4.视频生成_2031763163913392130.json、视频生成/文生视频/AI动画 VIDEO - Workflow V1.0_2028430413558976513.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `JjkText`
- `LoadImage`
- `PreviewAny`
- `RH_Grok_Video3`
- `RH_Sora2_I2V`
- `RH_Sora2_I2V_PRO`
- `RH_Veo3_Image2Video`
- `SaveVideo`
- `ShellAgentPluginOutputText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Sora2_I2V_Realistic` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
