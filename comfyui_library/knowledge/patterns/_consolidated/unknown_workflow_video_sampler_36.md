---
name: unknown_workflow_video_sampler_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.913
common_nodes: [LayerUtility: PurgeVRAM V2, LoadImage, MMAudioFeatureUtilsLoader, MMAudioModelLoader, MMAudioSampler, SaveAudio, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [音频生成/音频生成/MMaudio视频配音_1948634677694332930.json, 音频生成/音频生成/视频自动配对音效【Woosh+Qwen3】_2043733828946108418.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/MMaudio视频配音_1948634677694332930.json、音频生成/音频生成/视频自动配对音效【Woosh+Qwen3】_2043733828946108418.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `MMAudioSampler`
- `SaveAudio`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
