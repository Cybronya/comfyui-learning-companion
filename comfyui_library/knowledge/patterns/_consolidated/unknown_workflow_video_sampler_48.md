---
name: unknown_workflow_video_sampler_48
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [MMAudioFeatureUtilsLoader, MMAudioModelLoader, MMAudioSampler, NormalizeAudioLoudness, RIFEInterpolation, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [音频生成/音频生成/视频配音MMAudio视频加声_2041821972585254914.json, 音频生成/音频生成/视频配音MMAudio视频加声_2042033748270649345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_48

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/视频配音MMAudio视频加声_2041821972585254914.json、音频生成/音频生成/视频配音MMAudio视频加声_2042033748270649345.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `MMAudioSampler`
- `NormalizeAudioLoudness`
- `RIFEInterpolation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
