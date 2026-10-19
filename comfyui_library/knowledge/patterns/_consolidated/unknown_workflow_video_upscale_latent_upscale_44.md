---
name: unknown_workflow_video_upscale_latent_upscale_44
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.4907
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy float, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/双倍高清放大MiniMax H3-多参考生视频-字节DMAD加速版_2106606807736209409.json, 视频生成/图生视频/测试01剧本 YZ金鱼-MiniMax H3-多参考生视频-优化版_2107313229809672193.json, 视频生成/图生视频/进阶版！MiniMax H3 Ref2VA 多参生视频工作流_2102256455968710658.json, 视频生成/图生视频/金鱼-多参考生视频-电影感_2094788063007432706.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频_2097875587942666242.json, 视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频多比例版本_2104119164674859010.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2096460541328973825.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2097340280092581890.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒竖屏960分辨率）_2096477149321580546.json, 视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_44

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/双倍高清放大MiniMax H3-多参考生视频-字节DMAD加速版_2106606807736209409.json、视频生成/图生视频/测试01剧本 YZ金鱼-MiniMax H3-多参考生视频-优化版_2107313229809672193.json、视频生成/图生视频/进阶版！MiniMax H3 Ref2VA 多参生视频工作流_2102256455968710658.json、视频生成/图生视频/金鱼-多参考生视频-电影感_2094788063007432706.json、视频生成/图生视频/（最强一致性Singularity）Minimax H3多参考双采生视频_2097875587942666242.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy float`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/10 个有
- `Lora Loader Stack (rgthree)` —— 6/10 个有
- `ModelAttentionBackend` —— 6/10 个有
- `SolAttnMiniMax` —— 6/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `Label (rgthree)` —— 3/10 个有
- `Astra` —— 1/10 个有
- `ImageFromBatch` —— 1/10 个有
- `Int` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MiniMaxH3AVDecodeT8` —— 1/10 个有
- `SaveVideo` —— 1/10 个有
- `easy int` —— 1/10 个有
- `easy showAnything` —— 1/10 个有
- `孤海注释` —— 1/10 个有
- `获取视频信息` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
