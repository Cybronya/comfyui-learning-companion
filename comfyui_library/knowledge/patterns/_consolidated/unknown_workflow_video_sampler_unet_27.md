---
name: unknown_workflow_video_sampler_unet_27
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.600417
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, JoinStringMulti, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, PurgeVRAM_UTK, RandomNoise, SamplerCustomAdvanced, SetNode, StringConcatenate, ToString, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 Ref2VA 自用多图参考_2092052345797570562.json, 视频生成/图生视频/MiniMax H3 参考生视频 1080P高清版-9图+3音频参考-自动提示词优化-V1.6_2086990183689445377.json, 视频生成/图生视频/MiniMax H3 参考生视频-8步加速-自动提示词优化-V2_2085675916306509826.json, 视频生成/图生视频/MiniMax H3 参考生视频-lightx2v 4步加速-自动提示词优化-V1.3_2085749432846479361.json, 视频生成/图生视频/MiniMax H3 参考生视频完美版本 1080P高清-多图+多音频参考-自动提示词优化-V1.2_2091401181330501633.json, 视频生成/图生视频/MiniMax H3图片加音色参考生视频-自动提示词优化-V2.1_2083091369735843842.json, 视频生成/图生视频/绘影 - MiniMax H3参考生视频 1080P高清版-V2_2095314550949240833.json, 视频生成/图生视频/绘影-MiniMax H3 参考生视频-fl2va-bf16-720P-V2_2102641646197366785.json, 视频生成/图生视频/绘影-MiniMax H3 参考生视频-fl2va-int8-720P-V2_2102641358329700353.json, 视频生成/图生视频/绘影-MiniMax H3 参考生视频-ref2va-int8-720P-V2_2100107761043460098.json, 视频生成/图生视频/绘影-MiniMax H3 参考生视频-混合25-49-int8-720P-V2_2102552907047596033.json, 视频生成/文生视频/MiniMax H3 Ref2VA 多参考素材生视频 1080P高清版-9图+3音频参考带自动提示词_2091171246720503809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_27

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 Ref2VA 自用多图参考_2092052345797570562.json、视频生成/图生视频/MiniMax H3 参考生视频 1080P高清版-9图+3音频参考-自动提示词优化-V1.6_2086990183689445377.json、视频生成/图生视频/MiniMax H3 参考生视频-8步加速-自动提示词优化-V2_2085675916306509826.json、视频生成/图生视频/MiniMax H3 参考生视频-lightx2v 4步加速-自动提示词优化-V1.3_2085749432846479361.json、视频生成/图生视频/MiniMax H3 参考生视频完美版本 1080P高清-多图+多音频参考-自动提示词优化-V1.2_2091401181330501633.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 12 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `JoinStringMulti`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringConcatenate`
- `ToString`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `H3SigmaRefiner` —— 10/12 个有
- `MiniMaxH3SigmaShift` —— 10/12 个有
- `ModelAttentionBackend` —— 10/12 个有
- `ZNGB_ImageBatchMulti` —— 10/12 个有
- `Int` —— 7/12 个有
- `ratio_selector` —— 7/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/12 个有
- `PDRatioSelector` —— 6/12 个有
- `ConvertAny2Int` —— 5/12 个有
- `LTXVConcatAVLatent` —— 5/12 个有
- `LTXVSeparateAVLatent` —— 5/12 个有
- `MiniMaxChunkFeedForward` —— 5/12 个有
- `MiniMaxLowVRAMAttention` —— 5/12 个有
- `MinimaxH3LatentUpscaler3D` —— 5/12 个有
- `ResolutionSelector` —— 5/12 个有
- `SplitSigmas` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `ModelPreviewOverrideKJ` —— 3/12 个有
- `SolAttnMiniMax` —— 3/12 个有
- `BatchImagesNode` —— 2/12 个有
- `ComfyNumberConvert` —— 1/12 个有
- `ComfySwitchNode` —— 1/12 个有
- `Compare` —— 1/12 个有
- `CreateVideo` —— 1/12 个有
- `SaveVideo` —— 1/12 个有
- `SetReserveVRAM` —— 1/12 个有
- `SplitStringByDelimiter` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `easy ifElse` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
