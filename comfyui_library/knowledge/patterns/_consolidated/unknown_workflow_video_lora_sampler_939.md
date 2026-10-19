---
name: unknown_workflow_video_lora_sampler_939
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9835
common_nodes: [BasicGuider, CreateVideo, GetImageRangeFromBatch, ImageResizeKJv2, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, RandomNoise, SamplerCustomAdvanced, VHS_LoadVideo, VHS_VideoCombine, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3-4步极速工作流（手动填写提示词版）_2085573024950087681.json, 视频生成/文生视频/Minimax_h3_多参生视频+手动@插件+light2V加速lora0.1版本_2085874663896477697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_939

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3-4步极速工作流（手动填写提示词版）_2085573024950087681.json、视频生成/文生视频/Minimax_h3_多参生视频+手动@插件+light2V加速lora0.1版本_2085874663896477697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CreateVideo`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `UniBlockSwap` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
