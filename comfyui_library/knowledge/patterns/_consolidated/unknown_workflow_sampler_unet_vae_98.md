---
name: unknown_workflow_sampler_unet_vae_98
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.836
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3图生视频Org开源版_2084180933296607233.json, 视频生成/图生视频/MiniMax H3图生视频_2089703971740020737.json, 视频生成/图生视频/MiniMax H3图生视频工作流低显存加速版 开源 FL2VA_2084432209041252353.json, 视频生成/图生视频/MiniMax H3图生视频（Sage加速）2608_2085826329311801346.json, 视频生成/图生视频/MiniMax H3首尾帧视频工作流低显存加速版 开源 FL2VA_2084428374197497858.json, 视频生成/图生视频/Minimax-H3-单_双图生视频-sage+cache双重提速-平均3分半钟出5秒！_2084572403178500098.json, 视频生成/图生视频/video_minimax_h3_i2v_2084124570839240705.json, 视频生成/文生视频/MiniMax H3图生视频工作流_2084631760146620417.json, 视频生成/文生视频/MiniMax H3文生视频（Sage加速）2608_2085826303927869442.json, 视频生成/文生视频/minimax-h3 -标准官方工作流（文生_首尾帧生视频）_2094754298751180802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_98

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频Org开源版_2084180933296607233.json、视频生成/图生视频/MiniMax H3图生视频_2089703971740020737.json、视频生成/图生视频/MiniMax H3图生视频工作流低显存加速版 开源 FL2VA_2084432209041252353.json、视频生成/图生视频/MiniMax H3图生视频（Sage加速）2608_2085826329311801346.json、视频生成/图生视频/MiniMax H3首尾帧视频工作流低显存加速版 开源 FL2VA_2084428374197497858.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `SaveVideo` —— 9/10 个有
- `PathchSageAttentionKJ` —— 7/10 个有
- `CR Prompt Text` —— 5/10 个有
- `ImageScaleToTotalPixels` —— 5/10 个有
- `EasyCache` —— 4/10 个有
- `GetImageSize` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `FlashVSRInitPipe` —— 2/10 个有
- `FlashVSRNodeAdv` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `SolAttnPatch` —— 2/10 个有
- `PrimitiveInt` —— 1/10 个有
- `SpectrumSDXL` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
