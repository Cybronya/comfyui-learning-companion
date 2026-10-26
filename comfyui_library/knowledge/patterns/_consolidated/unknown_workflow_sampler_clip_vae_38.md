---
name: unknown_workflow_sampler_clip_vae_38
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.852571
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json, 视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json, 视频生成/文生视频/danoebook-ltx2.3-t2v_2062519416595767297.json, 视频生成/文生视频/sulphur_t2v_distilled_2051940984962985985.json, 视频生成/文生视频/video_ltx2_3_i2v_GGUF_2030688003991015426.json, 视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json, 视频生成/文生视频/video_ltx2_3_i2v图生视频，音画同步视频生成，qwen3.5文本反推，_2042515888879968257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_38

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/LTX2.3文生视频工作流_2077424982275219458.json、视频生成/文生视频/Sulphur2  文生视频基础工作流_2055614181512097793.json、视频生成/文生视频/danoebook-ltx2.3-t2v_2062519416595767297.json、视频生成/文生视频/sulphur_t2v_distilled_2051940984962985985.json、视频生成/文生视频/video_ltx2_3_i2v_GGUF_2030688003991015426.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `LTXVAudioVAELoader` —— 6/7 个有
- `LTXVCropGuides` —— 6/7 个有
- `LTXVLatentUpsampler` —— 6/7 个有
- `LatentUpscaleModelLoader` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `VAEDecodeTiled` —— 6/7 个有
- `LTXAVTextEncoderLoader` —— 5/7 个有
- `LTXVImgToVideoInplace` —— 4/7 个有
- `LTXVPreprocess` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `ResizeImageMaskNode` —— 4/7 个有
- `ResizeImagesByLongerEdge` —— 4/7 个有
- `LoadImage` —— 3/7 个有
- `VAEDecode` —— 2/7 个有
- `DualCLIPLoader` —— 1/7 个有
- `DualCLIPLoaderGGUF` —— 1/7 个有
- `LTXVScheduler` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `SamplerEulerAncestral` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `VAELoaderKJ` —— 1/7 个有
- `easy getNode` —— 1/7 个有
- `easy setNode` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

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
