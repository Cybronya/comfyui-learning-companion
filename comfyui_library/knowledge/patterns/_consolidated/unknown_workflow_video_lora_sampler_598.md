---
name: unknown_workflow_video_lora_sampler_598
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.638
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, ComfyMathExpression, GetImageSize, GetNode, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 视频图片参考vfx edit Lora 流 taomate加速_2111436148177457153.json, 视频生成/图生视频/H3 视频图片参考换脸Lora 流 taomate加速_2111425514496937985.json, 视频生成/图生视频/H3+视频角色替换+Lora+真实人物加速流_2111443719965732865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_598

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/H3 视频图片参考vfx edit Lora 流 taomate加速_2111436148177457153.json、视频生成/图生视频/H3 视频图片参考换脸Lora 流 taomate加速_2111425514496937985.json、视频生成/图生视频/H3+视频角色替换+Lora+真实人物加速流_2111443719965732865.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `VHS_LoadVideoFFmpeg` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
