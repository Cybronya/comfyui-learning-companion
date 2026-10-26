---
name: unknown_workflow_video_upscale_latent_upscale_87
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89875
common_nodes: [AnyBooleanSwitch, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MinimaxH3LatentUpscaler3D, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/海螺H3 极速6分钟生成1.5M 10秒视频-标准模式-文图首尾帧视频3合一工作流_2084510220184809474.json, 图片生成/图生图/海螺H3_极速6分钟生成1.5M_10秒视频-标准模式-全能参考生视频_2114641161150353410.json, 视频生成/文生视频/H3全能参考生视频-练习模式_2092890005231464450.json, 视频生成/文生视频/海螺H3 极速6分钟生成1.5M 10秒视频-标准模式-全能参考生视频_2084582921754730497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_87

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/海螺H3 极速6分钟生成1.5M 10秒视频-标准模式-文图首尾帧视频3合一工作流_2084510220184809474.json、图片生成/图生图/海螺H3_极速6分钟生成1.5M_10秒视频-标准模式-全能参考生视频_2114641161150353410.json、视频生成/文生视频/H3全能参考生视频-练习模式_2092890005231464450.json、视频生成/文生视频/海螺H3 极速6分钟生成1.5M 10秒视频-标准模式-全能参考生视频_2084582921754730497.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `AnyBooleanSwitch`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MinimaxH3LatentUpscaler3D`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
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
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `MiniMaxChunkFeedForward` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `MiniMaxLowVRAMAttention` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `ResizeImagesByShorterEdge` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `easy imageIndexSwitch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
