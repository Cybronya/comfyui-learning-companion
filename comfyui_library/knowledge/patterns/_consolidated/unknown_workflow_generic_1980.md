---
name: unknown_workflow_generic_1980
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.864
common_nodes: [CM_FloatToInt, CM_FloatUnaryOperation, CM_IntToFloat, FL_ImageBatchToGrid, GetImageSizeAndCount, GetVideoComponents, ImageFromBatch+, LoadVideo, PreviewAny, PreviewImage, RunningHub OmniShotCut Detector, RunningHub OmniShotCut Loader, RunningHub OmniShotCut SaveJson, RunningHub OmniShotCut ShotCount, RunningHub OmniShotCut VideoSplitter, SaveImage, SaveVideo, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-分割视频(包含音频)-OmniShotCut_2055203665241231362.json, 平台全量/视频-分割视频(包含音频)-OmniShotCut_2066055881797988352.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1980

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频-分割视频(包含音频)-OmniShotCut_2055203665241231362.json、平台全量/视频-分割视频(包含音频)-OmniShotCut_2066055881797988352.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CM_FloatToInt`
- `CM_FloatUnaryOperation`
- `CM_IntToFloat`
- `FL_ImageBatchToGrid`
- `GetImageSizeAndCount`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LoadVideo`
- `PreviewAny`
- `PreviewImage`
- `RunningHub OmniShotCut Detector`
- `RunningHub OmniShotCut Loader`
- `RunningHub OmniShotCut SaveJson`
- `RunningHub OmniShotCut ShotCount`
- `RunningHub OmniShotCut VideoSplitter`
- `SaveImage`
- `SaveVideo`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
