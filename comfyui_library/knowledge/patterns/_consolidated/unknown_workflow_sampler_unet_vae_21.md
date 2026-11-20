---
name: unknown_workflow_sampler_unet_vae_21
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.860208
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3｜Larry 4步｜参考生视频_2098331637259001857.json, 视频生成/文生视频/MiniMax H3｜Larry 4步｜首尾帧_2098334091904118785.json, 视频生成/文生视频/MiniMax H3｜Larry 8步｜参考生视频_2098334052255363074.json, 视频生成/文生视频/MiniMax H3｜Larry 8步｜首尾帧_2098334066805395458.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜参考生视频_2098326332844363777.json, 视频生成/文生视频/MiniMax H3｜LightX2V 4步｜首尾帧视频_2098317959839174657.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜参考生视频_2098326323948244994.json, 视频生成/文生视频/MiniMax H3｜LightX2V 8步｜首尾帧视频_2098326342881333250.json, 视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json, 视频生成/文生视频/MiniMax H3｜Sol Attention｜首尾帧+参考生视频_2098331649598640129.json, 视频生成/文生视频/MiniMaxH3文生视频_2112906168044703746.json, 视频生成/文生视频/MiniMaxT2V 文生视频超强稳定动作_2084482575703302145.json, 视频生成/文生视频/Minimax H3 文生视频_2085256821585039362.json, 视频生成/文生视频/Minimax H3 文生视频_2089487806417694721.json, 视频生成/文生视频/Minimax H3-t2v 官方提示词文生视频_2085182661756276737.json, 视频生成/文生视频/Minimax H3-t2v 官方版文生视频_2084192379581583362.json, 视频生成/文生视频/Minimax H3视频模型文生视频_2084169698551361537.json, 视频生成/文生视频/Minimax H3高质量融合模型10Eros-图生视频BF16加速_2086859043209039874.json, 视频生成/文生视频/MinimaxT2V_2084151579204214786.json, 视频生成/文生视频/Minimax_h3_文生视频_2084276192676507650.json, 视频生成/文生视频/minimax_h3_文生_图生视频_2084261498850988033.json, 视频生成/文生视频/minimax_h3文生视频 图生视频 首尾帧+sage加速_2084126972392857602.json, 视频生成/文生视频/minimax_h3文生视频 图生视频 首尾帧+sage加速_2085982926470213634.json, 视频生成/文生视频/海螺H3首尾帧生视频_2087721274360553473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_21

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3｜Larry 4步｜参考生视频_2098331637259001857.json、视频生成/文生视频/MiniMax H3｜Larry 4步｜首尾帧_2098334091904118785.json、视频生成/文生视频/MiniMax H3｜Larry 8步｜参考生视频_2098334052255363074.json、视频生成/文生视频/MiniMax H3｜Larry 8步｜首尾帧_2098334066805395458.json、视频生成/文生视频/MiniMax H3｜LightX2V 4步｜参考生视频_2098326332844363777.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 20/24 个有
- `LoadImage` —— 16/24 个有
- `ComfyMathExpression` —— 14/24 个有
- `MiniMaxH3ImageToVideo` —— 14/24 个有
- `PrimitiveFloat` —— 14/24 个有
- `ResolutionSelector` —— 14/24 个有
- `MiniMaxH3AudioConditioningT8` —— 10/24 个有
- `PathchSageAttentionKJ` —— 9/24 个有
- `LoraLoaderModelOnly` —— 6/24 个有
- `EasyCache` —— 5/24 个有
- `ImageScaleToTotalPixels` —— 5/24 个有
- `MiniMaxH3SigmaShift` —— 5/24 个有
- `GetImageSize` —— 4/24 个有
- `MiniMaxH3TurboLoRA` —— 4/24 个有
- `MiniMaxH3TurboSampler` —— 4/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/24 个有
- `PrimitiveStringMultiline` —— 3/24 个有
- `BOOLConstant` —— 1/24 个有
- `EmptyImage` —— 1/24 个有
- `Fast Groups Bypasser (rgthree)` —— 1/24 个有
- `ImageResizeKJv2` —— 1/24 个有
- `MiniMaxH3BlockCacheT8` —— 1/24 个有
- `MiniMaxH3MemoryEfficientSolAttentionPatch` —— 1/24 个有
- `easy imageIndexSwitch` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
