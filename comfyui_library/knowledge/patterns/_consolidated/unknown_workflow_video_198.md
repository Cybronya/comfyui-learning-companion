---
name: unknown_workflow_video_198
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [HunyuanVideoFoley, ImageFromBatch, PreviewAudio, RH_Captioner, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/Hunyuan Foley视频配音_1963195011397554177.json, 平台全量/混元Foley视频配音效工作流_1963144315331645441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_198

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Hunyuan Foley视频配音_1963195011397554177.json、平台全量/混元Foley视频配音效工作流_1963144315331645441.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `HunyuanVideoFoley`
- `ImageFromBatch`
- `PreviewAudio`
- `RH_Captioner`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
