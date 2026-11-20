---
name: unknown_workflow_video_196
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/GIMM-VFI视频增强流程_1948748090526900226.json, 平台全量/视频更顺滑！GIMM视频补帧，16帧补到60帧_1978344939014774786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_196

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/GIMM-VFI视频增强流程_1948748090526900226.json、平台全量/视频更顺滑！GIMM视频补帧，16帧补到60帧_1978344939014774786.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageSmartSharpen+` —— 1/2 个有
- `Video_Upscale_With_Model` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
