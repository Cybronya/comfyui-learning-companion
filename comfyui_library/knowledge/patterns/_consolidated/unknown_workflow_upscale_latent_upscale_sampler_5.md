---
name: unknown_workflow_upscale_latent_upscale_sampler_5
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.882769
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-I2V-GGUF_2031025711103873026.json, 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037157386359672834.json, 视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037707002851364865.json, 视频生成/图生视频/LTX2.3-首尾帧转场+Qwen3.5反推【测试版】_2038548270510776322.json, 视频生成/图生视频/LTX2.3最强首尾帧声画同步_2037742707522670593.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_guide_2031027294181003266.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2031010048406720514.json, 视频生成/图生视频/video_ltx2_3_FLframe_latent_injection_2058784933593837570.json, 视频生成/图生视频/video_ltx2_3_FLframe_transition_multi_guide_2036368754602414082.json, 视频生成/图生视频/video_ltx2_3_FLframe_transition_video_inplace_2036749082479304706.json, 视频生成/图生视频/video_ltx2_3_FMLframe_latent_injection1_2031034395125096450.json, 视频生成/文生视频/LTX2.3-文生视频三采样+自动提示词_2040703381571899393.json, 视频生成/文生视频/最新LTX 2.3  文生视频工作流 智能自动扩写提示词_2031229319539859458.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-I2V-GGUF_2031025711103873026.json、视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037157386359672834.json、视频生成/图生视频/LTX2.3-首尾帧超级转场（transition）_2037707002851364865.json、视频生成/图生视频/LTX2.3-首尾帧转场+Qwen3.5反推【测试版】_2038548270510776322.json、视频生成/图生视频/LTX2.3最强首尾帧声画同步_2037742707522670593.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 12/13 个有
- `LTXVCropGuides` —— 12/13 个有
- `LTXVImgToVideoInplace` —— 12/13 个有
- `LTXVPreprocess` —— 12/13 个有
- `ResizeImagesByLongerEdge` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `LoadImage` —— 11/13 个有
- `ImageResizeKJv2` —— 10/13 个有
- `SaveVideo` —— 10/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `PrimitiveBoolean` —— 7/13 个有
- `PrimitiveStringMultiline` —— 7/13 个有
- `ResizeImageMaskNode` —— 7/13 个有
- `LTXVAddGuideMulti` —— 6/13 个有
- `ShowText|pysssss` —— 6/13 个有
- `SimpleMath+` —— 6/13 个有
- `Text` —— 5/13 个有
- `LTXVImgToVideoInplaceKJ` —— 4/13 个有
- `RH_LLMAPI_Pro_Node` —— 4/13 个有
- `VHS_VideoCombine` —— 3/13 个有
- `EmptyImage` —— 2/13 个有
- `GetImageSize` —— 2/13 个有
- `ImageSizeInfo` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `llama_cpp_instruct_adv` —— 2/13 个有
- `llama_cpp_model_loader` —— 2/13 个有
- `Display Any (rgthree)` —— 1/13 个有
- `ImageConcanate` —— 1/13 个有
- `ImageScaleBy` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有
- `PrimitiveFloat` —— 1/13 个有
- `UnetLoaderGGUF` —— 1/13 个有
- `VAELoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
