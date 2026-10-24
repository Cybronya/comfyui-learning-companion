---
name: unknown_workflow_sampler_clip_vae_32
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.834857
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa V2+Prompt Relay精准控制表情_2055852806652874753.json, 视频生成/图生视频/Sulphur 2+Prompt Relay精准控制表情_2054898098463354882.json, 视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json, 视频生成/文生视频/sulphur_t2v_distilled_2051940984962985985.json, 视频生成/文生视频/video_ltx2_3_i2v_GGUF_2030688003991015426.json, 视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json, 视频生成/文生视频/咕咕嘎嘎？_2042845410145869826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_32

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Dasiwa V2+Prompt Relay精准控制表情_2055852806652874753.json、视频生成/图生视频/Sulphur 2+Prompt Relay精准控制表情_2054898098463354882.json、视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json、视频生成/文生视频/sulphur_t2v_distilled_2051940984962985985.json、视频生成/文生视频/video_ltx2_3_i2v_GGUF_2030688003991015426.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `LTXVAudioVAELoader` —— 6/7 个有
- `LTXVImgToVideoInplace` —— 6/7 个有
- `LTXVPreprocess` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `LTXAVTextEncoderLoader` —— 5/7 个有
- `LTXVCropGuides` —— 5/7 个有
- `LTXVLatentUpsampler` —— 5/7 个有
- `LatentUpscaleModelLoader` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `ResizeImageMaskNode` —— 4/7 个有
- `ResizeImagesByLongerEdge` —— 4/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `VAELoaderKJ` —— 3/7 个有
- `easy getNode` —— 3/7 个有
- `easy setNode` —— 3/7 个有
- `GetNode` —— 2/7 个有
- `Int` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `PromptRelaySmartEncode` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `DualCLIPLoader` —— 1/7 个有
- `DualCLIPLoaderGGUF` —— 1/7 个有
- `LTXVScheduler` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `VAEDecode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
