---
name: unknown_workflow_video_lora_sampler_405
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.589286
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, ComfyMathExpression, GetImageSize, GetNode, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/H3+视频角色替换+Lora+真实人物加速流_2114202871649628161.json, 图片生成/图生图/H3+视频角色替换+Lora+真实人物加速流_2115257366215221249.json, 平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2113663378064498689.json, 平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2114924144327479298.json, 视频生成/图生视频/H3 视频图片参考vfx edit Lora 流 taomate加速_2111436148177457153.json, 视频生成/图生视频/H3 视频图片参考换脸Lora 流 taomate加速_2111425514496937985.json, 视频生成/图生视频/H3+视频角色替换+Lora+真实人物加速流_2111443719965732865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_405

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/H3+视频角色替换+Lora+真实人物加速流_2114202871649628161.json、图片生成/图生图/H3+视频角色替换+Lora+真实人物加速流_2115257366215221249.json、平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2113663378064498689.json、平台全量/MiniMax H3+character_swap lora-视频角色替换+字节4步加速lora_2114924144327479298.json、视频生成/图生视频/H3 视频图片参考vfx edit Lora 流 taomate加速_2111436148177457153.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoadImage` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `Text` —— 2/7 个有
- `孤海注释` —— 2/7 个有
- `AnyBooleanSwitch` —— 1/7 个有
- `CR Font File List` —— 1/7 个有
- `CompressImages` —— 1/7 个有
- `ImpactConditionalBranch` —— 1/7 个有
- `LoadFolderFromDir` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `VHS_LoadVideoFFmpeg` —— 1/7 个有
- `VHS_SelectFilename` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
