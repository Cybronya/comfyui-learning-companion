---
name: unknown_workflow_sampler_unet_vae_65
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8685
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_h3_超级加速图生视频_2084162376542281729.json, 视频生成/图生视频/Minimax_h3_超级加速首尾帧图生视频_2084842867264155649.json, 视频生成/图生视频/video_minimax_h3_i2v_2084181095406456833.json, 视频生成/图生视频/video_minimax_h3_i2v_RH_2096548199573049346.json, 视频生成/图生视频/【2】图生视频（首帧图生视频）video_minimax_h3_i2v_2087199971459289090.json, 视频生成/图生视频/【3】图生视频（尾帧图生视频）video_minimax_h3_i2v_2087202435805827073.json, 视频生成/图生视频/【4】图生视频（首尾帧模式）video_minimax_h3_i2v_2087205422599073793.json, 视频生成/文生视频/MiniMax H3 加速版 图生视频 首尾帧生视频_2086653248143978497.json, 视频生成/文生视频/Minimax_h3_超级加速文生视频_2084160987023896578.json, 视频生成/文生视频/首尾帧生视频+_2084526811551195138.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_65

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax_h3_超级加速图生视频_2084162376542281729.json、视频生成/图生视频/Minimax_h3_超级加速首尾帧图生视频_2084842867264155649.json、视频生成/图生视频/video_minimax_h3_i2v_2084181095406456833.json、视频生成/图生视频/video_minimax_h3_i2v_RH_2096548199573049346.json、视频生成/图生视频/【2】图生视频（首帧图生视频）video_minimax_h3_i2v_2087199971459289090.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 9/10 个有
- `ImageScaleToTotalPixels` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `ComfyMathExpression` —— 8/10 个有
- `PrimitiveFloat` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `CreateVideo` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `SaveVideo` —— 6/10 个有
- `CR Text` —— 4/10 个有
- `Label (rgthree)` —— 4/10 个有
- `VHS_VideoCombine` —— 4/10 个有
- `EasyCache` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 3/10 个有
- `PainterVRAM` —— 3/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `INTConstant` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
