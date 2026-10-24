---
name: unknown_workflow_sampler_unet_vae_179
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.785833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3图生视频&首尾帧 量化加速版_2084545071873093633.json, 视频生成/图生视频/Minimax_H3_单张参考图生视频标准版_2102317605854990338.json, 视频生成/图生视频/Minimax_H3_首尾帧图生视频标准版_2104053564233568257.json, 视频生成/图生视频/minimax_h3_i2v_accel_2096897727664836609.json, 视频生成/图生视频/minimax_h3_图生视频_牛来_2094972668582916098.json, 视频生成/图生视频/海螺H3八步极速生成文图首尾帧视频3合一工作流_2088515866974576641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_179

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3图生视频&首尾帧 量化加速版_2084545071873093633.json、视频生成/图生视频/Minimax_H3_单张参考图生视频标准版_2102317605854990338.json、视频生成/图生视频/Minimax_H3_首尾帧图生视频标准版_2104053564233568257.json、视频生成/图生视频/minimax_h3_i2v_accel_2096897727664836609.json、视频生成/图生视频/minimax_h3_图生视频_牛来_2094972668582916098.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ComfySwitchNode` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `EmptyImage` —— 3/6 个有
- `ResolutionSelector` —— 3/6 个有
- `AnyBooleanSwitch` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `CM_BoolBinaryOperation` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `Float` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ImpactConditionalBranch` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `Switch image [Crystools]` —— 1/6 个有
- `easy float` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
