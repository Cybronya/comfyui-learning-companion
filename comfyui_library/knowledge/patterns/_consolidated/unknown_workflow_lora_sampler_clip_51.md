---
name: unknown_workflow_lora_sampler_clip_51
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.842143
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json, 视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json, 视频生成/文生视频/danoebook-ltx2.3-t2v_2062519416595767297.json, 视频生成/文生视频/sulphur_t2v_distilled_2051940984962985985.json, 视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json, 视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json, 视频生成/文生视频/咕咕嘎嘎？_2042845410145869826.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json、视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json、视频生成/文生视频/danoebook-ltx2.3-t2v_2062519416595767297.json、视频生成/文生视频/sulphur_t2v_distilled_2051940984962985985.json、视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 6/7 个有
- `LTXAVTextEncoderLoader` —— 6/7 个有
- `LTXVCropGuides` —— 6/7 个有
- `LTXVLatentUpsampler` —— 6/7 个有
- `LatentUpscaleModelLoader` —— 6/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `LTXVImgToVideoInplace` —— 4/7 个有
- `LTXVPreprocess` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `ResizeImageMaskNode` —— 4/7 个有
- `ResizeImagesByLongerEdge` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `DualCLIPLoader` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LTXVScheduler` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `SamplerEulerAncestral` —— 1/7 个有
- `Text` —— 1/7 个有
- `VAEDecode` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 7 | 92% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，7 个样本，取值集中（一致性 92%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
