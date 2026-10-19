---
name: unknown_workflow_video_sampler_unet_65
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8035
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/VOSR2图像高清化_快速H3-04-i2v_一条龙_2099518036637208578.json, 视频生成/图生视频/h3-图生视频-加速版_2086591917021810690.json, 视频生成/图生视频/h3-文生视频-加速版_2089908211922067457.json, 视频生成/图生视频/h3-首尾帧-加速版_2086593854702182401.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_65

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/VOSR2图像高清化_快速H3-04-i2v_一条龙_2099518036637208578.json、视频生成/图生视频/h3-图生视频-加速版_2086591917021810690.json、视频生成/图生视频/h3-文生视频-加速版_2089908211922067457.json、视频生成/图生视频/h3-首尾帧-加速版_2086593854702182401.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 3/4 个有
- `LoraLoaderBypassModelOnly` —— 3/4 个有
- `Sleep` —— 3/4 个有
- `EasyCache` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `SLAAttention` —— 1/4 个有
- `SolAttnPatch` —— 1/4 个有
- `VOSR2ModelLoader` —— 1/4 个有
- `VOSR2Upscale` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
