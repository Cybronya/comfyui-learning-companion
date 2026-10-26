---
name: unknown_workflow_sampler_unet_vae_40
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.510933
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/VividMuse_MiniMax_H3_多参生视频_2084280381586628609.json, 图片生成/图生图/fastH3_ref2va_2112720537771397122.json, 图片生成/图生图/trim fast minimax_2107875369050267650.json, 数字人/数字人/7度工作流改版1_2098964914600763393.json, 视频生成/图生视频/H3最强单采V2【33步雷霆祭祀版】_2110602244931543042.json, 视频生成/图生视频/H3最强单采V2【33步雷霆祭祀版】_2113794769800491010.json, 视频生成/图生视频/H3最强单采V2【33步雷霆祭祀版】_2113805410691010562.json, 视频生成/图生视频/H3最强单采V2【动作迁移角色替换】_2111377785766899713.json, 视频生成/图生视频/H3爆裂冲击帧之【复仇之刃】_2113928730816106498.json, 视频生成/图生视频/MiniMax H3 全能参考｜真实电影质感V2_2113930456193396737.json, 视频生成/图生视频/MiniMax H3 全能参考｜真实电影质感V2【正式版】_2112677636630728705.json, 视频生成/图生视频/MiniMax H3_语义增强_2114043850519040002.json, 视频生成/图生视频/MiniMax_H3双采全能工作流V3-语义桥-文戏不油，武戏动态强-参考生视频-长视频-视频复刻-高清直出_2113557786440327170.json, 视频生成/图生视频/⭐️H3无损融合单采【官方满血API画布级本地流】_2113920580289384450.json, 视频生成/图生视频/【最强单采】双重显存优化1.0画质30秒直出流！_2113599252554407938.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_40

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/VividMuse_MiniMax_H3_多参生视频_2084280381586628609.json、图片生成/图生图/fastH3_ref2va_2112720537771397122.json、图片生成/图生图/trim fast minimax_2107875369050267650.json、数字人/数字人/7度工作流改版1_2098964914600763393.json、视频生成/图生视频/H3最强单采V2【33步雷霆祭祀版】_2110602244931543042.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 14/15 个有
- `PrimitiveStringMultiline` —— 14/15 个有
- `ResolutionSelector` —— 14/15 个有
- `BlockSparseAttention` —— 13/15 个有
- `GetNode` —— 13/15 个有
- `ModelAttentionBackend` —— 13/15 个有
- `SetNode` —— 13/15 个有
- `LoadAudio` —— 12/15 个有
- `VHS_VideoCombine` —— 12/15 个有
- `忽略多组孤海` —— 12/15 个有
- `BasicScheduler` —— 11/15 个有
- `ModelPreviewOverrideKJ` —— 11/15 个有
- `VHS_LoadVideo` —— 11/15 个有
- `ManualSigmas` —— 7/15 个有
- `LoraLoaderModelOnly` —— 6/15 个有
- `PreviewImage` —— 4/15 个有
- `CreateVideo` —— 3/15 个有
- `EmptyImage` —— 3/15 个有
- `SaveVideo` —— 3/15 个有
- `MiniMaxH3SigmaShift` —— 2/15 个有
- `GetImageSize` —— 1/15 个有
- `H3KitSemanticBridge` —— 1/15 个有
- `ImageScaleToTotalPixels` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/15 个有
- `MiniMaxH3ImageToVideo` —— 1/15 个有
- `MiniMaxH3LowVRAMAttentionT8Advanced` —— 1/15 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 1/15 个有
- `Seed (rgthree)` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
