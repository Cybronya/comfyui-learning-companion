---
name: unknown_workflow_video_lora_sampler_37
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.6864
common_nodes: [AudioSeparation, BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, DF_Int_to_Float, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadAudioUpload, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/H3无限分段长视频_Music+Digital+Avatars+_2114200257918750721.json, 图片生成/图生图/音乐数字人丨MiniMax H3丨音频驱动·对口型_2113116708411109378.json, 图片生成/图生图/音乐数字人丨MiniMax H3丨音频驱动·对口型_2113181852579221505.json, 数字人/数字人/H3 Unlimited Segmented Long-Form Videos + Music +_2114160824595083265.json, 数字人/数字人/MinimaxH3音乐数字人（无限分段长视频）_2104530829451026433.json, 数字人/数字人/MinimaxH3音乐数字人（无限分段长视频）_2104531808976199681.json, 数字人/数字人/MinimaxH3音乐数字人（无限分段长视频）艾橘溪_2100947063335899137.json, 数字人/数字人/kplei_scail.json_2109885347109883905.json, 视频生成/图生视频/H3 音频驱动 音乐数字人H3 Audio-Driven Music Avatars_2101838568909004801.json, 视频生成/图生视频/H3无限分段长视频 Music+Digital+Avatars+_2110904034117906434.json, 视频生成/图生视频/H3无限分段长视频_Music+Digital+Avatars+_2114192063163092994.json, 视频生成/图生视频/Minimax H3单图数字人（selflift无限分段长视频）2609_2106034159591444481.json, 视频生成/图生视频/Minimax-H3音乐数字人（无限分段长视频）_2101606771327594497.json, 视频生成/图生视频/Minimax-H3音乐数字人（无限分段长视频）_2101634155602866178.json, 视频生成/图生视频/MinimaxH3-音乐数字人【无限分段长视频】_2108721750065369089.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频_2110651688527941633.json, 视频生成/图生视频/MinimaxH3音乐数字人无限分段长视频_2111370884236791810.json, 视频生成/图生视频/MinimaxH3音乐数字人（无限分段长视频）-修复报错_2108876273467617281.json, 视频生成/图生视频/MinimaxH3音乐数字人（无限分段长视频）_2102314156711038978.json, 视频生成/图生视频/MinimaxH3音乐数字人（无限分段长视频）_2105100377552150529.json, 视频生成/图生视频/MinimaxH3音乐数字人（无限分段长视频）艾橘溪_2100947063335899137.json, 视频生成/图生视频/shotthree_2112434153026310145.json, 视频生成/图生视频/无限分段长视频 H3 Music Digital Avatars_2108376326993432578.json, 视频生成/文生视频/MinimaxH3音乐数字人（无限分段长视频）-修复报错_2108758135392530433.json, 视频生成/文生视频/zuixinfengjing_2113513892281413633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/H3无限分段长视频_Music+Digital+Avatars+_2114200257918750721.json、图片生成/图生图/音乐数字人丨MiniMax H3丨音频驱动·对口型_2113116708411109378.json、图片生成/图生图/音乐数字人丨MiniMax H3丨音频驱动·对口型_2113181852579221505.json、数字人/数字人/H3 Unlimited Segmented Long-Form Videos + Music +_2114160824595083265.json、数字人/数字人/MinimaxH3音乐数字人（无限分段长视频）_2104530829451026433.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 25 个 workflow 都包含：
- `AudioSeparation`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `DF_Int_to_Float`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadAudioUpload`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 24/25 个有
- `LoadImage` —— 24/25 个有
- `GetNode` —— 23/25 个有
- `MiniMaxH3ReferenceToVideo` —— 23/25 个有
- `SetNode` —— 23/25 个有
- `SoundFlow_GetLength` —— 23/25 个有
- `ModelPreviewOverrideKJ` —— 22/25 个有
- `PreviewImage` —— 21/25 个有
- `Compare` —— 20/25 个有
- `Int` —— 20/25 个有
- `InversionDemoLazySwitch` —— 20/25 个有
- `PreviewAudio` —— 20/25 个有
- `LoadAudio` —— 3/25 个有
- `PreviewAny` —— 3/25 个有
- `JjkText` —— 2/25 个有
- `LayerUtility: TextJoin` —— 2/25 个有
- `MiniMaxH3ImageToVideo` —— 2/25 个有
- `孤海注释` —— 2/25 个有
- `EmptyImage` —— 1/25 个有
- `FlashVSRNode` —— 1/25 个有
- `ImageFromBatch` —— 1/25 个有
- `Make Image Batch` —— 1/25 个有
- `TrimAudioDuration` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
