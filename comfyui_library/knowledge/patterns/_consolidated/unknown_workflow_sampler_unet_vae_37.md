---
name: unknown_workflow_sampler_unet_vae_37
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.841929
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json, 视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json, 视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json, 视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json, 视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json, 视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json, 视频生成/图生视频/video_minimax_h3_i2v_2084124570839240705.json, 视频生成/图生视频/video_minimax_h3_i2v_2084181095406456833.json, 视频生成/图生视频/video_minimax_h3_i2v_2087451619603603457.json, 视频生成/图生视频/video_minimax_h3_i2v_RH_2096548199573049346.json, 视频生成/图生视频/video_minimax_h3_i2v_first_last_frame_2092171283260862466.json, 视频生成/图生视频/【2】图生视频（首帧图生视频）video_minimax_h3_i2v_2087199971459289090.json, 视频生成/图生视频/【3】图生视频（尾帧图生视频）video_minimax_h3_i2v_2087202435805827073.json, 视频生成/图生视频/【4】图生视频（首尾帧模式）video_minimax_h3_i2v_2087205422599073793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_37

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/minimax_h3图生视频_2084523818936262657.json、视频生成/图生视频/minimax_h3图生视频（稳定）_2085014325353340930.json、视频生成/图生视频/minimax_图生视频8步加速_2087371300875620353.json、视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json、视频生成/图生视频/minmaxh3图生视频_2109544409682497537.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/14 个有
- `PrimitiveFloat` —— 12/14 个有
- `CreateVideo` —— 11/14 个有
- `SaveVideo` —— 11/14 个有
- `ResolutionSelector` —— 10/14 个有
- `GetImageSize` —— 9/14 个有
- `ImageScaleToTotalPixels` —— 9/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/14 个有
- `Label (rgthree)` —— 4/14 个有
- `EasyCache` —— 3/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/14 个有
- `LayerUtility: PurgeVRAM V2` —— 3/14 个有
- `PrimitiveStringMultiline` —— 3/14 个有
- `VHS_VideoCombine` —— 3/14 个有
- `YK_LoadImageFromURL` —— 2/14 个有
- `easy int` —— 2/14 个有
- `easy showAnything` —— 2/14 个有
- `ImageScale` —— 1/14 个有
- `JjkText` —— 1/14 个有
- `PrimitiveInt` —— 1/14 个有
- `easy positive` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
