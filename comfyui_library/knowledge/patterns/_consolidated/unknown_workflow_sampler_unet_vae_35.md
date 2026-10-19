---
name: unknown_workflow_sampler_unet_vae_35
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.720643
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2102924951413153793.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2103672100170067969.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2104844242353999874.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 参考生视频_2108491242530234370.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 首尾帧_2108488300557328386.json, 视频生成/图生视频/Minimax H3 单张参考图生视频标准版_2102224374689517569.json, 视频生成/图生视频/Minimax H3 参考图和参考视音频生成视频满血版_2105625287546462210.json, 视频生成/图生视频/Minimax H3 首尾帧图生视频标准版_2102237236300435457.json, 视频生成/图生视频/Minimax_H3_单张参考图生视频标准版_2102317605854990338.json, 视频生成/图生视频/Minimax_H3_首尾帧图生视频标准版_2104053564233568257.json, 视频生成/图生视频/Minimax图生视频I2V_2099170083997315073.json, 视频生成/图生视频/Minmax多参考生成视频R2V_2084668436755599362.json, 视频生成/文生视频/Minimax文生视频T2V_2098449873984122882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_35

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_全参考ref2va_中文版_2085180698285142017.json、视频生成/图生视频/MiniMax_H3_参考生视频_2102924951413153793.json、视频生成/图生视频/MiniMax_H3_参考生视频_2103672100170067969.json、视频生成/图生视频/MiniMax_H3_参考生视频_2104844242353999874.json、视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 参考生视频_2108491242530234370.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 13/14 个有
- `LoadImage` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `PrimitiveBoolean` —— 13/14 个有
- `PrimitiveInt` —— 13/14 个有
- `ResolutionSelector` —— 10/14 个有
- `LoadAudio` —— 8/14 个有
- `PrimitiveStringMultiline` —— 8/14 个有
- `MiniMaxH3ImageToVideo` —— 7/14 个有
- `MiniMaxH3ReferenceToVideo` —— 7/14 个有
- `GetImageSize` —— 5/14 个有
- `ImageScaleToTotalPixels` —— 5/14 个有
- `AudioCrop` —— 3/14 个有
- `GetNode` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `easy minimaxH3AudioLock` —— 3/14 个有
- `EmptyImage` —— 2/14 个有
- `GetVideoComponents` —— 2/14 个有
- `LoadVideo` —— 2/14 个有
- `PreviewImage` —— 2/14 个有
- `VHS_LoadVideo` —— 2/14 个有
- `VedaSparseAttention` —— 2/14 个有
- `ImageUpscaleWithModel` —— 1/14 个有
- `LTXVSeparateAVLatent` —— 1/14 个有
- `SaveLatent` —— 1/14 个有
- `UpscaleModelLoader` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
