---
name: unknown_workflow_lora_sampler_unet_49
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.758
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, JjkText, KSamplerSelect, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveInt, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2111005025232310273.json, 图片生成/图生图/舞蹈短片丨MiniMax H3丨首帧驱动·音画同生_2112107711432318977.json, 数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3 Image-to-Video! Long-Form Video_2107994007895896066.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站_2113791006826131458.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2084203498043957249.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2110889409909452801.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2113790005394104322.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2113802066551468034.json, 视频生成/图生视频/MiniMaxH3武状元，双人对战，效果超赞！_2114304947578818562.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2111005025232310273.json、图片生成/图生图/舞蹈短片丨MiniMax H3丨首帧驱动·音画同生_2112107711432318977.json、数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json、视频生成/图生视频/H3图生视频！长视频加速版！H3 Image-to-Video! Long-Form Video_2107994007895896066.json、视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `JjkText`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveInt`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/11 个有
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `VHS_VideoCombine` —— 9/11 个有
- `DF_Int_to_Float` —— 8/11 个有
- `RTXVideoFrameGeneration` —— 8/11 个有
- `ResolutionSelector` —— 8/11 个有
- `EmptyImage` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `CreateVideo` —— 2/11 个有
- `SaveVideo` —— 2/11 个有
- `MiniMaxH3ImageToVideo` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
