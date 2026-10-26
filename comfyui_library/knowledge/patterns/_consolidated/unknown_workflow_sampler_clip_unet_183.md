---
name: unknown_workflow_sampler_clip_unet_183
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.861143
common_nodes: [BasicScheduler, CLIPTextEncode, CreateVideo, DualCLIPLoader, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/hunyuan_video_text_to_video.json, 图片生成/反推提示词/73wenshengshipws_2052614102392033282.json, 图片生成/文生图/文生视频加速版_1993105222903988226.json, 视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json, 视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json, 视频生成/文生视频/Image_capybara_v0_1_text_to_video_fast_2027049393966292993.json, 视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v-混元Video1.5大模型——文生视频工作流_1994019108255629313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_183

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/hunyuan_video_text_to_video.json、图片生成/反推提示词/73wenshengshipws_2052614102392033282.json、图片生成/文生图/文生视频加速版_1993105222903988226.json、视频生成/文生视频/HunyuanVideo 1.5 480P 8步LightX2V文生视频加速版V1_1992951299952099329.json、视频生成/文生视频/HunyuanVideo 1.5 720P 20步优化版文生视频_1992813591025831937.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CreateVideo`
- `DualCLIPLoader`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 6/7 个有
- `EmptyHunyuanVideo15Latent` —— 6/7 个有
- `VAEDecodeTiled` —— 6/7 个有
- `EasyCache` —— 4/7 个有
- `JWInteger` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `AddLabel` —— 1/7 个有
- `BasicGuider` —— 1/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `FluxGuidance` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
