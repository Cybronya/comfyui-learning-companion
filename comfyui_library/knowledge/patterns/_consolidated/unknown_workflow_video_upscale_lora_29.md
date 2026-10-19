---
name: unknown_workflow_video_upscale_lora_29
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7695
common_nodes: [CLIPLoader, CR Load LoRA, ComfyMiniMaxH3Director, CustomCombo, LoraLoaderModelOnly, MiniMaxH3DirectorRefine, MiniMaxH3MemoryEfficientSageAttentionPatch, PreviewAny, StringToNumber, TextSwitchCase, UNETLoader, UpscaleModelLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 导演台全能工作流-ref2va-全能参考_2110567905564909569.json, 视频生成/图生视频/MiniMax H3 导演台全能工作流-图生视频-人物去油_2110348948257988609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 导演台全能工作流-ref2va-全能参考_2110567905564909569.json、视频生成/图生视频/MiniMax H3 导演台全能工作流-图生视频-人物去油_2110348948257988609.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Load LoRA`
- `ComfyMiniMaxH3Director`
- `CustomCombo`
- `LoraLoaderModelOnly`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PreviewAny`
- `StringToNumber`
- `TextSwitchCase`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAELoader`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
