---
name: unknown_workflow_sampler_unet_vae_250
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.827
common_nodes: [BasicGuider, BasicScheduler, BoolOperationNode, CLIPLoader, CM_BoolToInt, ComfyMathExpression, CreateVideo, ExecutionBlocker, FloatConditions, FloatToText, GetCurrentTimeNode, ImpactNeg, JjkText, KSamplerSelect, LoadImage, PrimitiveBoolean, PrimitiveFloat, RHLLMChatNode, RTXVideoSuperResolution, RandomNoise, SamplerCustomAdvanced, SaveAudioAdvanced, SaveLatent, SaveVideo, StringReplace, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAELoader, easy anythingIndexSwitch, easy mathString, ttN concat, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/Minimax图生视频20260806  (8)4步加速lora_2084192333918199809.json, 视频生成/图生视频/Minimax多参考生视频20260805_2084182454797160450.json, 视频生成/图生视频/Minimax首尾帧生视频20260806 (8)4步加速lora_2084953395093397506.json, 视频生成/图生视频/开源短剧+TVC广告Minimax多参考生视频_2084926833153372162.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_250

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Minimax图生视频20260806  (8)4步加速lora_2084192333918199809.json、视频生成/图生视频/Minimax多参考生视频20260805_2084182454797160450.json、视频生成/图生视频/Minimax首尾帧生视频20260806 (8)4步加速lora_2084953395093397506.json、视频生成/图生视频/开源短剧+TVC广告Minimax多参考生视频_2084926833153372162.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BoolOperationNode`
- `CLIPLoader`
- `CM_BoolToInt`
- `ComfyMathExpression`
- `CreateVideo`
- `ExecutionBlocker`
- `FloatConditions`
- `FloatToText`
- `GetCurrentTimeNode`
- `ImpactNeg`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RHLLMChatNode`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioAdvanced`
- `SaveLatent`
- `SaveVideo`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy mathString`
- `ttN concat`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `CM_IntToFloat` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `GetVideoComponents` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `Int` —— 2/4 个有
- `IntConditions` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `EasyCache` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `MiniMaxH3BlockCacheT8` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有
- `easy imageInsetCrop` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
