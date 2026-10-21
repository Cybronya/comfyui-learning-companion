---
name: unknown_workflow_video_lora_sampler_300
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.713143
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 视频图片参考vfx edit Lora 流 taomate加速_2111436148177457153.json, 视频生成/图生视频/H3 视频图片参考换脸Lora 流 taomate加速_2111425514496937985.json, 视频生成/图生视频/H3+视频角色替换+Lora+真实人物加速流_2111443719965732865.json, 视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json, 视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json, 视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json, 视频生成/文生视频/MiniMaxH3+多合一稳定MAX｜4步8步加速（自用）_2092482860316971010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_300

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3 视频图片参考vfx edit Lora 流 taomate加速_2111436148177457153.json、视频生成/图生视频/H3 视频图片参考换脸Lora 流 taomate加速_2111425514496937985.json、视频生成/图生视频/H3+视频角色替换+Lora+真实人物加速流_2111443719965732865.json、视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json、视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `BasicGuider` —— 4/7 个有
- `LoadAudio` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `VAEDecodeAudio` —— 4/7 个有
- `CFGGuider` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `LTXVSeparateAVLatent` —— 3/7 个有
- `MiniMaxH3AddGuide` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LazySwitchKJ` —— 1/7 个有
- `MiniMaxH3ImageToVideo` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `VHS_LoadVideoFFmpeg` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
