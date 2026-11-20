---
name: unknown_workflow_lora_sampler_unet_28
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.739778
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2111005025232310273.json, 图片生成/图生图/舞蹈短片丨MiniMax H3丨首帧驱动·音画同生_2112107711432318977.json, "平台全量/H3图生视频H3_ Image-to-Video, Long-Form Video Acceler_2117453506549469186.json", 数字人/数字人/MiniMax H3  30秒长视频短剧+自定义音频-V1.0_2116449796264386561.json, 数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json, 视频生成/图生视频/H3全能参考Spark+selflift_2114965725633925122.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3 Image-to-Video! Long-Form Video_2107994007895896066.json, 视频生成/图生视频/H3图生视频！长视频加速版！H3_Image-to-Video!_Long-Form_Video_2110912412697325569.json, 视频生成/图生视频/MiniMax H3 长视频短剧+自定义音频-V1.0_2116431493559050242.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站_2113791006826131458.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2084203498043957249.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2110889409909452801.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2113790005394104322.json, 视频生成/图生视频/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2113802066551468034.json, 视频生成/图生视频/MiniMaxH3武状元，双人对战，效果超赞！_2114304947578818562.json, 视频生成/图生视频/MiniMax_H3_30秒长视频短剧+自定义音频-V1.0_2116700607980589057.json, 视频生成/图生视频/MiniMax_H3_30秒长视频短剧+自定义音频-V1.0_2116714833243627522.json, 视频生成/图生视频/超强Minimax H3 sigma强化+Selflift（双采）文不油 武不糊！全能(多图3音频参考)生视频高质量可长视频小脸不崩啦-量化加速版_1938828920093659137.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_28

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3图生视频！长视频加速版！B站艾橘溪_2111005025232310273.json、图片生成/图生图/舞蹈短片丨MiniMax H3丨首帧驱动·音画同生_2112107711432318977.json、平台全量/H3图生视频H3_ Image-to-Video, Long-Form Video Acceler_2117453506549469186.json、数字人/数字人/MiniMax H3  30秒长视频短剧+自定义音频-V1.0_2116449796264386561.json、数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 17/18 个有
- `LTXVSeparateAVLatent` —— 17/18 个有
- `LayerUtility: PurgeVRAM V2` —— 17/18 个有
- `MiniMaxH3ReferenceToVideo` —— 17/18 个有
- `ModelAttentionBackend` —— 17/18 个有
- `PrimitiveInt` —— 17/18 个有
- `VHS_VideoCombine` —— 16/18 个有
- `ResolutionSelector` —— 15/18 个有
- `DF_Int_to_Float` —— 13/18 个有
- `GetNode` —— 13/18 个有
- `RTXVideoFrameGeneration` —— 13/18 个有
- `SetNode` —— 13/18 个有
- `Fast Groups Bypasser (rgthree)` —— 7/18 个有
- `LoadAudio` —— 6/18 个有
- `EmptyImage` —— 4/18 个有
- `PreviewImage` —— 4/18 个有
- `CreateVideo` —— 2/18 个有
- `H3SigmaRefiner` —— 2/18 个有
- `PrimitiveFloat` —— 2/18 个有
- `SaveVideo` —— 2/18 个有
- `Any To String (mtb)` —— 1/18 个有
- `AudioCrop` —— 1/18 个有
- `CR Prompt Text` —— 1/18 个有
- `Float` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `LoraLoaderBypassModelOnly` —— 1/18 个有
- `MiniMaxH3ImageToVideo` —— 1/18 个有
- `MiniMaxH3SparkAttentionAuto` —— 1/18 个有
- `PreviewAudio` —— 1/18 个有
- `Text Concatenate` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有
- `easy seed` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
