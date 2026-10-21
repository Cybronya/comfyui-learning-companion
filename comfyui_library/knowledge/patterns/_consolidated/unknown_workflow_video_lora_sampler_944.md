---
name: unknown_workflow_video_lora_sampler_944
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8635
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveStringMultiline, RandomNoise, SFH3MultimodalDirector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜多模态参考导演台｜ 宫格分镜自动拆分+全能参考（图片｜视频｜音频）_2096977007417585666.json, 视频生成/文生视频/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2085626169877155842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_944

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜多模态参考导演台｜ 宫格分镜自动拆分+全能参考（图片｜视频｜音频）_2096977007417585666.json、视频生成/文生视频/万象AI+Minimax_h3_导演台插件3.0+4步lora加速版（批量短剧专用）_2085626169877155842.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SFH3MultimodalDirector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImpactFloat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
