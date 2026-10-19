---
name: unknown_workflow_lora_sampler_clip_43
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.815333
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2055852806652874753.json, 视频生成/图生视频/2054898098463354882.json, 视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json, 视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json, 视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json, 视频生成/文生视频/咕咕嘎嘎？_2042845410145869826.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2055852806652874753.json、视频生成/图生视频/2054898098463354882.json、视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json、视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json、视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXAVTextEncoderLoader` —— 5/6 个有
- `LTXVImgToVideoInplace` —— 5/6 个有
- `LTXVPreprocess` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LTXVCropGuides` —— 4/6 个有
- `LTXVLatentUpsampler` —— 4/6 个有
- `LatentUpscaleModelLoader` —— 4/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `ResizeImageMaskNode` —— 3/6 个有
- `ResizeImagesByLongerEdge` —— 3/6 个有
- `easy getNode` —— 3/6 个有
- `easy setNode` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `Int` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `PromptRelaySmartEncode` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `VAELoaderKJ` —— 2/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
