---
name: unknown_workflow_sampler_unet_vae_27
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.863353
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax - T2V_2087875413392580609.json, 数字人/数字人/h3_i2v_int8_35秒直播预生成_2111256612936704002.json, 数字人/数字人/首尾帧逻辑_2087967441874931713.json, 视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084195676602331137.json, 视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084745751497895937.json, 视频生成/图生视频/(量化加速版)Minimax多参生视频V1_2084238539549663234.json, 视频生成/图生视频/0812日Minimax H3 ref2va加速工作流_2087422773068128257.json, 视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json, 视频生成/图生视频/H3_单采极速文戏_2106860537857527810.json, 视频生成/图生视频/H3_单采极速文戏_2109821779844886530.json, 视频生成/图生视频/H3官流（单采极速文戏）_2113998368463740930.json, 视频生成/图生视频/H3官流（终极版）231_2108222613133811714.json, 视频生成/图生视频/H3高清快速出视频_2105232331433930754.json, 视频生成/图生视频/api横屏640p坤坤H3官流无lora12步_2114189872008351746.json, 视频生成/图生视频/api竖屏768pH3官流_2110570859592249346.json, 视频生成/图生视频/api竖屏768pH3官流_2111012386319724545.json, 视频生成/图生视频/自用H3官流（单采极速文戏）_2108455375656804353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_27

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/MiniMax - T2V_2087875413392580609.json、数字人/数字人/h3_i2v_int8_35秒直播预生成_2111256612936704002.json、数字人/数字人/首尾帧逻辑_2087967441874931713.json、视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084195676602331137.json、视频生成/图生视频/(二倍速！量化加速版)Minimax多参生视频_2084745751497895937.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 16/17 个有
- `LoadImage` —— 16/17 个有
- `PrimitiveFloat` —— 16/17 个有
- `PrimitiveStringMultiline` —— 16/17 个有
- `VAEDecodeAudio` —— 16/17 个有
- `MiniMaxH3ReferenceToVideo` —— 13/17 个有
- `VHS_VideoCombine` —— 12/17 个有
- `LoraLoaderModelOnly` —— 11/17 个有
- `ModelAttentionBackend` —— 11/17 个有
- `BlockSparseAttention` —— 10/17 个有
- `ModelPreviewOverrideKJ` —— 9/17 个有
- `LoadAudio` —— 8/17 个有
- `MiniMaxH3SigmaShift` —— 8/17 个有
- `VHS_LoadVideo` —— 6/17 个有
- `CreateVideo` —— 5/17 个有
- `ExtendIntermediateSigmas` —— 5/17 个有
- `ManualSigmas` —— 5/17 个有
- `SaveVideo` —— 5/17 个有
- `MiniMaxH3ImageToVideo` —— 4/17 个有
- `PreviewAny` —— 4/17 个有
- `EmptyImage` —— 2/17 个有
- `HAIGC_SaveImagesToZip` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `BetaSamplingScheduler` —— 1/17 个有
- `H3SLAAttention` —— 1/17 个有
- `PathchSageAttentionKJ` —— 1/17 个有
- `Power Lora Loader (rgthree)` —— 1/17 个有
- `SoundFlow_GetLength` —— 1/17 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
