---
name: unknown_workflow_sampler_unet_vae_26
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.852056
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json, 视频生成/图生视频/MiniMax-H3 Fl2va 首尾帧生视频标准版_2095499784147791873.json, 视频生成/图生视频/MiniMax-H3 图生视频（首尾帧）_2084150513402204161.json, 视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json, 视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2085948478043283457.json, 视频生成/图生视频/MiniMax-H3-首尾帧视频_2084274212876939265.json, 视频生成/图生视频/MiniMax-H3全能参考工作流_2084872705010130945.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2084237228296986625.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2084248036343115777.json, 视频生成/图生视频/MiniMax-H3开源版 图生视频 加速版_2093286738599960577.json, 视频生成/图生视频/MiniMax-H3开源版 多图参考生视频 短剧生成_2084629247259406338.json, 视频生成/图生视频/MiniMax-H3开源版 多图参考生视频_2084595722531459073.json, 视频生成/图生视频/MiniMaxH3+ EasyCache提速_2084489591494631425.json, 视频生成/图生视频/Minimax H3 图生视频工作流｜AI海报动画生成｜最强免费开源视频模型_2089969033876692993.json, 视频生成/图生视频/Minimax H3 多参视频生成_2089987673200091137.json, 视频生成/文生视频/MiniMax-H3全能参考工作流-金水1987_2084528401230159874.json, 视频生成/文生视频/Minimax H3 全系列工作流【AI小王子】_2084162640192032770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_26

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json、视频生成/图生视频/MiniMax-H3 Fl2va 首尾帧生视频标准版_2095499784147791873.json、视频生成/图生视频/MiniMax-H3 图生视频（首尾帧）_2084150513402204161.json、视频生成/图生视频/MiniMax-H3-图生视频_2084259365334372354.json、视频生成/图生视频/MiniMax-H3-图生视频（4步生视频超级加速）_2085221255543877633.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 11/18 个有
- `PrimitiveStringMultiline` —— 10/18 个有
- `MiniMaxH3ImageToVideo` —— 8/18 个有
- `GetImageSize` —— 5/18 个有
- `ImageScaleToTotalPixels` —— 5/18 个有
- `EasyCache` —— 4/18 个有
- `Fast Groups Bypasser (rgthree)` —— 4/18 个有
- `LoraLoaderModelOnly` —— 4/18 个有
- `PathchSageAttentionKJ` —— 4/18 个有
- `LoadAudio` —— 2/18 个有
- `ModelPatchTorchSettings` —— 2/18 个有
- `Bjornulf_ShowInt` —— 1/18 个有
- `ImpactConditionalBranch` —— 1/18 个有
- `RH_Captioner` —— 1/18 个有
- `StringConcatenate` —— 1/18 个有
- `VHS_LoadVideo` —— 1/18 个有
- `easy boolean` —— 1/18 个有
- `ttN int` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
