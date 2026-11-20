---
name: unknown_workflow_video_224
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8195
common_nodes: [ASRMW, HAIGC_VideoSubtitleTimestampPro, PreviewAny, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource]
problems: []
missing: []
members: [平台全量/智能字幕生成：精准对齐语音节奏，智能优化视觉呈现_1996813372798771202.json, 平台全量/视频字幕自动生成 精准对齐语音节奏_2058452510372880386.json]
source: knowledge_consolidation
---

# unknown_workflow_video_224

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/智能字幕生成：精准对齐语音节奏，智能优化视觉呈现_1996813372798771202.json、平台全量/视频字幕自动生成 精准对齐语音节奏_2058452510372880386.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `ASRMW`
- `HAIGC_VideoSubtitleTimestampPro`
- `PreviewAny`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/2 个有
- `Fast Actions Button (rgthree)` —— 1/2 个有
- `Fast Muter (rgthree)` —— 1/2 个有
- `PurgeVRAM_UTK` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
