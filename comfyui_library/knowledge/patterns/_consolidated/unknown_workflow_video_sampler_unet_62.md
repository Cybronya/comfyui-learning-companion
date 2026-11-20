---
name: unknown_workflow_video_sampler_unet_62
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.822571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax-H3-i2v_2084853035779584002.json, 视频生成/图生视频/海螺H3全能多参音视频生成（9图3视频3音频）开源加速版_2086595985899347970.json, 视频生成/文生视频/video_minimax_h3_r2v_fast_2094242970009694209.json, 视频生成/文生视频/海螺H3(minimaxH3)全能参考生视频2K开源版（9图3视频3音频）_2084577541385445377.json, 视频生成/文生视频/海螺H3【多参视频工作流】【万能提示词模板】_2084446461143638017.json, 视频生成/文生视频/海螺H3全能多参音视频生成开源版（9图3视频3音频）_2084825306258558977.json, 视频生成/文生视频/海螺H3全能多参音视频生成（9图3视频3音频）开源加速版_2085264471232180225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_62

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/minimax-H3-i2v_2084853035779584002.json、视频生成/图生视频/海螺H3全能多参音视频生成（9图3视频3音频）开源加速版_2086595985899347970.json、视频生成/文生视频/video_minimax_h3_r2v_fast_2094242970009694209.json、视频生成/文生视频/海螺H3(minimaxH3)全能参考生视频2K开源版（9图3视频3音频）_2084577541385445377.json、视频生成/文生视频/海螺H3【多参视频工作流】【万能提示词模板】_2084446461143638017.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 6/7 个有
- `EasyCache` —— 5/7 个有
- `LoadAudio` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `SolAttnPatch` —— 4/7 个有
- `PainterVRAM` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `LoadAudioUI` —— 1/7 个有
- `RIFEInterpolation` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
