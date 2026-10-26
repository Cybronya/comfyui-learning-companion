---
name: unknown_workflow_lora_sampler_unet_324
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9185
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, CreateVideo, Fast Groups Bypasser (rgthree), GetLatentSizeAndCount, H3SigmaRefiner, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PlaySound|pysssss, SaveImage, SaveVideo, Seed (rgthree), SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy imageChooser, kkVideoFirstLastFrames]
problems: []
missing: []
members: ["视频生成/图生视频/Amumu-数字人15s直出1080P,16分钟左右，新用户绑定  rh-v1571体验_2100601806509395970.json", "视频生成/图生视频/Amumu-数字人自动提示词，15s直出1080P,16分钟左右，新用户绑定  rh-v1571体验_2101011759321669634.json"]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_324

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Amumu-数字人15s直出1080P,16分钟左右，新用户绑定  rh-v1571体验_2100601806509395970.json、视频生成/图生视频/Amumu-数字人自动提示词，15s直出1080P,16分钟左右，新用户绑定  rh-v1571体验_2101011759321669634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetLatentSizeAndCount`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PlaySound|pysssss`
- `SaveImage`
- `SaveVideo`
- `Seed (rgthree)`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy imageChooser`
- `kkVideoFirstLastFrames`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ComfyNumberConvert` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MiniMaxH3EasyMediaLoader` —— 1/2 个有
- `MiniMaxH3EasyMediaSplitter` —— 1/2 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
