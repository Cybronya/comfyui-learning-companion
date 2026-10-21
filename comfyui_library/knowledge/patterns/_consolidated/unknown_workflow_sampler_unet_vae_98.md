---
name: unknown_workflow_sampler_unet_vae_98
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.76475
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3图生视频Org开源版_2084180933296607233.json, 视频生成/图生视频/MiniMax H3图生视频_2089703971740020737.json, 视频生成/图生视频/MiniMax H3图生视频工作流低显存加速版 开源 FL2VA_2084432209041252353.json, 视频生成/图生视频/MiniMax H3图生视频（Sage加速）2608_2085826329311801346.json, 视频生成/图生视频/MiniMax H3首尾帧视频工作流低显存加速版 开源 FL2VA_2084428374197497858.json, 视频生成/图生视频/Minimax H3 I2v_首尾帧 (加速版，去动态噪点）_2084495129297121281.json, 视频生成/图生视频/Minimax H3 图生视频_首尾帧 (加速版，去高动态噪点）_2088505534927433729.json, 视频生成/图生视频/Minimax+H3+I2v_首尾帧+(加速版，去动态噪点）_2089185922914021377.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_98

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频Org开源版_2084180933296607233.json、视频生成/图生视频/MiniMax H3图生视频_2089703971740020737.json、视频生成/图生视频/MiniMax H3图生视频工作流低显存加速版 开源 FL2VA_2084432209041252353.json、视频生成/图生视频/MiniMax H3图生视频（Sage加速）2608_2085826329311801346.json、视频生成/图生视频/MiniMax H3首尾帧视频工作流低显存加速版 开源 FL2VA_2084428374197497858.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `SaveVideo` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `GetImageSize` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `EasyCache` —— 3/8 个有
- `ImageScale` —— 3/8 个有
- `LayerUtility: TextBox` —— 3/8 个有
- `Label (rgthree)` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `VHS_VideoCombine` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `FlashVSRInitPipe` —— 1/8 个有
- `FlashVSRNodeAdv` —— 1/8 个有
- `H3SigmaRefiner` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `SolAttnPatch` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
